from math import radians
import numpy as np                

arr1= np.array([1, 2, 3, 4])

current_dtype =  arr1.dtype # определение текущего типа данных

arr = np.array([1,2,3], dtype=int) # создание массива от 1 до 3, включительно, с типом данных целых чисел.

arr_float = np.array([1.2, 2.5, 3.8, 4.1])
arr_int = arr_float.astype(int) # округлите вещественные числа до целых

# Датасет температуры (тип данных: int)
temp_data = np.array([[22, 25, 24, 23, 21],
                      [20, 18, 19, 22, 24]])

# Датасет влажности (тип данных: int)
humid_data = np.array([[45, 50, 48, 52, 47],
                       [45, 48, 50, 51, 53]])

def change_data_type(dataset ,  new_dtype):  # добавь два аргумента для функции согласно условию
    return  dataset.astype(new_dtype)

temp_data = change_data_type(temp_data, float) # измени с помощью функции change_data_type тип данных temp_data на float
humid_data =  change_data_type(humid_data, float)# измени с помощью функции change_data_type тип данных humid_data на float