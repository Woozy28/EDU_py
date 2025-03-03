import numpy as np
arr = np.array([-1, 2, -3, 4, -5])

modified_arr =  np.where(arr<0,0,arr)# замените все отрицательные значения в массиве на 0

print("Исходный массив:")
print(arr)
print("Модифицированный массив:")
print(modified_arr)