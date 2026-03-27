import pandas as pd
from datetime import datetime, timedelta
import random
import os

def generate_sample_spreadsheet(filename="data/exemplo_financas.xlsx"):
    # Ensure data directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Template columns: data | descricao | categoria | tipo (receita ou despesa) | valor
    base_date = datetime(2026, 1, 1)
    
    data = [
        # Receitas Fixas
        {"data": (base_date).strftime("%Y-%m-%d"), "descricao": "Salário Mensal", "categoria": "Renda", "tipo": "receita", "valor": 5500.00},
        {"data": (base_date + timedelta(days=14)).strftime("%Y-%m-%d"), "descricao": "Freelance Design", "categoria": "Extra", "tipo": "receita", "valor": 850.00},
        
        # Despesas Fixas
        {"data": (base_date + timedelta(days=4)).strftime("%Y-%m-%d"), "descricao": "Aluguel + Condomínio", "categoria": "Moradia", "tipo": "despesa", "valor": 2200.00},
        {"data": (base_date + timedelta(days=5)).strftime("%Y-%m-%d"), "descricao": "Conta de Luz", "categoria": "Contas Fixas", "tipo": "despesa", "valor": 180.00},
        {"data": (base_date + timedelta(days=6)).strftime("%Y-%m-%d"), "descricao": "Internet Fibra", "categoria": "Contas Fixas", "tipo": "despesa", "valor": 120.00},
        {"data": (base_date + timedelta(days=7)).strftime("%Y-%m-%d"), "descricao": "Seguro Saúde", "categoria": "Saúde", "tipo": "despesa", "valor": 450.00},
        
        # Despesas Variáveis (Alimentação)
        {"data": (base_date + timedelta(days=2)).strftime("%Y-%m-%d"), "descricao": "Supermercado Semanal 1", "categoria": "Alimentação", "tipo": "despesa", "valor": 350.00},
        {"data": (base_date + timedelta(days=9)).strftime("%Y-%m-%d"), "descricao": "Supermercado Semanal 2", "categoria": "Alimentação", "tipo": "despesa", "valor": 420.00},
        {"data": (base_date + timedelta(days=16)).strftime("%Y-%m-%d"), "descricao": "Jantar Fora (Delivery)", "categoria": "Lazer", "tipo": "despesa", "valor": 120.00},
        {"data": (base_date + timedelta(days=23)).strftime("%Y-%m-%d"), "descricao": "Churrasco com Amigos", "categoria": "Lazer", "tipo": "despesa", "valor": 200.00},
        
        # Transporte
        {"data": (base_date + timedelta(days=10)).strftime("%Y-%m-%d"), "descricao": "Combustível Carro", "categoria": "Transporte", "tipo": "despesa", "valor": 250.00},
        {"data": (base_date + timedelta(days=20)).strftime("%Y-%m-%d"), "descricao": "Manutenção Preventiva", "categoria": "Transporte", "tipo": "despesa", "valor": 600.00},
        
        # Outros / Supérfluos (Para testar o diagnóstico "SAIR DO VERMELHO")
        {"data": (base_date + timedelta(days=12)).strftime("%Y-%m-%d"), "descricao": "Streaming Bundle", "categoria": "Assinaturas", "tipo": "despesa", "valor": 95.00},
        {"data": (base_date + timedelta(days=25)).strftime("%Y-%m-%d"), "descricao": "Roupas Novas (Shopping)", "categoria": "Compras", "tipo": "despesa", "valor": 550.00},
        {"data": (base_date + timedelta(days=28)).strftime("%Y-%m-%d"), "descricao": "Gasto Não Identificado", "categoria": "Outros", "tipo": "despesa", "valor": 300.00},
    ]
    
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Planilha de exemplo gerada em: {filename}")

if __name__ == "__main__":
    generate_sample_spreadsheet()
