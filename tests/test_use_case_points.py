import pytest

from software_metrics.use_case_points import (
    ActorComplexity,
    UseCaseComplexity,
    UseCasePointCalculator,
)


def test_use_case_points_basic():
    calc = UseCasePointCalculator()
    calc.add_actor("Usuário Humano", ActorComplexity.COMPLEX)  # peso 3
    calc.add_actor("API Externa", ActorComplexity.SIMPLE)  # peso 1

    calc.add_use_case("Manter Acervo", UseCaseComplexity.AVERAGE)  # peso 10
    calc.add_use_case("Realizar Empréstimo", UseCaseComplexity.COMPLEX)  # peso 15

    assert calc.calculate_uaw() == 4
    assert calc.calculate_uucw() == 25
    assert calc.calculate_uucp() == 29

    # Ratings padrão (3 para todos os fatores)
    tcf = calc.calculate_tcf()
    ecf = calc.calculate_ecf()

    assert tcf == pytest.approx(1.02)
    assert ecf == pytest.approx(0.995)

    ucp = calc.calculate_ucp()
    assert ucp > 0

    effort = calc.estimate_effort_hours(20.0)
    assert effort == pytest.approx(ucp * 20.0, 0.01)

    summary = calc.summary()
    assert summary["uaw"] == 4
    assert summary["uucw"] == 25
    assert summary["uucp"] == 29


def test_use_case_points_ratings_validation():
    calc = UseCasePointCalculator()
    with pytest.raises(ValueError):
        calc.set_technical_rating("T99", 3)

    with pytest.raises(ValueError):
        calc.set_technical_rating("T1", 6)

    with pytest.raises(ValueError):
        calc.set_environmental_rating("E99", 3)

    with pytest.raises(ValueError):
        calc.set_environmental_rating("E1", -1)

    with pytest.raises(ValueError):
        calc.estimate_effort_hours(-5)
