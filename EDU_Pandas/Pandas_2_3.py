
import pandas as pd

def solution_One(df): #Отфильтруйте товары из DataFrame sales, у которых цена больше 200 и количество на складе меньше 100.
    result = df.query("price > 200 and stock_qty < 100")

    return result


sales_one = pd.DataFrame({
    'product_code': ['P001', 'P002', 'P003', 'P004'],
    'product_group': ['PG1', 'PG3', 'PG2', 'PG3'],
    'price': [150, 250, 50, 400],
    'stock_qty': [300, 80, 150, 40]
})

def solution(df): #Отфильтруйте товары, принадлежащие к товарной группе "PG1" или "PG4", и у которых цена меньше 50 долларов. (df["price"] < 50) and
    result = df[ (df["product_group"].isin(["PG1", "PG4"])) & (df["price"] < 50)]

    return result

sales = pd.DataFrame({
    "product_code": [101, 102, 103, 104],
    "product_group": ["PG1", "PG2", "PG1", "PG4"],
    "price": [40, 60, 30, 45]
})




print(solution(sales))