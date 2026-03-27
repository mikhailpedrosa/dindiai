import requests
import os

def test_analysis():
    url = "http://localhost:8000/api/finance/analyze"
    file_path = "data/exemplo_financas.xlsx"
    
    if not os.path.exists(file_path):
        print(f"Erro: Arquivo {file_path} não encontrado.")
        return

    print(f"Enviando {file_path} para análise...")
    
    with open(file_path, "rb") as f:
        files = {"file": f}
        try:
            response = requests.post(url, files=files)
            if response.status_code == 200:
                result = response.json()
                print("\n=== SUCESSO! RESUMO FINANCEIRO ===")
                print(f"Receita Total: R$ {result['summary']['metricas_gerais']['receita_total']}")
                print(f"Despesa Total: R$ {result['summary']['metricas_gerais']['despesa_total']}")
                print(f"Saldo: R$ {result['summary']['metricas_gerais']['saldo_mensal']}")
                
                print("\n=== RELATÓRIO DO AGENTE (GEMINI) ===")
                print(result['report_text'][:500] + "...") # Primeiros 500 chars
                print("\n...relatório completo recebido.")
            else:
                print(f"Erro na análise: {response.status_code}")
                print(response.text)
        except Exception as e:
            print(f"Erro na requisição: {e}")

if __name__ == "__main__":
    test_analysis()
