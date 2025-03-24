import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

sorted_arr =  np.sort(arr)# отсортируйте массив по возрастанию

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])

setdiff_arr =  np.setdiff1d(arr1,arr2)# элементы, которые встречаются только в arr1, но не в arr2.


arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])

setxor_arr =  np.setxor1d(arr1,arr2)# элементы, встречающиеся только в одном из массивов

people = np.array([('John', 28), 
                   ('Sam', 22), 
                   ('Smith', 25), 
                   ('Jones', 30)], 
            dtype=[('name', 'S10'), ('age', int)]) # определение структуры данных для массива,
                                                   # где каждый элемент имеет поле 
                                                   # "name" типа str длиной до
                                                   # 10 символов ('S10') и поле "age" типа int

sorted_people_by_name =  np.sort(people)# cортировка массива по полю 'name' в алфавитном порядке 
sorted_people_by_age = np.sort(people, order='age')# cортировка массива по полю 'age' в порядке возрастания
sorted_people_by_age_desc = sorted_people_by_age[::-1] # cортировка массива по полю 'age' в порядке убывания

arr1 = np.array([1, 2, 'apple', 'orange', 5, 'orange', 'apple', 'orange'])
arr2 = np.array([3, 'apple', 'banana', 6, 7, 1, 'mango'])

unique_arr1 =  np.unique(arr1)# уникальные элементы arr1
unique_arr2 =  np.unique(arr2)# уникальные элементы arr2

intersection =   np.intersect1d(unique_arr1,unique_arr2)# пересечение уникальных элементов arr1 и arr2 

arr = np.array([3, 2, 4, 1, 5, 2, 6, 4, 7])

unique_elements =  np.unique(arr, return_index=True)# массив уникальных элементов + массив индексов их первого вхождения

min_element =  min(arr)# наименьший элемент
max_element =  max(arr)# наибольший элемент


arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])

unique_arr1 =  np.unique(arr1)# находим уникальные элементы в arr1 
unique_arr2 =  np.unique(arr2)# находим уникальные элементы в arr2

union = np.union1d(arr1,arr2)  # находим объединение уникальных элементов обоих массивов с уникальными элементами

in_arr1_mask =  np.isin(union,arr1) # создаем маску - встречается ли каждый элемент из объединения в arr1
in_arr2_mask =  np.isin(union,arr2) # создаем маску - встречается ли каждый элемент из объединения в arr2

common_elements_mask = in_arr1_mask & in_arr2_mask # создаем маску - есть ли каждый элемент из объединения и в arr1, и в arr2
common_elements = union[common_elements_mask] # фильтруем объединение, с маской, чтобы получить только общие элементы

arr = np.array([3, 2, 4, 1, 5, 2, 6, 4, 7])
threshold = 4  # порог для удаления элементов

unique_elements =  np.unique(arr)# нахождение уникальных элементов массива
indices_to_remove = np.where(unique_elements <= threshold) # нахождение индексов элементов, превышающих порог
filtered_arr =  unique_elements[indices_to_remove]# удаление элементов массива arr, превышающих порог

arr = np.array([3, 2, 4, 1, 5, 2, 6, 4, 7])

unique_elements, counts =  np.unique(arr, return_counts=True)# нахождение уникальных обьектов и кол-во их появлений 
elements_to_remove =  unique_elements[counts==1]# создание массива со значениями для удаления 
mask = np.isin(arr,elements_to_remove)
filtered_arr = arr[mask]# возвращение значений которые есть в arr, но нет в elements_to_remove, т.е. удаление нужных нам значений  

print("Исходный массив:", arr)
print("Массив после удаления элементов, встречающихся более одного раза:", filtered_arr)