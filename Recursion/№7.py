# Определение максимального элемента списка.

def Foo(arr, a, b=0):
    if b >= len(arr):
        return a
    elif arr[b] > a:
        a = arr[b]
        return Foo(arr, a, b + 1)
    else:
        return Foo(arr, a, b + 1)


lis = [12, 3, 4, 44]
result = lis[0]
result = Foo(lis, result)

print(result)