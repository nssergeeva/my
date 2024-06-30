from math import inf

def divide(first, second):
    if second == 0:
        return 'Ошибка'
    else:
        return first/second


res1 = divide(22, 0)
res2 = divide(4,1)
print(res1)
print(res2)