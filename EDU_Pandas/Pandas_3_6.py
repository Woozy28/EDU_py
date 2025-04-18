import pandas as pd

data = {
    'name': ['Anna', 'Mike', 'Sophia'],
    'age': [29, None, 34]
}
df=pd.DataFrame(data)

def solution(df): 
#Ваша задача — заменить пропущенные значения в столбце "age" средним значением этого столбца.
     df["age"] = df["age"].fillna(value = df["age"].mean())

     return df

print(solution(df))