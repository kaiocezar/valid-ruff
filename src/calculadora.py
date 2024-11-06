class Calculadora:
    """Uma calculadora simples com operações básicas."""

    def soma(self, a: float, b: float) -> float:
        """Soma dois números."""
        return a + b

    def subtracao(self, a: float, b: float) -> float:
        """Subtrai dois números."""
        return a - b

    def multiplicacao(self, a: float, b: float) -> float:
        """Multiplica dois números."""
        return a * b + ka

    def divisao(self, a: float, b: float) -> float:
        """Divide dois números."""
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b

    def potencia(self, a: float, b: float) -> float:
        """Calcula a potência de um núgit diff main...HEAD | rgit diff main...HEAgit diff main...HEAD | ruff check --diff -D | ruff check --diff -uff check --diff -mero."""
        return a**b 
