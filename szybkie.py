import random
import copy
import time
import matplotlib.pyplot as plt
import pandas as pd
from merge_sort import merge_sort as merge_sort
from qs_srodek import qs_srodek as qs_srodek
from counting_sort import counting_sort as counting_sort
from heap_sort import heap_sort as heap_sort

def generate_data():
    algorithms = {'Merge Sort': merge_sort,
                  'QS (środkowy jako pivot)': qs_srodek,
                  'CS': counting_sort,
                  'Heap Sort': heap_sort}

    data = []
    for n in [10000, 30000, 50000, 100000, 140000, 180000, 250000, 400000, 550000, 650000, 800000, 1000000, 1200000, 1500000]:
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
    df.to_csv('szybkie.csv', sep=';', index=False)

    wykres = ['Merge Sort', 'QS (środkowy jako pivot)', 'CS', 'Heap Sort']
    for name in wykres:
        plt.plot(df['n'], df[name], label=name)
    plt.xlabel('Ilość elementów do posortowania [mln]')
    plt.ylabel('Czas sortowania [s]')
    plt.legend()
    plt.show()

generate_data()
