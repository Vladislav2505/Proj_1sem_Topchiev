# Вычислить количество отрицательных чисел в наборе.

def Foo(arr, q=0):
    result = 0

    if q >= len(arr):
        return 0
    elif arr[q] < 0:
        return result + 1 + Foo(arr, q + 1)
    else:
        return Foo(arr, q + 1)


lis = [-5, -4, -34, -4]
res = Foo(lis)

print(res)
