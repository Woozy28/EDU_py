import pandas as pd

myseries = pd.Series([1, 2, 5, 7, 11, 36])

print(myseries.median()) #Медиана то значение находящееся посередине, когда значения отсортированы в порядке возрастания или убывания

myseries = pd.Series([1, 4, 6, 6, 6, 11, 11, 24])

print(f"The mode of my series is {myseries.mode()[0]}") #Мода это наиболее часто встречающееся значение в наборе данных

sales = pd.read_csv("sales.csv")

print("mean: ")
print(sales["price"].mean())

print("median: ")
print(sales["price"].median())

print("mode: ")
print(sales["price"].mode()[0])

print("minimum: ")
print(sales["price"].min())

print("maximum: ")
print(sales["price"].max())