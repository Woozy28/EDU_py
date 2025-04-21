import pandas as pd

#Сводная таблица

grocery = pd.read_csv("grocery.csv")

# Creating the week column
grocery["sales_date"] = grocery["sales_date"].astype("datetime64[ns]")
grocery["week"] = grocery["sales_date"].dt.isocalendar().week

print(list(grocery.columns))
# Creating the pivot table
print(
  pd.pivot_table(
    data = grocery, 
    values = "price", 
    index = "week", 
    columns = "product_group",
    aggfunc = ["mean","std"]
  )
)
print(
  pd.pivot_table(
    data = grocery, 
    values = "sales_quantity", 
    index = "product_group", 
    columns = "week",
    aggfunc = "sum",
    margins = True,
    margins_name = "Total"
  )
)

data = {'product_group': ['fruits', 'vegetables', 'fruits', 'vegetables', 'fruits', 'vegetables'],
        'week': [1, 1, 2, 2, 3, 3],
        'sales_quantity': [20, 15, 25, 12, 30, 18]}

df = pd.DataFrame(data)

#Необходимо создать сводную таблицу, которая показывает максимальные и минимальные продажи для каждой группы товаров за неделю.

def solution(df: pd.DataFrame):
    result = pd.pivot_table(
        data = df,
        values='sales_quantity',
        index = 'product_group',
        columns = "week",
        aggfunc = ["max","min"]
    )

    return result

print(solution(df))