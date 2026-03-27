# Plano de Implementação — MVP Agente de Finanças Pessoais (Dindiai)

Este projeto visa criar um Agente Inteligente de Finanças Pessoais inspirado na metodologia de Gustavo Cerbasi, utilizando uma arquitetura MVC robusta e uma stack moderna.

## Objetivos
1.  **Frontend**: Interface Next.js premium com dashboard interativo e upload de planilhas.
2.  **Backend**: API FastAPI para processamento de dados e integração com **Gemini API**.
3.  **IA**: Agente que gera diagnóstico, plano de saída do vermelho e recomendações personalizadas.
4.  **Dados**: Processamento de Excel/CSV via Pandas e persistência em **SQLite** (inicialmente).
5.  **Exportação**: Geração de relatórios em **PDF, .doc e Markdown**.

## Arquitetura Proposta

### Camadas (MVC)
- **Model**: Lógica de processamento de dados financeiros (Pandas) e esquemas de banco de dados (SQLAlchemy/SQLite).
- **Controller**: Endpoints da API que coordenam o upload, processamento e chamadas ao Agente de IA.
- **View**: Dashboard React (Next.js) com gráficos dinâmicos (Chart.js/Recharts) e relatórios formatados.

## Mudanças Propostas

### 1. Estrutura do Projeto
- `backend/`: Código Python (FastAPI).
- `frontend/`: Código JavaScript/TypeScript (Next.js).
- `data/`: Armazenamento local (SQLite e Planilhas).

### 2. Backend (FastAPI) [NEW]
#### `backend/main.py`
Ponto de entrada da aplicação.
#### `backend/app/models/finance_processor.py`
Processamento de planilhas usando Pandas. Cálculo de indicadores (Receita, Despesa, Saldo, Categorias).
#### `backend/app/services/ai_agent.py`
Integração com **Gemini API** para gerar o relatório "estilo Cerbasi".
#### `backend/app/services/exporter.py`
Serviço para exportação em PDF, Docx e Markdown.
#### `backend/app/controllers/finance_controller.py`
Endpoints de upload e análise.

### 3. Frontend (Next.js) [NEW]
#### `frontend/src/app/page.tsx`
Landing page e dashboard principal.
#### `frontend/src/components/UploadZone.tsx`
Componente moderno de Drag & Drop para planilhas.
#### `frontend/src/components/Dashboard.tsx`
Gráficos e indicadores visuais.
#### `frontend/src/components/ReportViewer.tsx`
Exibição do relatório gerado pela IA.

## Requisitos de Estética (Rich Aesthetics)
- **Paleta de Cores**: Tons de verde esmeralda, cinza profundo e toques de dourado (estética "Premium Finance").
- **Tipografia**: Outfit ou Inter.
- **Interações**: Micro-animações no upload e transições suaves nos gráficos.

## Perguntas em Aberto
> [!IMPORTANT]
> 1. Deseja que eu gere uma planilha de exemplo para testes iniciais? (Confirmado: Sim)

## Plano de Verificação

### Testes de Integração
- Simular upload de CSV/Excel.
- Validar cálculos de saldo e categorias no backend.
- Verificar a resposta do Agente OpenAI.

### Verificação Manual
- Validar responsividade do dashboard.
- Testar o fluxo completo: Upload -> Processamento -> Relatório IA.
