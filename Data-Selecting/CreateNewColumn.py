import pandas as pd
# create new column
data = {
    'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
    'salary': [4548, 28150, 1103, 6593, 74576, 24433]
}
df = pd.DataFrame(data)
# print(df)

def createBonusColumn(employees:pd.DataFrame)->pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    # employees = employees.assign(bonus=employees['salary']*2)
    return employees
print(createBonusColumn(df))
