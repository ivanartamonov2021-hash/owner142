import pandas as pd
data = pd.read_csv('titanic.csv')




print(data['PassengerId'].count()) # кол - во пассажиров




print(data['Age'].isnull().sum()) # кол - во незаполненных ячеек в столбце Age




print(data[data['Sex'] == 'male']['PassengerId'].count()) # кол - во мужчин на корабле




print(data[data['Pclass'] == 1].shape[0]) #кол - во кают 1 класса




print(data[data['Survived'] == 1].shape[0]) #кол - во живых




print((data[data['Survived'] == 1].shape[0]) / 891 * 100) # процент выживших




print(data[data['Sex']=='female']['Survived'].mean()*100) # выживаемость женщин




print(data[data['Sex']=='male']['Survived'].mean()*100) # выживаемость мужчин




print(data[data['Pclass'] == 1]['Fare'].mean()) # средняя стоимость билета для 1 класса




print(data[data['Pclass'] == 3]['Survived'].mean() * 100) # выживаемость 3 - его класса




data['Age'] = data['Age'].fillna(data['Age'].median()) # задание 5
print(data['Age'].head(10)) # задание 5
print(data['Age'].median()) # задание 5



p = data['SibSp'] # 6 задание
o = data['Parch'] # 6 задание
data['FamilySize'] = p + o + 1 # 6 задание
print(data.iloc[887]) # 6 задание




print(data[data['Survived'] == 1]['Age'].mean()) # ср возраст выживших




print(data[data['Survived'] == 0]['Age'].mean()) # ср возраст погибших




a = data[data['Sex'] == 'female'] # кл - во выживших женщин 
b = a[a['Survived'] == 1] # кл - во выживших женщин 
print(len(b)) # кл - во выживших женщин 




c = data[data['Age'] < 18] # моложе 18 без родителей
d = c[c['Parch'] == 0] # моложе 18 без родителей
print(len(d)) # моложе 18 без родителей
