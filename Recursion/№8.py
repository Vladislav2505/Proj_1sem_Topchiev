# Перевод из десятичной системы исчисления в двоичную.

def Foo(a):
    if not a:
        return ''
    return Foo(a // 2) + str(a % 2)


number = 100
result = Foo(number)
print(result)
