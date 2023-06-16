def printNTimes(i, n):
    if (n == i):
        return
    else:
        print("Shank", str(n))
        n = n-1
        printNTimes(i, n)


i = 0
n = 6
# printNTimes(i, n)


# Factorial of n


def FactorialN(n):
    if (n == 0):
        return 1
    else:
        return n * FactorialN(n-1)


# print(FactorialN(n))


# Reversing an array


def ArrayReverse(Array):

    a = 0
    b = len(Array)-1

    while a <= b:
        Array[a], Array[b] = Array[b], Array[a]
        a += 1
        b -= 1
    return Array


# print(ArrayReverse([1, 2, 3, 4, 5, 6]))


Array = [1, 2, 3, 4, 5, 6]
