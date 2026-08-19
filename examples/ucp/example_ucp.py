"""Exemplo Prático: Cálculo de Use Case Points (UCP) no Sistema de Biblioteca.

Demonstra o cálculo de UCP para o Sistema de Biblioteca fictício.
"""

from software_metrics.use_case_points import (
    UseCasePointCalculator,
    ActorComplexity,
    UseCaseComplexity,
)


def main():
    print("=== ESTUDO DE CASO: USE CASE POINTS (SISTEMA DE BIBLIOTECA) ===")

    calc = UseCasePointCalculator()

    # 1. Identificação de Atores
    # Leitor (humano via Web GUI -> Complexo = 3)
    calc.add_actor("Leitor", ActorComplexity.COMPLEX)
    # Bibliotecário (humano via Web GUI -> Complexo = 3)
    calc.add_actor("Bibliotecario", ActorComplexity.COMPLEX)
    # Sistema de Pagamento / Serasa (API Externa -> Simples = 1)
    calc.add_actor("ServicoExternoCredito", ActorComplexity.SIMPLE)

    # 2. Identificação de Casos de Uso
    # UC01: Manter Usuários (4 transações -> Média = 10)
    calc.add_use_case("UC01_ManterUsuarios", UseCaseComplexity.AVERAGE)
    # UC02: Manter Acervo (4 transações -> Média = 10)
    calc.add_use_case("UC02_ManterAcervo", UseCaseComplexity.AVERAGE)
    # UC03: Realizar Empréstimo (8 transações com validações -> Complexa = 15)
    calc.add_use_case("UC03_RealizarEmprestimo", UseCaseComplexity.COMPLEX)
    # UC04: Registrar Devolução (3 transações -> Simples = 5)
    calc.add_use_case("UC04_RegistrarDevolucao", UseCaseComplexity.SIMPLE)
    # UC05: Pesquisar Livros (2 transações -> Simples = 5)
    calc.add_use_case("UC05_PesquisarLivros", UseCaseComplexity.SIMPLE)

    # Ajustando alguns Fatores Ambientais/Técnicos do time fictício
    calc.set_technical_rating("T2", 4)  # Desempenho alto exigido
    calc.set_technical_rating("T11", 4)  # Recursos de segurança
    calc.set_environmental_rating("E1", 4)  # Boa experiência com o processo
    calc.set_environmental_rating("E3", 4)  # Alta experiência em Orientação a Objetos

    summary = calc.summary(productivity_factor=20.0)

    print(f"UAW  (Peso Atores):            {summary['uaw']}")
    print(f"UUCW (Peso Casos de Uso):       {summary['uucw']}")
    print(f"UUCP (Pontos Não Ajustados):   {summary['uucp']}")
    print(f"TCF  (Fator Técnico):           {summary['tcf']}")
    print(f"ECF  (Fator Ambiental):         {summary['ecf']}")
    print(f"--------------------------------------------------")
    print(f"TOTAL UCP:                      {summary['ucp']} UCP")
    print(f"ESFORÇO ESTIMADO (20h/UCP):     {summary['estimated_effort_hours']} horas")


if __name__ == "__main__":
    main()
