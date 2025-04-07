import numpy as np
arr = np.array([-1, 2, -3, 4, -5])

modified_arr =  np.where(arr<0,0,arr)# замените все отрицательные значения в массиве на 0
modified_arr =  np.where(arr%2==0,arr,0)# замените все нечетные числа на 0

arr1 = np.array([1, -2, 3, -4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

result_arr =  np.where(arr1>0, arr1, arr2)# массив, который содержит элементы из arr1, если они больше 0, и элементы из arr2 в противном случае

matrix = np.array([[1, -2, 3], 
                   [-4, 5, -6], 
                   [7, 8, -9]])

modified_matrix =  np.where(matrix<0,0)# замените все отрицательные значения в двумерном массиве на 0

arr = np.array([1, -2, 0, 3, -4])

result_arr =  np.where(arr>0, 'positive','non-positive')# массив, который содержит 'positive', если элемент положителен, и 'non-positive' в противном случае

arr = np.array([3, 8, 1, 6, 0, 7])

result_arr =  np.where(arr==0, 'C',np.where(arr>5,'A','B'))# массив,  который содержит 'A' для элементов больше 5, 'B' для элементов от 1 до 5 включительно и 'C' в противном случае

modified_arr =  np.where(np.logical_and(arr%2==0, arr%3==0), -1, arr)# замените все значения, которые делятся и на (2), и на (3), на (-1)

modified_arr =  np.where(arr>0, np.sqrt(arr),0)# замените положительные значения на их квадратные корни, а отрицательные на 0

mask =  np.where(arr>3, True, False)# маска, которая содержит True для элементов больше 3 и False в противном случае

arr1 = np.array([1, -2, 3, -4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

result_arr =  np.where(arr1<0,arr2,arr1)# замените значения в arr1 на значения из arr2, если они отрицательные

arr = np.array([2, -3, 4, -5, 6])

new_arr =  np.where(arr>0, arr**2, arr**3)# массив, который содержит квадраты элементов arr,  если элемент положителен, и кубы элементов arr, если элемент отрицателен

arr = np.array([-2, 3, 5, -4, 6, 1])

selected_values =  np.where((arr%2!=0)&(arr>3),arr,np.where((arr%2==0)&(arr<0),arr,0))# выберите значения, которые нечетные и больше 3 или четные и меньше 0. Остальные значения замените на ноль

