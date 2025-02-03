from math import radians
import numpy as np                

arr = np.zeros((3,2,4))# создание трехмерного массива из нулей (каждый массив по две строки и четыре столбца)
dimension = np.ndim(arr) # определение количества измерений 

matrix = np.ones((3,4)) # создание матрицы 3 на 4 заполненную единицами
matrix_shape = np.shape(matrix) # определение размеров матрицы 

idenity_matrix = np.identity(4) # создание квадратной матрицы с единицами на главной диагонали


original_array = np.array([1, 2, 3])
tiled_array1 = np.tile(original_array,(3,1)) # массив с повторенными элементами

tiled_array2 = np.tile(original_array,(4,2)) # повторение массива с дополнительным критерием
tiled_array = np.tile(original_array,(2,4,2)) # повторение массива + сделайте этот массив двумерным

def print_matrix (z,x,y):
    return np.zeros((z,x,y))
