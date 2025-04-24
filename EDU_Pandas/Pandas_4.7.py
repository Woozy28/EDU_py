import pandas as pd

# create product and sales DataFrames
product = pd.DataFrame({
  "product_code": [1001, 1002, 1003, 1004],
  "weight": [125, 200, 100, 400],
  "price": [10.5, 24.5, 9.9, 34.5]
})

sales = pd.DataFrame({
  "product_code": [1001, 1002, 1003, 1007],
  "sales_date": ["2021-12-10"] * 4,
  "sales_qty": [8, 14, 22, 7]
})

# merge DataFrames
merged_df = product.merge(sales, how="left", on="product_code")

print(merged_df)