# put your python code here
import numpy as np

arr3 = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15]])

transposed_arr =  arr3.transpose()

print("Транспонированный массив:")
print(transposed_arr)

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6],
                 [7, 8]])

result =  np.dot(arr1,arr2)# умножьте матрицы

print("Результат умножения:")
print(result)

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12]])

reshaped_arr =  arr.reshape((2,6))# измените форму массива на (2, 6)

print("Массив после изменения формы:")
print(reshaped_arr)

data = np.array([[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10]])

data_new = data.transpose() # перестановка осей

print("Изначальные данные:")
print(data)
print("Данные после перестановки:")
print(data_new)

import numpy as np

arr2_8 =  np.arange(16).reshape(2, 8) #Создайте массив размером 2x8, заполненный значениями от 0 до 15.

print("Массив:")
print(arr)

# put your python code here
import numpy as np

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6],
                 [7, 8]])

result =  arr1 @ arr2# умножьте две матрицы затем транспонируйте результат

transposed_result =  result.transpose()# транспонируйте результат

print("Транспонированный результат умножения:")
print(transposed_result)

A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

A =  A[:2,0:2].transpose()# транспонирование верхнего левого квадранта матрицы A
print("угол")
print(A)