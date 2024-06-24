import pandas as pd
# fill missing value
data = {
    'Name': ['Wristwatch', 'WirelessEarbuds', 'GolfClubs', 'Printer'],
    'Quantity': [None, None, 779, 849],
    'Price': [135, 821, 9319, 3051]
}
df = pd.DataFrame(data)
# print(df)

def fillMissingValues(products:pd.DataFrame)->pd.DataFrame:
    products['Quantity'].fillna(0,inplace=True)
    return products
print(fillMissingValues(df))