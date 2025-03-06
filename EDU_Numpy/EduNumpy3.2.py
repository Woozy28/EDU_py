import numpy as np

arr = np.array([2, 4, 6, 8, 10])

result =  np.sum(arr)# сумма
result2 =  np.mean(arr)# среднее значение

value1 =  np.min(arr)# минимальное значение
value2 =  np.max(arr)# максимальное значение

result1 =  np.std(arr)# стандартное отклонение
result2 =  np.var(arr)# дисперсия

result1 =  np.argmin(arr)# индекс минимального значения 
result2 =  np.argmax(arr)# индекс максимального значения 


result1 = np.cumsum(arr) # кумулятивная сумма
result2 =  np.cumprod(arr)# кумулятивное произведение

stock_prices = np.array([50, 55, 60, 52, 48, 65, 70])
days = np.array(['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'])

daily_returns =  np.diff(stock_prices)# Изменения цен за день
best_day =  days[np.argmax(daily_returns)+1]# День с максимальным приростом
worst_day =  days[np.argmin(daily_returns)+1]# День с минимальным приростом


temperature_data = np.array([20, 22, 25, 18, 30, 28, 35, 22, 15, 10, 5, 12])

temperature_range =  np.ptp(temperature_data)# Размах температур (максимальная - минимальная)
coldest_day =  np.argmin(temperature_data)# Индекс самого холодного дня
hottest_day =  np.argmax(temperature_data)# Индекс самого теплого дня

# Заданные данные (доходы инвесторов в тысячах долларов)
income_data = np.array([40, 55, 60, 75, 80, 85, 90, 100, 120, 150])

median_income =  np.median(income_data)# Медиана доходов

above_median =  income_data[np.where(income_data>median_income)]# Инвесторы, заработавшие выше медианы
below_median =  income_data[np.where(income_data<median_income)]# Инвесторы, заработавшие ниже медианы

income_range_above_median =  np.ptp(above_median)# Разброс доходов для инвесторов, заработавших выше медианы


#________________________________________________________________________________________________________________________________________________________
# Цены акций для 3 компаний(каждый столбец - отдельная компания)
stock_prices = np.array([
    [110, 112, 108],
    [115, 118, 120],
    [108, 110, 105],
    [122, 121, 124],
    [128, 130, 125],
    [133, 132, 134],
    [129, 127, 130]
])

average_prices =  np.round(np.mean(stock_prices,axis=0),2)# Средняя стоимость акций каждой компании за все дни (ответ округлите до 2-х знаков после запятой)

volatility =  np.ptp(stock_prices,axis=0)# Размах цен для каждой компании
most_volatile_company = np.argmax(volatility) # Индекс компании(столбца) с максимальной волатильностью (наибольшим размахом цен)

total_daily_change = np.diff(stock_prices,axis=0) # Общее изменение в цене акций 3-х компаний за каждый день
day_with_max_change =  np.argmax(np.sum(total_daily_change, axis=0),axis=0)+1# Индекс дня(строки) с наибольшим общим изменением в стоимости акций всех компаний.

###_______________________________________________________________________________________________________________________________________________________

# Заданные данные (1-й столбец: возраст, 2-й столбец: уровень холестерина, 3-й столбец: давление)
medical_data = np.array([
    [30, 200, 120],
    [45, 220, 130],
    [35, 190, 110]
])

average_age = np.round(np.mean(medical_data[:,0]),1) # Средний возраст пациентов (ответ округлите до 1 знака после запятой)
max_cholesterol_patient = medical_data[np.argmax(medical_data[:,1]),:] # Индекс пациента с самым высоким уровнем холестерина
min_pressure_patient =  medical_data[np.argmin(medical_data[:,2]),:]# Индекс пациента с самым низким давлением



###_____________________________________________________________________________________________________________________________________________________________

student_scores = np.array([
    [5, 4, 3],  # Оценки первого студента за три задачи
    [3, 2, 4],  # Оценки второго студента за три задачи
    [5, 5, 3]   # Оценки третьего студента за три задачи
])

average_scores =  np.round(np.mean(student_scores,axis=0),1)# Средний балл за каждую задачу (округлите до 1 знака после запятой)
highest_avg_student =  np.argmax(np.mean(student_scores,axis=1))# Индекс студента с наивысшим средним баллом.
min_variability_task =  np.argmin(np.var(student_scores,axis=0))# Индекс задачи с наименьшей дисперсией баллов.

###___________________________________________________________________________________________________________________________________________________________

def most_frequent_number(arr):
    bin_counts =  np.bincount(arr)# подсчет встреченных элементов
    most_frequent_index =  np.argmax(bin_counts)# найдите индекс максимального значения встреченных элементов 
    occurrences =  bin_counts[most_frequent_index]# получите количество вхождений наиболее часто встречающегося числа
    return most_frequent_index, occurrences

arr = np.array([1, 2, 3, 1, 2, 1, 4, 5, 4, 3, 3])
result_number, result_occurrences = most_frequent_number(arr)

print(f"Наиболее часто встречающееся число: {result_number}")
print(f"Количество вхождений: {result_occurrences}")