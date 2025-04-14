import pandas as pd

#У вас есть DataFrame с данными о продажах товаров. Нужно выбрать третью и четвертую строки, а также первые два столбца.

def solution(df):
    df = pd.DataFrame(df) #на входе надо переделать дикт в дата фрэйм
    print(type(df))
    result = df.iloc[[1,2],[0,1]] #отправляем в рзалт нужные строки и столбцы

    return result

data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Headphones'],
    'Price': [1000, 700, 300, 100],
    'Quantity': [5, 8, 3, 10]
}

print(solution(data))    

#Используя метод loc, выберите первые 5 строк и столбцы с названиями product_code и product_group.

def solution(df:data):
    
    result =1 #пишите код здесь

    return result