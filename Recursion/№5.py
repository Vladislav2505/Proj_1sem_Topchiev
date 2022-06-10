# Реверсирование числа.

def Foo(a, c=0):
    if a <= 0:
        return c
    else:
        b = a % 10
        c = (c * 10) + b
        a = a // 10
        return Foo(a, c)


number = 15567

result = Foo(number)
print(result)
