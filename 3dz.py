import pandas as pd
data = pd.read_csv('titanic.csv')


print(data[data['Survived'] == 1].shape[0]) #кол - во живых




print((data[data['Survived'] == 1].shape[0]) / 891 * 100) # процент выживших




print(data[data['Sex']=='female']['Survived'].mean()*100) # выживаемость женщин




print(data[data['Sex']=='male']['Survived'].mean()*100) # выживаемость мужчин