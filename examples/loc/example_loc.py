"""Exemplo Prático: Cálculo de LOC, KLOC e Produtividade no Sistema de Biblioteca.

Este script demonstra como utilizar o módulo `software_metrics.loc` e `software_metrics.productivity`
para analisar o tamanho do código-fonte do Sistema de Biblioteca.
"""

from software_metrics.loc import count_code_lines, calculate_kloc
from software_metrics.productivity import calculate_productivity, calculate_effort_per_unit

SAMPLE_SOURCE_CODE = """
# Sistema de Biblioteca - Módulo de Empréstimos
import datetime

class EmprestimoService:
    def __init__(self, repositorio_livros, repositorio_usuarios):
        self.repo_livros = repositorio_livros
        self.repo_usuarios = repositorio_usuarios

    def realizar_emprestimo(self, usuario_id: int, livro_id: int):
        # Verifica se o usuário pode pegar empréstimo
        usuario = self.repo_usuarios.buscar_por_id(usuario_id)
        if not usuario or usuario.possui_pendencias:
            raise ValueError("Usuário inválido ou com pendências financeiras.")

        livro = self.repo_livros.buscar_por_id(livro_id)
        if not livro or not livro.disponivel:
            raise ValueError("Livro indisponível para empréstimo.")

        # Efetua o registro do empréstimo
        livro.disponivel = False
        data_devolucao = datetime.date.today() + datetime.timedelta(days=14)
        return {"usuario": usuario.nome, "livro": livro.titulo, "devolucao": data_devolucao}
"""


def main():
    print("=== ESTUDO DE CASO: MEDIÇÃO DE LOC NO SISTEMA DE BIBLIOTECA ===")

    stats = count_code_lines(SAMPLE_SOURCE_CODE)
    print(f"Total de Linhas Físicas: {stats['total_lines']}")
    print(f"Linhas em Branco:       {stats['blank_lines']}")
    print(f"Linhas de Comentário:   {stats['comment_lines']}")
    print(f"Linhas de Código (SLOC): {stats['code_lines']}")

    kloc = calculate_kloc(stats["code_lines"])
    print(f"Tamanho em KLOC:         {kloc:.4f} KLOC")

    # Supondo 10.000 SLOC para o sistema completo e 500 horas de esforço
    total_system_sloc = 10000
    effort_hours = 500
    prod = calculate_productivity(total_system_sloc, effort_hours)
    effort_rate = calculate_effort_per_unit(total_system_sloc, effort_hours)

    print("\n--- Métricas do Sistema Completo ---")
    print(f"Produtividade: {prod:.2f} LOC/hora")
    print(f"Taxa de Esforço: {effort_rate:.4f} horas/LOC ({effort_rate * 1000:.1f} horas/KLOC)")


if __name__ == "__main__":
    main()
