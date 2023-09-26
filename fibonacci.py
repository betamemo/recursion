def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return fibonacci(n - 1) + fibonacci(n - 2)


month = 2
mate = fibonacci(month)
new = fibonacci(month - 1)

print('month #', month, ':', mate, 'mate,', new, 'new')
