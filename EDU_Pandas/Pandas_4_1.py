import pandas as pd

grocery = pd.read_csv("grocery.csv")

print(grocery.shape) #Размер фрэйма

print(list(grocery.columns)) # имена колонок таблицы

print(grocery.head()) # Вывести первыке 5 строк

print(grocery.groupby('product_group').mean(numeric_only=True)) #Вывкести сгруппированныей список с расчётос среднего по числовым колонкам  

print(grocery.groupby('product_description').agg( # выводим список с передачей агрументов
                        avg_price = ("price","mean"),
                        total_sales  = ("sales_quantity","sum")
    ).sort_values(by = 'total_sales' ,ascending = True) 
    )

data = {
    'product_description': ['Apple', 'Banana', 'Carrot', 'Apple'],
    'price': [1.00, 0.50, 1.50, 1.00],
    'sales_quantity': [200, 150, 100, 300]
}
df=pd.DataFrame(data)

#Ваша задача — вычислить среднюю цену и общее количество продаж для каждого товара, а затем отсортировать результат по количеству продаж в порядке убывания.

def solution_one(df: pd.DataFrame):
    result = df.groupby('product_description').agg(
        avg_price  = ('price', 'mean'),
        total_sales = ('sales_quantity','sum')
    )

    return result

print(solution_one(df))

data_2 = pd.DataFrame({
    "product_group": ["Fruit", "Vegetable", "Fruit", "Meat", "Meat"],
    "price": [5, 3, 6, 10, 12],
    "sales_quantity": [20, 15, 30, 5, 8]
})
#Рассчитайте среднюю цену и общее количество продаж для каждой группы товаров, используя функцию groupby, и отсортируйте результат по средней цене по убыванию.
def solution(df: pd.DataFrame):
    result = df.groupby("product_group").agg(
        avg_price  = ('price', 'mean'),
        total_sales = ('sales_quantity','sum')
    ).sort_values(by= 'avg_price', ascending=False) 

    return result

print(solution(data_2))

data_3 = pd.DataFrame({
    "product_description": ["Apple", "Banana", "Apple", "Beef", "Banana"],
    "price": [5, 2, 7, 10, 3]
})
#Найдите минимальную и максимальную цену для каждого описания продукта и отсортируйте результат по минимальной цене по возрастанию.
def solution(df: pd.DataFrame):
    result = df.groupby("product_description").agg(
        min_price = ("price",'min') ,
        max_price = ("price",'max')
    ).sort_values(by= 'min_price', ascending=True)

    return result