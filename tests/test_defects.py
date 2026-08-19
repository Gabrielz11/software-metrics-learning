import pytest

from software_metrics.defects import (
    calculate_defect_density,
    calculate_defect_removal_efficiency,
)


def test_calculate_defect_density():
    assert calculate_defect_density(40, 10) == 4.0
    assert calculate_defect_density(0, 100) == 0.0


def test_calculate_defect_density_exceptions():
    with pytest.raises(ValueError):
        calculate_defect_density(-1, 10)

    with pytest.raises(ValueError):
        calculate_defect_density(40, 0)

    with pytest.raises(TypeError):
        calculate_defect_density("40", 10)  # type: ignore


def test_calculate_defect_removal_efficiency():
    assert calculate_defect_removal_efficiency(90, 10) == 90.0
    assert calculate_defect_removal_efficiency(0, 0) == 100.0


def test_calculate_defect_removal_efficiency_exceptions():
    with pytest.raises(ValueError):
        calculate_defect_removal_efficiency(-5, 10)

    with pytest.raises(TypeError):
        calculate_defect_removal_efficiency(10, "5")  # type: ignore
