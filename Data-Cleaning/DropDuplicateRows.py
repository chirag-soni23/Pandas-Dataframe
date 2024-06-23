import pandas as pd
# Drop duplicate emails
data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com']
}
df = pd.DataFrame(data)
# print(df)

def dropDuplicateEmail(customers:pd.DataFrame)->pd.DataFrame:
    # keep -> number of occurences
    # inplace -> modifed or not => True or False
    customers.drop_duplicates(subset='email',keep="first",inplace=True)
    return customers
print(dropDuplicateEmail(df))