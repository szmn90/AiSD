def qs_srodek(arr):
    if len(arr) <= 1:
        return arr
    
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    less_than_pivot = []
    greater_than_pivot = []
    for i, value in enumerate(arr):
        if i == pivot_index:
            continue
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    
    return qs_srodek(less_than_pivot) + [pivot] + qs_srodek(greater_than_pivot)
