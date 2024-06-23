import pandas as pd
# Select data
data = {
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
}
df = pd.DataFrame(data)
# print(df)

def selectData(students:pd.DataFrame)->pd.DataFrame:
    return students.loc[students['student_id']==101,['name','age']]
print(selectData(df))
    