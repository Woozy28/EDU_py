import numpy as np

array1 = np.array([10, 15, 8, 20])
array2 = np.array([3, 4, 2, 7])

result =  np.add(array1, array2)# поэлементное сложения массивов 

result =  np.subtract(array1, array2)# поэлементное вычитание массивов 

result =  np.multiply(array1, array2)# поэлементное умножение массивов 

result_divide =  np.divide(array1, array2) # поэлементное деление массивов 

result =  np.power(array1, array2) # возведение каждого элемента  в степень соответствующего элемента 

result_maximum =  np.maximum(array1, array2) # найдите максимальные значения из этих двух массивов поэлементно 

result_mod =  np.mod(array1, array2) # найдите остатки от деления элементов array1 на соответствующие элементы array2

result_copysign =  np.copysign(array1, array2) # скопируйте знаки значений из array2 в значения array1

heights = np.array([720, 1080, 480, 960])
widths = np.array([1280, 1920, 640, 1280])

total_pixels =  np.multiply(heights, widths)# расчитайте общее кол-во пикселей в каждом изображении

download_speeds = np.array([50, 60, 45, 70, 55])
upload_speeds = np.array([30, 40, 25, 50, 35])

max_speeds =  np.maximum(download_speeds, upload_speeds)# расчитайте максимальную скорость
min_speeds =  np.minimum(download_speeds, upload_speeds)# расчитайте минимальную скорость


prices = np.array([25.50, 12.75, 18.90, 30.25, 15.60])
vat_rate = 0.20

prices_with_vat =  np.add(prices, np.multiply(prices, vat_rate))# рассчитайте стоимость товаров с НДС

annual_income = np.array([15, 20, 25, 18, 22])
tax_rate = 0.20

taxes =  annual_income * tax_rate# посчитайте налог на прибыль
net_income =  annual_income - taxes# посчитайте чистую прибыль

speeds = np.array([60, 75, 90, 100, 80, 65])
distance = 150
slowdown_rate = 0.20

#adjusted_speeds =  # скорость с учетом 20% снижения
travel_times =  np.floor_divide(distance, speeds - speeds * slowdown_rate)# времени в пути для каждой скорости 

arr = np.array([5, 10, 15, 20, 25])

result =  arr % 2 ==0# булев массив, который показывает является ли каждый элемент массива четным

print(result)

