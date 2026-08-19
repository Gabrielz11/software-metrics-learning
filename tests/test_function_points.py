import pytest

from software_metrics.function_points import (
    Complexity,
    DataFunctionType,
    FunctionPointCalculator,
    TransactionType,
    get_data_function_complexity,
    get_ee_complexity,
    get_se_ce_complexity,
)


def test_get_data_function_complexity():
    assert get_data_function_complexity(1, 10) == Complexity.LOW
    assert get_data_function_complexity(1, 60) == Complexity.AVERAGE
    assert get_data_function_complexity(3, 10) == Complexity.LOW
    assert get_data_function_complexity(3, 30) == Complexity.AVERAGE
    assert get_data_function_complexity(3, 60) == Complexity.HIGH
    assert get_data_function_complexity(7, 10) == Complexity.AVERAGE
    assert get_data_function_complexity(7, 30) == Complexity.HIGH


def test_get_data_function_complexity_invalid():
    with pytest.raises(ValueError):
        get_data_function_complexity(0, 10)


def test_get_ee_complexity():
    assert get_ee_complexity(1, 10) == Complexity.LOW
    assert get_ee_complexity(1, 20) == Complexity.AVERAGE
    assert get_ee_complexity(2, 2) == Complexity.LOW
    assert get_ee_complexity(2, 10) == Complexity.AVERAGE
    assert get_ee_complexity(2, 20) == Complexity.HIGH
    assert get_ee_complexity(4, 2) == Complexity.AVERAGE
    assert get_ee_complexity(4, 10) == Complexity.HIGH


def test_get_ee_complexity_invalid():
    with pytest.raises(ValueError):
        get_ee_complexity(-1, 5)


def test_get_se_ce_complexity():
    assert get_se_ce_complexity(1, 10) == Complexity.LOW
    assert get_se_ce_complexity(1, 25) == Complexity.AVERAGE
    assert get_se_ce_complexity(3, 3) == Complexity.LOW
    assert get_se_ce_complexity(3, 10) == Complexity.AVERAGE
    assert get_se_ce_complexity(3, 25) == Complexity.HIGH
    assert get_se_ce_complexity(5, 3) == Complexity.AVERAGE
    assert get_se_ce_complexity(5, 10) == Complexity.HIGH


def test_get_se_ce_complexity_invalid():
    with pytest.raises(ValueError):
        get_se_ce_complexity(1, 0)


def test_function_point_calculator_library_example():
    calc = FunctionPointCalculator()
    # Adicionando ALI
    df1 = calc.add_data_function("Livro", DataFunctionType.ALI, ret=1, det=5)
    assert df1.complexity == Complexity.LOW
    assert df1.unadjusted_points == 7

    # Adicionando EE
    tf1 = calc.add_transactional_function("Cadastrar Livro", TransactionType.EE, ftr=1, det=5)
    assert tf1.complexity == Complexity.LOW
    assert tf1.unadjusted_points == 3

    assert calc.calculate_total_unadjusted_points() == 10
    summary = calc.summary()
    assert summary["total_data_functions"] == 1
    assert summary["total_transactional_functions"] == 1
    assert summary["total_unadjusted_function_points"] == 10
