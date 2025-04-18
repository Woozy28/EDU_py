import pandas as pd
import numpy as np

data = pd.DataFrame({
    "A": [1, 2, np.nan, 5],
    "B": [np.nan, 5, 6, 7],
    "C": ["foo", np.nan, "foo", "bar"]
})

# все пропущенные значения в числовых столбцах средним значением по столбцу,
#  а в строковых столбцах — наиболее частым значением (модой).

def solution(df):
    
    for col in df.select_dtypes(include ='number'):
        df[col] = df[col].fillna(value = df[col].mean())
    
    for col in df.select_dtypes(exclude= 'number'):
        most_frequent = df[col].value_counts().index[0]
        df[col] = df[col].fillna(value = most_frequent)
    return df

print(solution(data))