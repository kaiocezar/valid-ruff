import pytest

from src.calculadora import Calculadora


def test_soma():
    calc = Calculadora()
    assert calc.soma(2, 2) == 4


def test_subtracao():
    calc = Calculadora()
    assert calc.subtracao(4, 2) == 2


def test_multiplicacao():
    calc = Calculadora()
    assert calc.multiplicacao(3, 3) == 9


def test_divisao():
    calc = Calculadora()
    assert calc.divisao(6, 2) == 3


def test_divisao_por_zero():
    calc = Calculadora()
    with pytest.raises(ValueError):
        calc.divisao(6, 0) 