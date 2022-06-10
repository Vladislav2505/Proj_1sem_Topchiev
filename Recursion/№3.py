# Вычисление суммы чисел с поддержкой вложенных списков

def Foo(arr, q=0):
    if q >= len(arr):
        return 0
    if type(arr[q]) == list:
        arr[q] = sum(arr[q])
    return arr[q] + Foo(arr, q + 1)


lis = [2, 3, 4, [2, 3]]

summ = Foo(lis)

print(summ)
