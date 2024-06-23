import pandas as pd
# modify salary column
data = {
    'name': ['Jack', 'Piper', 'Mia', 'Ulysses'],
    'salary': [19666, 74754, 62509, 54866]
}
df = pd.DataFrame(data)
print(df)

def modifieSalarycolumn(employees:pd.DataFrame)->pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees
print(modifieSalarycolumn(df))