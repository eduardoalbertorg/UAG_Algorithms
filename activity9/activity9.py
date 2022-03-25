"""
Usa programación dinámica para resolver el siguiente problema de la mochila.
Suponga una capacidad máxima de 140 unidades.
¿Cuál es el valor óptimo de la mochila?,
¿Cuáles son los objetos que debemos tomar? 

	    1	2	3	4	5	6	7	8	9	10
Valor	79	32	47	18	26	85	33	40	45	59
Peso	85	26	48	21	22	95	43	45	55	52

"""

import numpy as np


object_dict = { 
    0:{"value":79, "weight":85},
    1:{"value":32, "weight":26},
    2:{"value":47, "weight":48},
    3:{"value":18, "weight":21},
    4:{"value":26, "weight":22},
    5:{"value":85, "weight":95},
    6:{"value":33, "weight":43},
    7:{"value":40, "weight":45},
    8:{"value":45, "weight":55},
    9:{"value":59, "weight":52}
    }
"""
object_dict = { 
    0:{"value":3000, "weight":4},
    1:{"value":2000, "weight":3},
    2:{"value":1500, "weight":1}
    }
"""
number_of_values = len(object_dict)
item_values_list = range(number_of_values + 1)
max_weight = 140
weights_list = range(max_weight + 1)
cells = [[0 for w in weights_list] for i in item_values_list]

for i in item_values_list:
    for w in weights_list:
        if i == 0 or w == 0:
            cells[i][w] = 0
        elif object_dict[i-1]["weight"] <= w:
            current_item_value = object_dict[i-1]["value"]
            current_item_weight = object_dict[i-1]["weight"]
            cells[i][w] = max(cells[i-1][w], current_item_value + cells[i-1][w-current_item_weight])
        else:
            cells[i][w] = cells[i-1][w]

most_value = cells[number_of_values][max_weight]

print(np.matrix(cells))
print('Most optimal value stolen:', most_value)

remaining_weight = max_weight
for i in range(number_of_values, 0, -1):
    if most_value <= 0:
        break
    if most_value == cells[i - 1][remaining_weight]:
        continue
    else:
        print('Item included: ', list(object_dict.keys())[i - 1])
        most_value = most_value - object_dict[i - 1]["value"]
        remaining_weight = remaining_weight - object_dict[i - 1]["weight"]


