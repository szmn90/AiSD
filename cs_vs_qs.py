import sys
sys.setrecursionlimit(10**6)
import random
import copy
import time
import matplotlib.pyplot as plt
import pandas as pd
from qs_skrajny import qs_skrajny as qs_skrajny
from qs_srodek import qs_srodek as qs_srodek
from counting_sort import counting_sort as counting_sort

def generate_data():
    algorithms = {'QS (skrajny jako pivot)': qs_skrajny,
                  'CS': counting_sort}
    
    data = []
    for n in [10000, 25000, 35000, 50000, 70000, 80000, 100000, 130000, 160000, 200000]:
        arr = [random.randint(1, 0.01*n) for i in range(n)]
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
    df.to_csv('cs_vs_qs_001n.csv', sep=';', index=False)

    wykres = ['QS (skrajny jako pivot)', 'CS']
    for name in wykres:
        plt.plot(df['n'], df[name], label=name)
    plt.xlabel('Ilość elementów do posortowania')
    plt.ylabel('Czas sortowania [s]')
    plt.legend()
    plt.show()

generate_data()
