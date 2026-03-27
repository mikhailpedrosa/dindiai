import google.generativeai as genai
import os
import json
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class AIAgent:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY não encontrada no ambiente (.env)")
        genai.configure(api_key=api_key)
        # Seleção dinâmica de modelo para evitar 405 Method Not Allowed
        try:
            available_models = [m.name for m in genai.list_models() if "generateContent" in m.supported_generation_methods]
            print(f"Modelos disponíveis: {available_models}")
            if "models/gemini-1.5-flash" in available_models:
                self.model_name = "models/gemini-1.5-flash"
            elif available_models:
                self.model_name = available_models[0]
            else:
                self.model_name = "gemini-pro"
            self.model = genai.GenerativeModel(self.model_name)
        except Exception as e:
            print(f"Erro ao listar modelos: {e}. Usando fallback.")
            self.model = genai.GenerativeModel("gemini-pro")

    def generate_report(self, summary_data: Dict[str, Any]) -> str:
        """
        Gera um relatório financeiro completo via Especialista em Finanças Pessoais.
        """
        prompt = self._build_prompt(summary_data)
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Erro ao gerar relatório com IA: {str(e)}"

    def _build_prompt(self, data: Dict[str, Any]) -> str:
        metrics = data.get("metricas_gerais", {})
        categories = data.get("categorias", {})
        essential = data.get("analise_essencial", {})

        prompt = f"""
        Você é um Especialista em Finanças Pessoais experiente e sênior, focado em metodologias de prosperidade e equilíbrio financeiro.
        Seu objetivo é analisar os dados financeiros de um usuário e gerar um relatório completo, didático e motivador que transforme sua relação com o dinheiro.

        DIRETRIZES ESTRATÉGICAS:
        - Priorizar a organização de um orçamento mensal rígido.
        - Focar na redução de gastos não essenciais (supérfluos) para gerar capacidade de poupança.
        - Se houver dívidas, focar na renegociação e no estancamento de juros altos.
        - Enfatizar a criação de uma reserva de emergência antes de qualquer investimento.
        - Manter uma mentalidade de abundância através da disciplina e planejamento.

        DADOS FINANCEIROS (Mês Atual):
        - Receita Total: R$ {metrics.get('receita_total', 0):.2f}
        - Despesa Total: R$ {metrics.get('despesa_total', 0):.2f}
        - Saldo Mensal: R$ {metrics.get('saldo_mensal', 0):.2f}
        - Capacidade de Poupança: {metrics.get('capacidade_poupanca_perc', 0):.1f}%
        - Endividamento Atual: R$ {metrics.get('endividamento', 0):.2f}

        Gasto por Categoria:
        {json.dumps(categories.get('gastos', {}), indent=2)}

        Análise de Essencialidade:
        - Gastos Essenciais: R$ {essential.get('essencial', 0):.2f} ({essential.get('perc_essencial', 0):.1f}%)
        - Gastos Não Essenciais (Supérfluos): R$ {essential.get('nao_essencial', 0):.2f}

        REGRAS DO RELATÓRIO:
        1. Use linguagem simples, humana e estratégica.
        2. FOCO: Organização, disciplina e prosperidade.
        3. Se o saldo for negativo, priorize o "Plano para Sair do Vermelho".
        4. O relatório DEVE conter estas seções:
           ## Diagnóstico Financeiro
           ## Análise de Gastos (Pontos críticos)
           ## Plano para Sair do Vermelho (Metas de 30, 60 e 90 dias)
           ## Estratégia de Recuperação Financeira
           ## Plano de Ação (Ações práticas imediatas)
           ## Recomendações Personalizadas

        Responda em PORTUGUÊS (Brasil), mantendo o tom de um consultor sênior que quer o sucesso do cliente.
        """
        return prompt
