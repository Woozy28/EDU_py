import numpy as np

array = np.array([1.1, 2.7, 3.4, 4.9])

result =  np.abs(array) # абсолютные значения всех элементов массива

result =  np.sqrt(array)# квадратные корни для каждого элемента

result =  np.log(array)# натуральные логарифмы для каждого элемента

result =  np.sign(array)# знак каждого элемента

result = np.ceil(array) # округлите элементы массива в большую сторону

result = np.floor(array) # округлите элементы массива в меньшую сторону

result = np.isnan(array) # булев массив, указывающий, является ли каждый элемент NaN

fractional_part, integer_part =  np.modf(array)# дробная и целая часть массива

result = np.square(array) # возведите каждый элемент в квадрат

squares =  np.square(array)# возведите каждый элемент в квадрат
result =  np.sign(squares)# определите знак каждого элемента

result =  np.sqrt(np.abs(array))# квадратные корни для каждого элемента # найдите абсолютные значения

print(result)

