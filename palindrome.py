# Check if a string is a palindrome


def palindrome(arr):
    if len(arr) == 1:
        return True
    if arr[-1] == arr[0]:
        return palindrome(arr[1:len(arr) - 1])
    else:
        return False


arr = 'abcba'
print(palindrome(arr))
