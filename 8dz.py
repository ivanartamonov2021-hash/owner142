import pandas as pd
data = pd.read_csv('titanic.csv')


a = data[data['Sex'] == 'female'] # кл - во выживших женщин 
b = a[a['Survived'] == 1] # кл - во выживших женщин 
print(len(b)) # кл - во выживших женщин 




c = data[data['Age'] < 18] # моложе 18 без родителей
d = c[c['Parch'] == 0] # моложе 18 без родителей
print(len(d)) # моложе 18 без родителей