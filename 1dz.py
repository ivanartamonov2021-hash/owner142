import pandas as pd 
data = pd.read_csv('titanic.csv')




print(data['PassengerId'].count()) # кол - во пассажиров gghh




print(data['Age'].isnull().sum()) # кол - во незаполненных ячеек в столбце Age
