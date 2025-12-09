import pandas as pd
data = pd.read_csv('titanic.csv')

print(data[data['Pclass'] == 1]['Fare'].mean()) # средняя стоимость билета для 1 класса




print(data[data['Pclass'] == 3]['Survived'].mean() * 100) # выживаемость 3 - его класса