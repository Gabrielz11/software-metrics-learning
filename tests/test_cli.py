import sys

import pytest

from software_metrics.cli import main


def test_cli_productivity(capsys, monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["software-metrics", "productivity", "--size", "10000", "--effort", "500"],
    )
    main()
    captured = capsys.readouterr()
    assert "Produtividade: 20.00 unidades/hora" in captured.out


def test_cli_defects(capsys, monkeypatch):
    monkeypatch.setattr(
        sys, "argv", ["software-metrics", "defects", "--defects", "40", "--size", "10"]
    )
    main()
    captured = capsys.readouterr()
    assert "Densidade de defeitos: 4.00 defeitos/unidade" in captured.out


def test_cli_kloc(capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["software-metrics", "kloc", "--loc", "2500"])
    main()
    captured = capsys.readouterr()
    assert "KLOC: 2.500" in captured.out


def test_cli_error_handling(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["software-metrics", "productivity", "--size", "100", "--effort", "0"],
    )
    with pytest.raises(SystemExit):
        main()
