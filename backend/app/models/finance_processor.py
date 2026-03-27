import pandas as pd
import numpy as np
from typing import Dict, Any, List

class FinanceProcessor:
    def __init__(self):
        # Categorias consideradas essenciais (exemplo base)
        self.essential_categories = ['Moradia', 'Saúde', 'Contas Fixas', 'Educação', 'Transporte']

    def process_spreadsheet(self, file_path: str) -> Dict[str, Any]:
        """
        Lê a planilha e retorna um resumo estruturado dos indicadores.
        """
        try:
            if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                df = pd.read_excel(file_path)
            else:
                df = pd.read_csv(file_path)

            # Padronização de nomes de colunas
            df.columns = [c.lower().strip() for c in df.columns]
            
            # Validação básica
            required_cols = ['data', 'descricao', 'categoria', 'tipo', 'valor']
            for col in required_cols:
                if col not in df.columns:
                    raise ValueError(f"Coluna obrigatória ausente: {col}")

            # Limpeza
            df['valor'] = pd.to_numeric(df['valor'], errors='coerce').fillna(0)
            df['tipo'] = df['tipo'].str.lower().str.strip()
            df['data'] = pd.to_datetime(df['data'], errors='coerce')

            # Indicadores de Topo
            receita_total = df[df['tipo'] == 'receita']['valor'].sum()
            despesa_total = df[df['tipo'] == 'despesa']['valor'].sum()
            saldo_mensal = receita_total - despesa_total

            # Gastos por Categoria
            gastos_por_categoria = df[df['tipo'] == 'despesa'].groupby('categoria')['valor'].sum().to_dict()
            receitas_por_categoria = df[df['tipo'] == 'receita'].groupby('categoria')['valor'].sum().to_dict()

            # Percentual por Categoria (sobre despesa total)
            percentual_por_categoria = {}
            if despesa_total > 0:
                for cat, valor in gastos_por_categoria.items():
                    percentual_por_categoria[cat] = (valor / despesa_total) * 100

            # Gastos Essenciais vs Não Essenciais
            df['is_essential'] = df['categoria'].apply(lambda x: any(ec.lower() in str(x).lower() for ec in self.essential_categories))
            
            despesas_essenciais = df[(df['tipo'] == 'despesa') & (df['is_essential'])]['valor'].sum()
            despesas_nao_essenciais = despesa_total - despesas_essenciais

            # Capacidade de Poupança
            capacidade_poupanca = (saldo_mensal / receita_total * 100) if receita_total > 0 else 0

            # Endividamento (Simples: se saldo < 0)
            endividamento = max(0, -saldo_mensal)

            # Preparação dos dados para o Agent Gemini (JSON)
            summary = {
                "metricas_gerais": {
                    "receita_total": float(receita_total),
                    "despesa_total": float(despesa_total),
                    "saldo_mensal": float(saldo_mensal),
                    "capacidade_poupanca_perc": float(capacidade_poupanca),
                    "endividamento": float(endividamento)
                },
                "categorias": {
                    "gastos": {k: float(v) for k, v in gastos_por_categoria.items()},
                    "receitas": {k: float(v) for k, v in receitas_por_categoria.items()},
                    "percentual_gastos": {k: float(v) for k, v in percentual_por_categoria.items()}
                },
                "analise_essencial": {
                    "essencial": float(despesas_essenciais),
                    "nao_essencial": float(despesas_nao_essenciais),
                    "perc_essencial": (despesas_essenciais / despesa_total * 100) if despesa_total > 0 else 0
                },
                "transacoes": df.to_dict('records') # Para referência se necessário
            }

            return summary

        except Exception as e:
            return {"error": str(e)}
