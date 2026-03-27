import pandas as pd
from datetime import datetime, timedelta
import os

def generate_debt_spreadsheet(filename="data/exemplo_dividas.xlsx"):
    # Ensure data directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    base_date = datetime(2026, 1, 1)
    
    data = [
        # Receitas (Saldo Baixo)
        {"data": (base_date).strftime("%Y-%m-%d"), "descricao": "Salário", "categoria": "Renda", "tipo": "receita", "valor": 3200.00},
        
        # Despesas Fixas Altas (Comprometimento de Renda)
        {"data": (base_date + timedelta(days=5)).strftime("%Y-%m-%d"), "descricao": "Aluguel Atrasado + Multa", "categoria": "Moradia", "tipo": "despesa", "valor": 1600.00},
        {"data": (base_date + timedelta(days=6)).strftime("%Y-%m-%d"), "descricao": "Prestação Carro", "categoria": "Transporte", "tipo": "despesa", "valor": 850.00},
        {"data": (base_date + timedelta(days=7)).strftime("%Y-%m-%d"), "descricao": "Condomínio", "categoria": "Moradia", "tipo": "despesa", "valor": 450.00},
        {"data": (base_date + timedelta(days=10)).strftime("%Y-%m-%d"), "descricao": "Empréstimo Pessoal", "categoria": "Dívidas", "tipo": "despesa", "valor": 600.00},
        
        # Despesas Variáveis Excessivas
        {"data": (base_date + timedelta(days=2)).strftime("%Y-%m-%d"), "descricao": "Supermercado (Cartão)", "categoria": "Alimentação", "tipo": "despesa", "valor": 700.00},
        {"data": (base_date + timedelta(days=15)).strftime("%Y-%m-%d"), "descricao": "Jantares e Festas", "categoria": "Lazer", "tipo": "despesa", "valor": 950.00},
        {"data": (base_date + timedelta(days=20)).strftime("%Y-%m-%d"), "descricao": "Compras Impulsivas", "categoria": "Compras", "tipo": "despesa", "valor": 1200.00},
        {"data": (base_date + timedelta(days=22)).strftime("%Y-%m-%d"), "descricao": "Anuidade Cartão Black", "categoria": "Taxas", "tipo": "despesa", "valor": 150.00},
        
        # Juros
        {"data": (base_date + timedelta(days=28)).strftime("%Y-%m-%d"), "descricao": "Juros Cheque Especial", "categoria": "Dívidas", "tipo": "despesa", "valor": 280.00},
    ]
    
    # Total Ganho: 3200
    # Total Gasto: 6780
    # Saldo: -3580
    
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Planilha de 'Finanças Comprometidas' gerada em: {filename}")

if __name__ == "__main__":
    generate_debt_spreadsheet()
