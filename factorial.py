# f(n) = n * f(n - 1)
# f(1) = 1
# f(0) = 1


def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)


# f(7) = 7 * 6 * 5 * 4 * 3 * 2 * 1
# f(7) = 7 * (7 - 1) * (7 - 2) * (7 - 3) * (7 - 4) * (7 - 5) * (7 - 6)
print(factorial(1))
