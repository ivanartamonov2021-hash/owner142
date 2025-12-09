import pandas as pd
data = pd.read_csv('titanic.csv')

data['Age'] = data['Age'].fillna(data['Age'].median()) # задание 5
print(data['Age'].head(10)) # задание 5
print(data['Age'].median()) # задание 5