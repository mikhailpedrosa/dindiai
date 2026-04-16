# DindiAI - Agente de Finanças Pessoais

DindiAI é um agente inteligente de finanças pessoais desenvolvido para ajudar os usuários a gerenciar suas dívidas e investimentos de forma automatizada e amigável. Utilizando tecnologias modernas de IA, o sistema analisa planilhas financeiras e gera recomendações personalizadas no estilo de consultores renomados.

## 🚀 Estrutura do Projeto

Abaixo está a organização das pastas e arquivos principais do projeto:

```text
dindiai/
├── backend/                # Backend em FastAPI
│   ├── app/                # Lógica principal da aplicação
│   │   ├── controllers/    # Rotas da API (Ex: finance_controller.py)
│   │   ├── models/         # Modelos de dados e processamento (Ex: db_models.py, finance_processor.py)
│   │   ├── services/       # Serviços de negócio (Ex: ai_agent.py, exporter.py)
│   │   └── utils/          # Funções utilitárias
│   ├── uploads/            # Pasta para arquivos enviados pelos usuários
│   ├── dindiai.db          # Banco de dados SQLite
│   ├── main.py             # Ponto de entrada do backend
│   └── requirements.txt    # Dependências Python
├── frontend/               # Frontend em Next.js
│   ├── public/             # Arquivos estáticos
│   ├── src/                # Código-fonte do frontend
│   │   ├── app/            # Estrutura de rotas (App Router do Next.js)
│   │   └── components/     # Componentes React reutilizáveis
│   ├── package.json        # Dependências e scripts do frontend
│   └── tsconfig.json       # Configuração do TypeScript
├── data/                   # Amostras de dados e exemplos de planilhas
│   ├── exemplo_dividas.xlsx
│   └── exemplo_financas.xlsx
├── generate_debt_sample.py # Script para gerar dados de exemplo de dívidas
├── generate_sample.py      # Script para gerar dados de exemplo financeiro global
├── test_api.py             # Script de testes da API
└── README.md               # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python, FastAPI, SQLite, Gemini AI SDK.
- **Frontend**: React, Next.js, TailwindCSS (opcional/conforme solicitado), Lucide React para ícones.
- **Data**: Pandas e Openpyxl para processamento de planilhas.

## 📖 Como Rodar o Projeto

1. **Backend**:
   - Navegue até a pasta `backend/`.
   - Crie um ambiente virtual: `python -m venv .venv`.
   - Instale as dependências: `pip install -r requirements.txt`.
   - Configure sua chave da API no arquivo `.env`.
   - Execute: `python main.py`.

2. **Frontend**:
   - Navegue até a pasta `frontend/`.
   - Git Clone https://github.com/mikhailpedrosa/dindinai-frontend.git
   - Instale as dependências: `npm install`.
   - Inicie o servidor de desenvolvimento: `npm run dev`.

---
Desenvolvido com o objetivo de democratizar o acesso à consultoria financeira pessoal.
