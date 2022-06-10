# Возведение числа x в степень y.

def Foo(a, b):
    if b == 2:
        return a ** 2
    return a * Foo(a, b - 1)


x = 5
y = 2

result = Foo(x, y)
print(result)