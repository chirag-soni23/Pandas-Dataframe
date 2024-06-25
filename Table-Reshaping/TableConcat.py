import pandas as pd
# concatenate Table
# Data 1
data1 = {
    'student_id': [1, 2, 3, 4],
    'name': ['Mason', 'Ava', 'Taylor', 'Georgia'],
    'age': [8, 6, 15, 17]
}
# Data 2
data2 = {
    'student_id': [5, 6],
    'name': ['Leo', 'Alex'],
    'age': [7, 7]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
# print(df1)
# print(df2)

def concatenateTable(df1:pd.DataFrame,df2:pd.DataFrame)->pd.DataFrame:
    return pd.concat([df1,df2])
print(concatenateTable(df1,df2))