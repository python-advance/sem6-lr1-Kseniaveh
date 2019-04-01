import pandas as pd
import csv

"""
[HW] #1 Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
"""
data = pd.read_csv('train.csv')
# группируем людей по портам отправления и считаем их отдельно для каждого порта
embarked = (data.groupby(['Embarked'])['PassengerId'].count())
# выводим количество людей для каждого порта через пробел
for i in list(embarked):
    print (i, end = ' ')  
# Ответ: 168 77 644 

"""
[HW] #2 Какие доли составляли пассажиры первого, второго, третьего класса?
"""
pclass_counts = data['Pclass'].value_counts()
pclass_1 = 100.0 * pclass_counts[1] / pclass_counts.sum()
pclass_2 = 100.0 * pclass_counts[2] / pclass_counts.sum()
pclass_3 = 100.0 * pclass_counts[3] / pclass_counts.sum()
print("первый класс", "{:0.2f}".format(pclass_1))
print("второй класс", "{:0.2f}".format(pclass_2))
print("третий класс", "{:0.2f}".format(pclass_3))
# Ответ: первый класс 24.24
#        второй класс 20.65
#        третий класс 55.11

"""
[HW] #3 Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
            возрастом и параметром survival;
            полом человека и параметром survival;
            классом, в котором пассажир ехал, и параметром survival.
"""



"""
[HW] #4 Посчитайте среднюю цену за билет и медиану.
"""
data = pd.read_csv('train.csv')
price = data['Fare'].mean()  #среднее
median = data['Fare'].median()   #медиана
print(round(price,2), median)
# Ответ: 32.2 14.4542

"""
[HW] #5 Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
"""
def get_nubmer_of_pass(sex, data = None):
    """
        Какое количество мужчин и женщин ехало на параходе? 
        Приведите два числа через пробел
    """
    setsex = data.value_counts()
    if sex == 'male':
        return setsex['male']
    else:
        return setsex['female']
    
data = pd.read_csv('train.csv', index_col='PassengerId')
male_int = get_nubmer_of_pass('male', data['Sex'] )
female_int = get_nubmer_of_pass('female', data['Sex'])
#print(data['Sex'])
print (male_int, female_int)
# Ответ: 577 314
