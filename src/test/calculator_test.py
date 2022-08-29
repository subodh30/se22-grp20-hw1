from src.code.calculator import addition, subtraction, division, multiplication, mod, power


def test_addition():
    assert addition(9, 9) == 18


def test_subtraction():
    assert subtraction(9, 9) == 0


def test_multiplication():
    assert multiplication(9, 9) == 81


def test_division():
    assert division(9, 9) == 1


def test_modulus():
    assert mod(9, 9) == 0


def test_power():
    assert power(2, 3) == 8


