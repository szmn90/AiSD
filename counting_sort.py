def counting_sort(arr):
    n = len(arr)
    res = [0] * n

    maks_num = -1
    for i in range(len(arr)):
        if arr[i] > maks_num:
            maks_num = arr[i]
    c = [0] * (maks_num + 1)

    for i in range(n):
        c[arr[i]] += 1

    for i in range(1, maks_num + 1):
        c[i] += c[i-1]

    for i in range(n - 1, -1, -1):
        res[c[arr[i]] - 1] = arr[i]
        c[arr[i]] -= 1

    return res
