"""Módulo para análise e contagem de Linhas de Código (LOC/SLOC/KLOC).

Este módulo fornece funções educacionais para medir linhas físicas,
linhas lógicas, linhas de comentário, linhas em branco e conversão para KLOC.
"""

from typing import Dict


def count_code_lines(code: str) -> Dict[str, int]:
    """Analisa um texto de código-fonte e conta estatísticas de linhas.

    Args:
        code: Conteúdo textual do código-fonte.

    Returns:
        Dicionário contendo:
            - total_lines: total físico de linhas
            - blank_lines: quantidade de linhas vazias
            - comment_lines: linhas que contêm apenas comentários (# ou // ou /*)
            - code_lines: linhas com código executável ou declarações
    """
    if not isinstance(code, str):
        raise TypeError("O parâmetro 'code' deve ser uma string.")

    lines = code.splitlines()
    total_lines = len(lines)
    blank_lines = 0
    comment_lines = 0
    code_lines = 0

    in_multiline_comment = False

    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            blank_lines += 1
            continue

        if in_multiline_comment:
            comment_lines += 1
            if "*/" in line:
                in_multiline_comment = False
            continue

        if line.startswith("/*"):
            comment_lines += 1
            if "*/" not in line:
                in_multiline_comment = True
            continue

        if line.startswith("#") or line.startswith("//"):
            comment_lines += 1
            continue

        code_lines += 1

    return {
        "total_lines": total_lines,
        "blank_lines": blank_lines,
        "comment_lines": comment_lines,
        "code_lines": code_lines,
    }


def calculate_kloc(loc: int | float) -> float:
    """Converte a contagem de LOC em KLOC (milhares de linhas de código).

    Args:
        loc: Quantidade total ou lógica de linhas de código.

    Returns:
        Valor equivalente em KLOC.

    Raises:
        ValueError: Se loc for negativo.
        TypeError: Se loc não for numérico.
    """
    if not isinstance(loc, (int, float)):
        raise TypeError("O parâmetro 'loc' deve ser um número (int ou float).")
    if loc < 0:
        raise ValueError("O valor de 'loc' não pode ser negativo.")
    return loc / 1000.0
