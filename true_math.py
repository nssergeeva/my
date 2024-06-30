import math


def divide(first, second):
    if second == 0:
        return math.inf
    else:
        return first / second


res1 = divide(12, 6)
print(res1)
res2 = divide(2, 0)
print(res2)