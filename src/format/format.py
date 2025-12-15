def back(a, b):
    # если a >= b будет True иначе False
    for i in range(min(len(a), len(b))):
        if a[i] > b[i]:
            return False
        elif a[i] <= b[i]:
            return True
    # если a длинее или равна b то True иначе False
    if len(a) >= len(b):
        return True
    elif len(a) < len(b):
        return False


a = input("Введите строку a")
b = input("Введите строку b")
print(back(a, b))
