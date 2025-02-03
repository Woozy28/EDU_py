from math import radians
import numpy as np                # installed with matplotlib

array1 = np.arange(0,5) # cоздайте одномерный массив из 5 целых чисел от 0 до 4
array2 = np.zeros((4,5)) # cоздайте двумерный массив размером 4x5, заполненный нулями
array3 = np.ones((3,2)) # cоздайте массив размером 3x2, заполненный единицами
array4 = np.arange(0,9,2)  # cоздайте одномерный массив из четных чисел от 0 до 8
array5 = np.linspace(0, 1, 5) # cоздайте массив из 5 равномерно распределенных значений между 0 и 1
array6 = np.full((2,3),7) # cоздайте массив размером 2x3, заполненного значением 7

array = np.full((5,2), True)
print(array)