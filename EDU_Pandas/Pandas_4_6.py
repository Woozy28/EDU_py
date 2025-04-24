import pandas as pd


import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Math": [85, 78],
    "Science": [92, 88]
})

df2 = pd.DataFrame({
    "Name": ["Charlie", "David"],
    "Math": [73, 95],
    "Science": [81, 90]
})

def solution(df1, df2):
    result = pd.concat([df1,df2], axis=0, ignore_index=True)

    return result


print(solution(df1,df2))