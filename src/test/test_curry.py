from ..curry.curry import curry
from ..curry.curry import uncurry
from ..curry.curry import summ


def test1():
    sum_curry = curry(summ, 10)
    sum_uncurry = uncurry(sum_curry, 10)
    assert sum_curry(1)(2)(3)(4)(5)(6)(7)(8)(9)(10) == 55
    assert sum_uncurry(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 55


def test2():
    sum_curry = curry(summ, 6)
    sum_uncurry = uncurry(sum_curry, 6)
    assert sum_curry(1)(2)(3)(4)(5)(-6) == 9
    assert sum_uncurry(1, 2, 3, 4, 5, -6) == 9


def test3():
    sum_curry = curry(summ, 5)
    sum_uncurry = uncurry(sum_curry, 5)
    try:
        assert sum_curry(1)(2)(3)(4)(5)(-6)
    except Exception:
        assert 1 == 1
    assert sum_uncurry(1, 2, 3, 4, 5, -6) is not int