# Вычислить сумму элементов набора чисел.

def Foo(arr, q=0):
    if q >= len(arr):
        return 0
    return arr[q] + Foo(arr, q + 1)


lis = [1, 32, 3]

result = Foo(lis)
print(result)
