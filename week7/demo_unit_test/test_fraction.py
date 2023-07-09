from fraction import Fraction

def test_constructor():
    f = Fraction(1, 2)
    assert f.numerator == 1
    assert f.denominator == 2

def test_str_01():
    f = Fraction(1, 2)
    assert str(f) == "1/2"

def test_str_02():
    f = Fraction(-1, 2)
    assert str(f) == "-1/2"

def test_str_03():
    f = Fraction(1, -2)
    assert str(f) == "-1/2"

def test_str_04():
    f = Fraction(-1, -2)
    assert str(f) == "1/2"