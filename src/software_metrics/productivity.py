"""Módulo para cálculo de Métricas de Produtividade.

Este módulo implementa cálculos educacionais de produtividade e taxa de esforço
alinhados aos conceitos do PRD.
"""


def calculate_productivity(size: float | int, effort: float | int) -> float:
    """Calcula a produtividade como a relação entre tamanho entregue e esforço gasto.

    Fórmula: Produtividade = Tamanho / Esforço

    Args:
        size: Tamanho do software (ex: LOC, KLOC, PF, UCP). Deve ser >= 0.
        effort: Esforço dispendido em horas, pessoas-mês, etc. Deve ser > 0.

    Returns:
        Valor da produtividade (unidades de tamanho por unidade de esforço).

    Raises:
        TypeError: Se os argumentos não forem numéricos.
        ValueError: Se o tamanho for negativo ou o esforço for <= 0.
    """
    if not isinstance(size, (int, float)) or not isinstance(effort, (int, float)):
        raise TypeError("Tamanho e esforço devem ser numéricos (int ou float).")
    if size < 0:
        raise ValueError("O tamanho do software não pode ser negativo.")
    if effort <= 0:
        raise ValueError("O esforço deve ser estritamente maior que zero.")

    return float(size) / float(effort)


def calculate_effort_per_unit(size: float | int, effort: float | int) -> float:
    """Calcula o esforço necessário por unidade de tamanho.

    Fórmula: Esforço por Unidade = Esforço / Tamanho

    Args:
        size: Tamanho do software (ex: LOC, PF, UCP). Deve ser > 0.
        effort: Esforço dispendido. Deve ser >= 0.

    Returns:
        Esforço médio necessário para produzir uma unidade de tamanho.

    Raises:
        TypeError: Se os argumentos não forem numéricos.
        ValueError: Se esforço for negativo ou tamanho for <= 0.
    """
    if not isinstance(size, (int, float)) or not isinstance(effort, (int, float)):
        raise TypeError("Tamanho e esforço devem ser numéricos (int ou float).")
    if effort < 0:
        raise ValueError("O esforço não pode ser negativo.")
    if size <= 0:
        raise ValueError("O tamanho deve ser estritamente maior que zero.")

    return float(effort) / float(size)
