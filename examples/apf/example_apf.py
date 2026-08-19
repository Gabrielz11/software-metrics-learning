"""Exemplo Prático: Análise de Pontos de Função (APF) no Sistema de Biblioteca.

Demonstra a contagem funcional do Sistema de Biblioteca fictício conforme IFPUG CPM.
"""

from software_metrics.function_points import (
    FunctionPointCalculator,
    DataFunctionType,
    TransactionType,
)


def main():
    print("=== ESTUDO DE CASO: ANÁLISE DE PONTOS DE FUNÇÃO (SISTEMA DE BIBLIOTECA) ===")

    calc = FunctionPointCalculator()

    # 1. Funções de Dados (ALIs e AIEs)
    # ALI: Usuário (DET: id, nome, email, cpf, pendente; RET: Usuário) -> 5 DET, 1 RET -> Baixa (7 PF)
    calc.add_data_function("ALI_Usuario", DataFunctionType.ALI, ret=1, det=5)

    # ALI: Livro (DET: id, titulo, autor, isbn, disponivel, categoria; RET: Livro) -> 6 DET, 1 RET -> Baixa (7 PF)
    calc.add_data_function("ALI_Livro", DataFunctionType.ALI, ret=1, det=6)

    # ALI: Empréstimo (DET: id, usuario_id, livro_id, data_emprestimo, data_devolucao, status; RET: Emprestimo) -> 6 DET, 1 RET -> Baixa (7 PF)
    calc.add_data_function("ALI_Emprestimo", DataFunctionType.ALI, ret=1, det=6)

    # AIE: Serviço de Serasa/Crédito (DET: cpf, status_credito, restritivo; RET: ConsultaCredito) -> 3 DET, 1 RET -> Baixa (5 PF)
    calc.add_data_function("AIE_SerasaCredito", DataFunctionType.AIE, ret=1, det=3)

    # 2. Funções Transacionais (EE, SE, CE)
    # EE: Cadastrar Usuário (FTR: ALI_Usuario; DET: nome, email, cpf -> 3 DET) -> Baixa (3 PF)
    calc.add_transactional_function("EE_CadastrarUsuario", TransactionType.EE, ftr=1, det=3)

    # EE: Atualizar Usuário (FTR: ALI_Usuario; DET: id, nome, email -> 3 DET) -> Baixa (3 PF)
    calc.add_transactional_function("EE_AtualizarUsuario", TransactionType.EE, ftr=1, det=3)

    # EE: Cadastrar Livro (FTR: ALI_Livro; DET: titulo, autor, isbn -> 3 DET) -> Baixa (3 PF)
    calc.add_transactional_function("EE_CadastrarLivro", TransactionType.EE, ftr=1, det=3)

    # EE: Realizar Empréstimo (FTR: ALI_Emprestimo, ALI_Livro, ALI_Usuario; DET: usuario_id, livro_id -> 2 DET, 3 FTR) -> Média (4 PF)
    calc.add_transactional_function("EE_RealizarEmprestimo", TransactionType.EE, ftr=3, det=2)

    # EE: Registrar Devolução (FTR: ALI_Emprestimo, ALI_Livro; DET: emprestimo_id -> 1 DET, 2 FTR) -> Baixa (3 PF)
    calc.add_transactional_function("EE_RegistrarDevolucao", TransactionType.EE, ftr=2, det=1)

    # CE: Consultar Livro (FTR: ALI_Livro; DET: titulo_busca, lista_resultados -> 5 DET, 1 FTR) -> Baixa (3 PF)
    calc.add_transactional_function("CE_ConsultarLivro", TransactionType.CE, ftr=1, det=5)

    # CE: Consultar Empréstimos (FTR: ALI_Emprestimo, ALI_Usuario; DET: usuario_id, lista_emprestimos -> 4 DET, 2 FTR) -> Baixa (3 PF)
    calc.add_transactional_function("CE_ConsultarEmprestimos", TransactionType.CE, ftr=2, det=4)

    # SE: Relatório de Empréstimos Atrasados (FTR: ALI_Emprestimo, ALI_Usuario, ALI_Livro; DET: total_atrasados, lista_detalhada, grafico -> 8 DET, 3 FTR) -> Média (5 PF)
    calc.add_transactional_function("SE_RelatorioAtrasos", TransactionType.SE, ftr=3, det=8)

    summary = calc.summary()

    print(f"Total Funções de Dados:         {summary['total_data_functions']} ({summary['data_function_points']} PF)")
    print(f"Total Funções Transacionais:   {summary['total_transactional_functions']} ({summary['transactional_function_points']} PF)")
    print(f"--------------------------------------------------")
    print(f"TAMANHO FUNCIONAL TOTAL:        {summary['total_unadjusted_function_points']} PF")


if __name__ == "__main__":
    main()
