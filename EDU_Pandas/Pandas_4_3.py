import pandas as pd

#Функция Where

grocery = pd.read_csv("grocery.csv")

grocery["price_updated"] = grocery["price"].where(
  grocery["price"] >= 3,
  other = grocery["price"] * 1.1
)

print("Checking prices less than $3:")
print(grocery[grocery["price"] < 3][["price","price_updated"]].head())

print("\nChecking prices of $3 or more:")
print(grocery[grocery["price"] >= 3][["price","price_updated"]].head())

grocery["price_updated"] = grocery["price"].where(
  grocery["product_group"] != "vegetable",
  other = grocery["price"] * 0.9
)

print("Checking prices of vegetables:")
print(grocery[grocery["product_group"] == "vegetable"][["price","price_updated"]].head())

print("\nChecking prices of other products:")
print(grocery[grocery["product_group"] != "vegetable"][["price","price_updated"]].head())

data = {'product_group': ['fruits', 'vegetables', 'fruits', 'vegetables', 'fruits'],
        'price': [2.5, 3.5, 2.8, 1.8, 4.0]}

df = pd.DataFrame(data)

#Используя функцию where, необходимо уменьшить цену на 10% для товаров в категории "vegetables". Для всех остальных категорий цены должны остаться неизменными.
def solution(df: pd.DataFrame):
    df['price_updated'] = df['price'].where(
        df['product_group'] != 'vegetables', df['price']*0.9
    )

    return df

print(solution(df))