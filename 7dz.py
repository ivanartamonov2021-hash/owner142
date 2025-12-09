import pandas as pd
data = pd.read_csv('titanic.csv')


print(data[data['Survived'] == 1]['Age'].mean()) # ср возраст выживших




print(data[data['Survived'] == 0]['Age'].mean()) # ср возраст погибших