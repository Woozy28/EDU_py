import pandas as pd

sales = pd.read_csv("sales.csv")

print(sales.shape) #Возвращает количество столбцов и строк фрэйма

print(sales.size) #ВОзвращает количество ячеек фрейма

print(len(sales)) #Лен вернёт количество строк
print(sales.dtypes)

sales["stock_qty"] = sales["stock_qty"].astype("float") #Можно менять тип данных в колонке

print(sales.dtypes)

sales = sales.astype({
  "stock_qty": "float",
  "last_week_sales": "float"
}) # В астайп можно запихать сразу несколько колонок 

print(sales.dtypes)

print(sales["product_group"].nunique())

print(sales["product_group"].unique())