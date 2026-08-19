import pytest

from software_metrics.loc import calculate_kloc, count_code_lines


def test_count_code_lines_basic():
    code = """# Comentário de cabeçalho
def hello():
    print("World") # linha de código

# Outro comentário
"""
    result = count_code_lines(code)
    assert result["total_lines"] == 5
    assert result["blank_lines"] == 1
    assert result["comment_lines"] == 2
    assert result["code_lines"] == 2


def test_count_code_lines_invalid_type():
    with pytest.raises(TypeError):
        count_code_lines(123)  # type: ignore


def test_calculate_kloc():
    assert calculate_kloc(1000) == 1.0
    assert calculate_kloc(2500) == 2.5
    assert calculate_kloc(0) == 0.0


def test_calculate_kloc_invalid():
    with pytest.raises(ValueError):
        calculate_kloc(-10)

    with pytest.raises(TypeError):
        calculate_kloc("1000")  # type: ignore
