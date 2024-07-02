import pandas as pd
# Find heavy animals
data = {
    'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
    'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
    'age': [98, 50, 6, 45, 100, 26],
    'weight': [464, 41, 328, 463, 50, 349]
}
df = pd.DataFrame(data)
# print(df)

def findHeavyAnimals(animals:pd.DataFrame)->pd.DataFrame:
    heavy_animals = animals[animals['weight']>100]
    return heavy_animals.sort_values(by='weight',ascending=False)[['name']]
print(findHeavyAnimals(df))