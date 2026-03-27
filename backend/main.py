from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import finance_controller
from app.models.db_models import init_db
import uvicorn
import os

app = FastAPI(title="Dindiai API", description="Agente de Finanças Pessoais MVP")

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permitir do frontend Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar Banco de Dados
@app.on_event("startup")
def startup_event():
    init_db()

# Incluir Rotas
app.include_router(finance_controller.router, prefix="/api/finance", tags=["Finance"])

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Dindiai API is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
