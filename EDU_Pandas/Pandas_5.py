import pandas as pd
import numpy as np

data1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df1 = pd.DataFrame(data1)
result1 = df1.loc[1, 'B']


data = {
    'product': ['TV', 'Sofa', 'Laptop', 'Table'],
    'category': ['Electronics', 'Furniture', 'Electronics', 'Furniture'],
    'price': [1200, 800, 1500, 300]
}

df = pd.DataFrame(data)

#Дан DataFrame с информацией о продуктах, содержащий столбцы product, category, и price. 
# Необходимо отфильтровать (оставить) все строки, где категория продукта равна 'Electronics', и цена превышает 1000.

def solution1(df: pd.DataFrame):
    result = df[(df['category'] == 'Electronics') & (df['price'] > 1000) ]
        
        

    return result[['product','category','price']]



data2 = {
    'A': [1, 2, np.nan, 4, np.nan],
    'B': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data2)

#Дан DataFrame, содержащий пропущенные значения в столбце A. 
# еобходимо заменить все пропущенные значения в этом столбце на среднее значение столбца A.

def solution2(df: pd.DataFrame):
    df['A'] = df['A'].where(
        ~df['A'].isna(),
        other =  df['A'].mean()
    )

    return df




data = {
    'date': ['2024-01-15', '2024-02-20', '2024-03-25'],
    'sales': [1000, 1500, 2000]
}

df = pd.DataFrame(data)

#Дан DataFrame с датами в столбце date и значениями в столбце sales. 
# Необходимо преобразовать столбец date в формат datetime и извлечь месяц в отдельный столбец month.

def solution3(df: pd.DataFrame):
    df = df.astype({'date': "datetime64[ns]"})
    
    df['month'] = df['date'].dt.month

    return df





data = {
    'category': ['Electronics', 'Furniture', 'Electronics', 'Furniture'],
    'sales': [2000, 1500, 3000, 2000]
}

df = pd.DataFrame(data)

#Дан DataFrame с информацией о продажах, содержащий столбцы category и sales. 
# Необходимо сгруппировать данные по категории и вычислить общую сумму продаж для каждой категории.

def solution4(df: pd.DataFrame):
   

    return  df.groupby('category').sum().reset_index()




data = {
    'student_id': [1, 1, 2, 2],
    'subject': ['Math', 'Science', 'Math', 'Science'],
    'score': [90, 85, 88, 92]
}

df = pd.DataFrame(data)

#Дан DataFrame с информацией о студентах, содержащий столбцы student_id, subject, и score. 
# Необходимо преобразовать DataFrame, чтобы каждая строка представляла одного студента, а каждый 
# предмет был представлен отдельным столбцом с соответствующим баллом.


def solution(df):
    result = pd.pivot_table(
        data= df,
        values = 'score', 
        index= 'student_id',
        columns = 'subject',
    ).reset_index()

    return result

print(solution(df))