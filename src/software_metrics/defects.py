"""Módulo para cálculo de Métricas de Qualidade e Defeitos.

Fornece funções educacionais para densidade de defeitos, eficiência na remoção
de defeitos e taxa de defeitos escapados.
"""


def calculate_defect_density(defects: int | float, size: float | int) -> float:
    """Calcula a densidade de defeitos de um produto ou componente.

    Fórmula: Densidade de Defeitos = Defeitos / Tamanho

    Args:
        defects: Quantidade total de defeitos identificados (>= 0).
        size: Tamanho do software (ex: KLOC, Pontos de Função, Múltiplos UCP) (> 0).

    Returns:
        Densidade de defeitos por unidade de tamanho.

    Raises:
        TypeError: Se os parâmetros não forem numéricos.
        ValueError: Se defeitos < 0 ou tamanho <= 0.
    """
    if not isinstance(defects, (int, float)) or not isinstance(size, (int, float)):
        raise TypeError("Defeitos e tamanho devem ser numéricos.")
    if defects < 0:
        raise ValueError("A quantidade de defeitos não pode ser negativa.")
    if size <= 0:
        raise ValueError("O tamanho deve ser estritamente maior que zero.")

    return float(defects) / float(size)


def calculate_defect_removal_efficiency(
    pre_release_defects: int | float, post_release_defects: int | float
) -> float:
    """Calcula a Eficiência de Remoção de Defeitos (DRE - Defect Removal Efficiency).

    Fórmula: DRE = (Defeitos Pré-Release / (Defeitos Pré-Release + Defeitos Pós-Release)) * 100

    Args:
        pre_release_defects: Defeitos encontrados e corrigidos antes do lançamento (>= 0).
        post_release_defects: Defeitos encontrados pelos usuários após o lançamento (>= 0).

    Returns:
        Porcentagem de defeitos removidos antes do lançamento (0% a 100%).

    Raises:
        TypeError: Se os parâmetros não forem numéricos.
        ValueError: Se algum parâmetro for negativo ou a soma total de defeitos for 0.
    """
    if not isinstance(pre_release_defects, (int, float)) or not isinstance(
        post_release_defects, (int, float)
    ):
        raise TypeError("Os valores de defeitos devem ser numéricos.")
    if pre_release_defects < 0 or post_release_defects < 0:
        raise ValueError("A quantidade de defeitos não pode ser negativa.")

    total_defects = pre_release_defects + post_release_defects
    if total_defects == 0:
        return 100.0  # Se não houver defeitos, a eficiência é considerada 100%

    return (float(pre_release_defects) / float(total_defects)) * 100.0
