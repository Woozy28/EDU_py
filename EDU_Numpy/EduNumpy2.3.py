import numpy as np

a = np.array([1, 2, 3])
b = np.array([2, 2, 2])

result =  np.greater(a,b)# булев массив, который показывает, в каких местах первый массив содержит большие значения, чем второй
result =  np.greater_equal(a,b)# булев массив, который показывает, где первый массив содержит значения, большие или равные соответствующим значениям второго
result = np.not_equal(a,b) # булев массив, показывающий, где соответствующие элементы не равны
result =  np.not_equal(a,3)# все элементы массива, которые не равны числу 3
exactly_one_event = np.not_equal(a,b)  # булев массив со значениями в каких случаях произошло ровно одно из событий.

classification1 = np.array([[1, 0, 1], 
                            [0, 1, 0]])
classification2 = np.array([[1, 0, 0], 
                            [0, 1, 1]])

result =  np.equal(classification1,classification2).astype(int)# массив где каждый элемент равен 1, если classification1 и classification2 совпадают, и 0 в противном случае

secret_codes = np.array([15, 23, 7, 42, 18, 10, 7, 29])
provided_codes = np.array([23, 7, 18, 7])

#some_data = np.isin(secret_codes, provided_codes)
#missing_codes =  secret_codes[some_data] # определить отсутствующие коды

result =[]

for i in secret_codes:
    if np.isin(i,provided_codes):
        continue
    else:
        result.append(i)

some_array = np.array(result)



celsius_temps = np.array([25, 32, 28, 35, 30]) 
days = np.array(['понедельник', 'вторник', 'среда', 'четверг', 'пятница']) 

fahrenheit_temps =  celsius_temps * 9 / 5 + 32 # температура в Фаренгейтах

hot_days_fahrenheit_temps = days[np.greater(fahrenheit_temps, 90)]  # дни когда температура в Фаренгейтах была выше 90
hot_days_celsius_temps =  days[np.greater_equal(celsius_temps, 30)]# дни когда температура в Цельсиях не ниже 30

numbers = np.array([5, 12, 15, 20, 25, 30, 35])

condition1 =  np.logical_and(numbers>10, numbers<=30)
condition2 =  numbers != 15

filtered_numbers =  numbers[np.logical_and(condition1,condition2)]# определите, какие числа удовлетворяют заданным критериям

numbers = np.array([2, 5, 8, 12, 15, 20, 23])

even_numbers =  numbers[numbers%2==0]# выведите четные числа в массиве

print(f'Четные числа: {even_numbers}')