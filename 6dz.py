import pandas as pd
data = pd.read_csv('titanic.csv')

p = data['SibSp'] # 6 задание
o = data['Parch'] # 6 задание
data['FamilySize'] = p + o + 1 # 6 задание
print(data.iloc[887]) # 6 задание
