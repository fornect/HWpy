def curry(func, n):
    def curried_func(*args):
        if n < 0:
            return
        elif len(args) == n:
            return func(*args)
        else:
            return lambda *args2: curried_func(*(args + args2))
    return curried_func

def uncurry(func_curry, n):
        return lambda *args: func_curry(*args)

def summ(*args):
    return sum(args)

num_el = 5
sum_curry = curry(summ, num_el)
sum_uncurry = uncurry(sum_curry, num_el)
try:
    result = sum_curry(1)(2)(3)(4)(5)(6)(7)(8)(9)(10)
except Exception:
    print("неверное количество переменных")
else:
    while type(result) is not int:
        result = result(0)
    print(result)
ar = (1, 2, 3, 4, 5, 6)
if len(ar) > num_el:
    print("неверное количество переменных")
else:
    while len(ar) != num_el:
        ar += (0,)
    result2 = sum_uncurry(*ar)
    print(result2)