import random
import copy
import time
import matplotlib.pyplot as plt
import pandas as pd
from bubble_sort import bubble_sort as bubble_sort
from insertion_sort import insertion_sort as insertion_sort
from selection_sort import selection_sort as selection_sort

def generate_data():
    algorithms = {'Bubble Sort': bubble_sort,
                  'Insertion Sort': insertion_sort,
                  'Selection Sort': selection_sort}

    data = []
    for n in [1000, 2500, 5000, 7500, 10000, 15000, 20000, 25000, 30000, 35000]:
        arr = [random.randint(1, n) for i in range(n)]
        row = {'n': n}
        for name, sort_func in algorithms.items():
            arr_copy = copy.deepcopy(arr)
            t_start = time.perf_counter()
            sort_func(arr_copy)
            t_end = time.perf_counter()
            t_elapsed = t_end - t_start
            row[name] = t_elapsed
        data.append(row)

    df = pd.DataFrame(data)
    df.to_csv('sorting_results.csv', sep=';', index=False)

    for name in algorithms.keys():
        plt.plot(df['n'], df[name], label=name)
    plt.xlabel('Ilość elementów do posortowania')
    plt.ylabel('Czas sortowania [s]')
    plt.legend()
    plt.show()

generate_data()
