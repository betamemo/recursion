# max in a list (recursive)
# step 1 tail
# step 2 body


def findmax(arr):
    if len(arr) == 1:
        return arr[0]
    last = arr[-1]
    rest = arr[:len(arr) - 1]
    if last > findmax(rest):
        return last
    else:
        return findmax(rest)


arr = [2, 5, 7, 2, 4, 9, 8]

print(findmax(arr))
