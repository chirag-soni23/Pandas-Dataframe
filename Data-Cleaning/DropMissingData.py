import pandas as pd
# Drop missing data
data = {
    'student_id': [32, 217, 779, 849],
    'name': ['Piper', None, 'Georgia', 'Willow'],
    'age': [5, 19, 20, 14]
}
df = pd.DataFrame(data)
# print(df)

def dropMissingData(students:pd.DataFrame)->pd.DataFrame:
    # first method
    return students.dropna(subset='name')
    # second method
    # return students.dropna(
    #     axis=0,
    #     how='any',
    #     subset=['name'],
    #     inplace=False,
    #     ignore_index=False
    # )
print(dropMissingData(df))