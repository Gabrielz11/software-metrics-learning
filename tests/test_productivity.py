import pytest

from software_metrics.productivity import (
    calculate_effort_per_unit,
    calculate_productivity,
)


def test_calculate_productivity():
    assert calculate_productivity(10000, 500) == 20.0
    assert calculate_productivity(200, 1000) == 0.2


def test_calculate_productivity_exceptions():
    with pytest.raises(ValueError):
        calculate_productivity(-10, 500)

    with pytest.raises(ValueError):
        calculate_productivity(100, 0)

    with pytest.raises(TypeError):
        calculate_productivity("100", 50)  # type: ignore


def test_calculate_effort_per_unit():
    assert calculate_effort_per_unit(200, 1000) == 5.0


def test_calculate_effort_per_unit_exceptions():
    with pytest.raises(ValueError):
        calculate_effort_per_unit(0, 100)

    with pytest.raises(ValueError):
        calculate_effort_per_unit(100, -5)

    with pytest.raises(TypeError):
        calculate_effort_per_unit(100, "50")  # type: ignore
