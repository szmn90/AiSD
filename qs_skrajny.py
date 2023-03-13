def qs_skrajny(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    less_than_pivot = []
    greater_than_pivot = []
    for i in arr[1:]:
        if i <= pivot:
            less_than_pivot.append(i)
        else:
            greater_than_pivot.append(i)
    
    return qs_skrajny(less_than_pivot) + [pivot] + qs_skrajny(greater_than_pivot)
