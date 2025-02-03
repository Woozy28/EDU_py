from math import radians
import numpy as np                

arr1 = np.array([[1, 2, 3]])
arr2 = np.array([[3, 2, 1]])

result_add = arr1 + arr2 # сложение двух массивов
result_multiply = arr1 * arr2 # поэлементное умножение двух массивов
result_subtract =  arr1 - arr2 # поэлементное вычитание
result_double =  arr1**2 # возведение массива в квадрат  
result_divide =  arr1 / 2# поэлементное деление 

grades = np.array([75, 45, 60, 90, 30, 85, 40])

grades =  grades.astype(float)# преобразование типа данных на float

for i in range (len(grades)):
    if grades[i] > 50:
        grades[i] = (grades[i]*0.1) + grades[i]

  # увеличте оценки более 50 на 10%

print(grades)