# put your python code here
# put your python code here
import numpy as np

def check_array(arr):
    has_positive =  np.any(arr > 0)# проверка, есть ли хотя бы одно положительное число в массиве
    all_negative =  np.all(arr < 0)# проверка, все ли элементы массива отрицательны

    return  has_positive, all_negative# функция должна возвращать два булева значения 

array2 = np.array([-2, -4, -6, 8, -1])
result =  check_array(array2)# проверь массив array2 с помощью функции check_array

#print(f"В массиве есть хотя бы одно положительное число: {result[0]}")
#print(f"Все элементы массива отрицательны: {result[1]}")

sales_data_array = np.array([[1, 10, 100],
                             [2, 5, 50],
                             [3, 0, 0],
                             [4, 8, 80]])

def analyze_sales_data(sales_data):
    zero_sales = 0
    non_positiv_income = 0

    has_zero_sales =  False# проверка, есть ли хотя бы одна запись с нулевыми продажами
    all_positive_income =  False# проверка, все ли товары имеют положительный доход от продаж
    for i in sales_data:
        if i[1] == 0:
            zero_sales +=1 
        if i[2] <=0:
            non_positiv_income +=1
    
    if zero_sales !=0: has_zero_sales = True
    if non_positiv_income !=0: all_positive_income = False


    return  has_zero_sales, all_positive_income# функция должна возвращать два булева значения 


result =  analyze_sales_data(sales_data_array)# проверь массив sales_data_array с помощью функции analyze_sales_data

print(f"Есть ли товары с нулевыми продажами: {result[0]}")  # первое булево значение согласно условию
print(f"Все ли товары имеют положительный доход: {result[1]}")  # второе булево значение согласно условию

def true_np_analyze_data(data):
    return np.any(data[:,1]==0), np.all(data[:,2]<=0)

print(true_np_analyze_data(sales_data_array))


#Дан массив data размером 5 x 5, заполненный случайными целыми числами от 0 до 9. Замените все четные 
#числа в массиве на 0, а все нечетные на 1. Используйте булеву индексацию для создания масок, которые соответствуют этим условиям, и примените их к массиву data.  

data = np.array([[6, 4, 8, 7, 9],
                 [0, 0, 1, 7, 2],
                 [5, 7, 9, 0, 4],
                 [5, 1, 2, 8, 6],
                 [9, 8, 3, 0, 3]])

#even_mask =  # создаем маску, которая соответствует четным числам
#odd_mask =  # создаем маску, которая соответствует нечетным числам

data[data%2 !=0] = 1
data[data%2 ==0] = 0 

  # Заменяем четные числа на 0
  # Заменяем нечетные числа на 1

print(data)

data8 = np.array([[8, 3, 9, 1, 9, 0],
                 [5, 4, 2, 7, 4, 2],
                 [0, 8, 7, 4, 3, 9],
                 [0, 9, 7, 1, 0, 1],
                 [7, 1, 0, 3, 9, 3],
                 [5, 8, 0, 4, 0, 6]])

#mask =  # Создаем маску, которая соответствует элементам на главной диагонали

mean =  np.mean(np.diag(data8))# Применяем маску к массиву и вычисляем среднее арифметическое 

print(f'Среднее арифметическое элементов на диагоналях: {mean:.2f}')

studydata = np.array([
    ['Анна', 19, 'F', 1, 4.5],
    ['Борис', 21, 'M', 2, 3.7],
    ['Вера', 21, 'F', 3, 4.8],
    ['Глеб', 22, 'M', 4, 3.9],
    ['Дарья', 18, 'F', 1, 4.2],
    ['Егор', 23, 'M', 3, 4.1],
    ['Жанна', 21, 'F', 2, 4.6],
    ['Захар', 19, 'M', 1, 4.0]
])

mask =  (studydata[:,2] == "F") & (studydata[:,3] == "3")  # создаем маску, которая соответствует всем условиям задачи

result = studydata[mask]  # применяем маску к датафрейму 

print(result)