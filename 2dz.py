import pandas as pd
data = pd.read_csv('titanic.csv')


print(data[data['Sex'] == 'male']['PassengerId'].count()) # кол - во мужчин на корабле




print(data[data['Pclass'] == 1].shape[0]) #кол - во кают 1 класса
