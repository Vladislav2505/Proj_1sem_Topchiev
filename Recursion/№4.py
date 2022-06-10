# Возврат ряда Фибоначчи.

def Foo(num, a=1, b=1):
    if num <= 1:
        return [a]
    return [a] + Foo(num - 1, a=b, b=b+a)


print(Foo(6))
