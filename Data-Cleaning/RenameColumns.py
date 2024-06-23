import pandas as pd
# rename column
data = {
    'id': [1, 2, 3, 4, 5],
    'first': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'],
    'last': ['King', 'Wright', 'Hall', 'Thompson', 'Moore'],
    'age': [6, 7, 16, 18, 10]
}
df = pd.DataFrame(data)
# print(df)

def renameColumns(students:pd.DataFrame)->pd.DataFrame:
    return students.rename(
        columns={
            "id":"student_id",
            "first":"first_name",
            "last":"last_name",
            "age":"age_in_years"
        }
    )
print(renameColumns(df))    
