import pandas as pd

def solution_one(df): #Объедините столбцы "Имя" и "Отдел" в одну строку с разделителем "-". Выведите новый объединённый столбец.
    result = df['name'] + "-" + df['department']

    return result

data1 = {'name': ['Alice Smith', 'Bob Johnson'], 'department': ['HR', 'Sales']}
df1 = pd.DataFrame(data1)

data2 = {'name': ['Alice Smith', 'Bob Johnson', 'Charlie Brown']}
df2=pd.DataFrame(data2)

def solution_two(df): #Разделите столбец "Имя" на два новых столбца: "Имя" и "Фамилия" (Гарантированно разделенные пробелом). Затем выведите получившиеся столбцы.
    df['last_name']= df['name'].str.split(" ", expand=True)[1]
    df['first_name']= df['name'].str.split(" ", expand=True)[0]
    
    return df[['first_name','last_name']]


data = pd.DataFrame({
    'name': ['Alice Smith', 'Bob Johnson', 'Charlie Brown'],
    'hire_date': ['15/03/2010', '22/07/2015', '01/01/2020']
})

#Извлечь только год из столбца "hire_date".
#Разделить столбец "name" на два новых столбца: "first_name" и "last_name".
#Объединить фамилию и год найма в один столбец с разделителем " - ".
#Преобразовать фамилию в верхний регистр в новом столбце.


def solution(df):
    
    df['year_hired'] = df['hire_date'].str[-4:]
    df[["first_name" , "last_name"]] = df['name'].str.split(' ', expand=True)
    df['combined'] = df["last_name"].str.upper() + ' - ' + df['year_hired']

    return df[["first_name" , "last_name", 'year_hired', 'combined']]

solution(data)
