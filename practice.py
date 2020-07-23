# -*- coding: cp1251 -*-
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('math_students.csv', delimiter=',')

#  №1
x = (data['traveltime'].value_counts()) # отсортируем значения в столбце traveltime по их количеству
print('значение', x.keys()[0], 'было самым частым значением в признаке traveltime') # и выведем первое значение

# №2
print(data[(data['Medu'] == 4) & (data['Fedu'] != 4)].shape[0], '- это кол-во студентов, у которых у матери есть высшее образование, а у отца нет')

# №3
Gp = data[data['school'] == 'GP'] # выберем учеников из школы GP
print(min(Gp['age'].unique()), '- это минимальный возраст учащегося школы Gabriel Pereira')    # и выведем минимальный возраст ученика из этой школы

# №4
search = data[(data['absences']%2 != 0) & (data['nursery'] == 'no')]
print(search.shape[0], '- это количество студентов, имеющих нечетное число пропусков и которые не посещали детский сад')

# №5
def mean(table):
    return table['G3'].mean() # найдём среднее значения для каждого типа

get, dont_get = mean(data[data['famsup'] == 'yes']), mean(data[data['famsup'] != 'yes']) # распределяем учеников 
print(round((get - dont_get), 2), '- разность между средними итоговыми оценками студентов, которые получают помощь от семьи при выполнении заданий и теми, кто не получает помощь при выполнении заданий.') # выводим с двумя знаками после запятой 

# №6
data_by_famrel = data.groupby('famrel').mean() # находим среднюю итоговую оценку для каждого значения в столбце famrel
plt.xlabel('famrel')
plt.ylabel('G3')
plt.xlim([1, 5])  #устанавливаем диапозон для осей
plt.ylim([0, 20])
plt.plot(data_by_famrel['G3'])
plt.show()
print('famrel не оказывает существенного влияние на итоговую оценку')