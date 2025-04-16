import pandas as pd

data = {
    'employee': ['John'],
    'start_time': ['2023-09-10 08:00:00'],
    'end_time': ['2023-09-10 17:00:00']
}
df=pd.DataFrame(data)



def solution(df): 
#У вас есть таблица с временем начала и окончания работы сотрудников за день. 
#вычислите количество времени, которое каждый сотрудник проработал за день, и добавьте новый столбец work_duration.
    df=df.astype({
        'start_time':"datetime64[ns]",
        'end_time' : "datetime64[ns]"
    })
    df['work_duration'] =   df['end_time'] - df['start_time']

    return df

print(solution(df))