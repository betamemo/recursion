# f(n) = f(n-1) * n
# f(1) = 1

def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n


print(factorial(7))
