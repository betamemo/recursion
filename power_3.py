# Check if a number is power by 3

def power_3(n):
    if n == 0:
        return False
    elif n == 1:
        return True
    elif n > 0:
        return is_power(n // 3)


print(is_power(60))
print(is_power(27))
