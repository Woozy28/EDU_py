import pandas as pd

data1 = pd.DataFrame({
    'product_name': ['Laptop', 'Smartphone', 'Tablet', 'Headphones'],
    'price': [1000, 700, 150, 80],
    'stock_qty': [50, 120, 300, 400]
})


def solution_one(df): #Выберите товары, у которых цена больше 200 и количество на складе меньше 150.
    result = df.query("price > 200 and stock_qty < 150")

    return result



data2 = pd.DataFrame({
    'product_name': ['Laptop', 'Smartphone', 'Tablet', 'Sofa', 'Chair'],
    'product_group': ['Electronics', 'Electronics', 'Electronics', 'Furniture', 'Furniture'],
    'price': [1000, 700, 300, 400, 150],
    'stock_qty': [50, 120, 300, 10, 50]
})

def solution_two(df): #Отфильтруйте товары, которые принадлежат к категориям "Electronics" или "Furniture" и имеют цену меньше 500. Затем выведите столбцы "product_name", "price", и "stock_qty".
    result = df[(df['product_group'].isin(['Electronics','Furniture']))&(df['price']< 500)]

    return result[["product_name", "price", "stock_qty"]]




data = pd.DataFrame( {
    'title': ['Harry Potter', 'The Hobbit', 'Fantastic Beasts', 'Silmarillion'],
    'author': ['J.K. Rowling', 'J.R.R. Tolkien', 'J.K. Rowling', 'J.R.R. Tolkien'],
    'sold_copies': [5000000, 3000000, 2000000, 1000000]
})

def solution(df): #Отфильтруйте все книги, написанные автором "J.K. Rowling", и выведите название книги и количество проданных копий.
    result = df.query("author == 'J.K. Rowling'")

    return result[['title','sold_copies']]



print(solution(data))

