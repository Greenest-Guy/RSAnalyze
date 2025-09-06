from pollards_rho.pollards_rho import PollardsRho
import math


def test_composite_number():
    num = 20701  # 163 * 127
    factor = PollardsRho(num).factorize()

    assert num % factor == 0
    assert factor not in [1, num]


def test_one():
    num = 1
    factor = PollardsRho(num).factorize()

    assert factor == 1
