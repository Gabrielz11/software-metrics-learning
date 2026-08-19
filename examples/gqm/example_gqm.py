"""Exemplo Prático: Modelo GQM (Goal-Question-Metric) Aplicado ao Sistema de Biblioteca.

Demonstra como estruturar a derivação de métricas a partir de um objetivo de negócio.
"""


def main():
    print("=== MODELO GQM APLICADO AO SISTEMA DE BIBLIOTECA ===")

    gqm_tree = {
        "Goal": {
            "Objeto": "Processo de Lançamento e Qualidade do Sistema de Biblioteca",
            "Propósito": "Avaliar e melhorar a confiabilidade das releases",
            "Foco": "Redução do número de falhas percebidas pelos usuários",
            "Ponto de Vista": "Gerente de Engenharia e Equipe de QA",
            "Contexto": "Ambiente de produção do Sistema de Biblioteca",
        },
        "Questions": [
            {
                "ID": "Q1",
                "Texto": "Qual é a densidade atual de defeitos encontrados pelos clientes em produção?",
                "Metrics": [
                    "Defeitos Pós-Release / KLOC",
                    "Defeitos Pós-Release / Ponto de Função",
                ],
            },
            {
                "ID": "Q2",
                "Texto": "Quão eficaz é nossa etapa de testes automatizados antes do deploy?",
                "Metrics": [
                    "Defect Removal Efficiency (DRE %)",
                    "Percentual de Cobertura de Testes de Código (%)",
                ],
            },
            {
                "ID": "Q3",
                "Texto": "Qual é a velocidade de resposta da equipe para corrigir defeitos críticos?",
                "Metrics": [
                    "Mean Time to Repair (MTTR em horas)",
                ],
            },
        ],
    }

    print(f"\n🎯 GOAL (OBJETIVO DE NEGÓCIO):")
    for k, v in gqm_tree["Goal"].items():
        print(f"  - {k}: {v}")

    print(f"\n❓ PERGUNTAS E 📊 MÉTRICAS DERIVADAS:")
    for q in gqm_tree["Questions"]:
        print(f"\n  [Pergunta {q['ID']}]: {q['Texto']}")
        for m in q["Metrics"]:
            print(f"    └── Métrica: {m}")


if __name__ == "__main__":
    main()
