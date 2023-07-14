import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src.algo.greedy import *
from src.algo.RLF import *
from src.generator import *
import random
import json

import numpy as np
import matplotlib.pyplot as plt

#make statistic for all algorithms and write data to json
def make_statistic(n):
    # name, algo
    algorhitms = [("greedy",greedy_coloring), ("sorting greedy", sorting_greedy_coloring), ("RLF",RLF)]

    data = {}
    for algorithm in algorhitms:
        data[algorithm[0]] = []
    
    for i in range(n):
        graph = generate_graph(100)
        for algorhitm in algorhitms:
            data[algorhitm[0]].append(algorhitm[1](graph))
            graph.resetColors()
    
    if os.path.exists('statistic.json'):
        old_data = json.load(open('statistic.json'))
        for algorithm in algorhitms:
            data[algorithm[0]] += old_data[algorithm[0]]
    json.dump(data, open('statistic.json', 'w'))


def visualize_statistic(filename): 
    data = json.load(open(filename))
    print("json loaded")
    algorithms = list(data.keys())
    value_arrays = list(data.values())
    average_values = [np.mean(values) for values in value_arrays]
    fig, ax = plt.subplots()

    
    colors = ['khaki', 'purple', 'coral'] 
    bars = ax.bar(range(len(algorithms)), average_values, color=colors)
    
    ax.set_xticks(range(len(algorithms)))
    ax.set_xticklabels(algorithms)
    ax.set_ylabel('Среднее значение')

    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, str(round(average_values[i], 2)),
                ha='center', va='bottom')


    legend_handles = [plt.Rectangle((0, 0), 1, 1, color=colors[i]) for i in range(len(algorithms))]
    ax.legend(legend_handles, algorithms)
    ax.text(0, 1.1, f"Количество значений: {len(value_arrays[0])}",
             transform=ax.transAxes, rotation=0, va='center')
    
    plt.show()