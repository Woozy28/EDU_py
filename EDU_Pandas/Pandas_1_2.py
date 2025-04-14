import pandas as pd 

myseries = pd.Series([10, 20, 30])

df = pd.DataFrame({
    "Name": ["Jane", "John", "Matt", "Ashley"],
    "Age": [24, 21, 26, 32]
})


#df.shape Show size


sales = pd.read_csv("sales.csv", usecols=["product_code","product_group","stock_qty"])

print(sales.head())