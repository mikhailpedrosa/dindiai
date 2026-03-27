from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from ..models.finance_processor import FinanceProcessor
from ..services.ai_agent import AIAgent
from ..services.exporter import Exporter
from ..models.db_models import SessionLocal, FinancialAnalysis, init_db
import os
import shutil
from datetime import datetime

router = APIRouter()
processor = FinanceProcessor()
exporter = Exporter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Caminho temporário para uploads
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

@router.post("/analyze")
async def analyze_finance(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """
    Upload da planilha, processamento de dados e geração de relatório IA.
    """
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        # 1. Processar dados via Model
        summary = processor.process_spreadsheet(file_path)
        if "error" in summary:
            raise HTTPException(status_code=400, detail=summary["error"])
        
        # 2. Chamar Agente IA (Gemini)
        agent = AIAgent()
        report_text = agent.generate_report(summary)
        
        # 3. Salvar no Banco (SQLite)
        metrics = summary["metricas_gerais"]
        db_analysis = FinancialAnalysis(
            filename=file.filename,
            receita_total=metrics["receita_total"],
            despesa_total=metrics["despesa_total"],
            saldo_mensal=metrics["saldo_mensal"],
            report_text=report_text,
            created_at=datetime.now().isoformat()
        )
        db.add(db_analysis)
        db.commit()
        db.refresh(db_analysis)
        
        return {
            "id": db_analysis.id,
            "summary": summary,
            "report_text": report_text
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Opcional: remover arquivo após processar
        # os.remove(file_path)
        pass

@router.get("/export/{analysis_id}/{format}")
async def export_report(analysis_id: int, format: str, db: Session = Depends(get_db)):
    """
    Exporta uma análise existente para o formato solicitado.
    """
    analysis = db.query(FinancialAnalysis).filter(FinancialAnalysis.id == analysis_id).first()
    if not analysis:
        raise HTTPException(status_code=404, detail="Análise não encontrada")
    
    report_text = analysis.report_text
    export_dir = "exports"
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)
        
    filename = f"relatorio_{analysis_id}"
    
    if format == "pdf":
        path = exporter.export_pdf(report_text, os.path.join(export_dir, f"{filename}.pdf"))
    elif format == "docx" or format == "doc":
        path = exporter.export_docx(report_text, os.path.join(export_dir, f"{filename}.docx"))
    elif format == "md":
        path = exporter.export_markdown(report_text, os.path.join(export_dir, f"{filename}.md"))
    else:
        raise HTTPException(status_code=400, detail="Formato não suportado: pdf, docx, doc, md")
    
    # Em um cenário real, você retornaria o FileResponse
    # Para o MVP, vamos apenas retornar o caminho relativo
    return {"file_path": path, "filename": os.path.basename(path)}
