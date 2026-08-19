"""Exemplo Prático: Cálculo de Métricas de Qualidade e Defeitos no Sistema de Biblioteca.
"""

from software_metrics.defects import (
    calculate_defect_density,
    calculate_defect_removal_efficiency,
)


def main():
    print("=== ESTUDO DE CASO: MÉTRICAS DE QUALIDADE (SISTEMA DE BIBLIOTECA) ===")

    # Dados coletados na Release 1.0 (Sistema com 10 KLOC ou 50 Pontos de Função)
    sloc = 10000
    kloc = 10.0
    pf = 50.0

    defects_pre_release = 35  # Encontrados pelos testes em QA
    defects_post_release = 5  # Reportados pelos usuários nos primeiros 3 meses

    total_defects = defects_pre_release + defects_post_release

    # Cálculo da Densidade de Defeitos
    density_kloc = calculate_defect_density(total_defects, kloc)
    density_pf = calculate_defect_density(total_defects, pf)

    # Eficiência de Remoção de Defeitos (DRE)
    dre = calculate_defect_removal_efficiency(defects_pre_release, defects_post_release)

    print(f"Total de Defeitos Identificados: {total_defects}")
    print(f"  - Pré-Release (QA):            {defects_pre_release}")
    print(f"  - Pós-Release (Produção):     {defects_post_release}")
    print(f"--------------------------------------------------")
    print(f"Densidade (por KLOC):            {density_kloc:.2f} defeitos/KLOC")
    print(f"Densidade (por Ponto de Função): {density_pf:.2f} defeitos/PF")
    print(f"Eficiência de Remoção (DRE):     {dre:.2f}%")


if __name__ == "__main__":
    main()
