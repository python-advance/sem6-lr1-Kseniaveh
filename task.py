import pandas as pd
import re

"""
   Какое количество мужчин и женщин ехало на параходе? 
   Приведите два числа через пробел
"""
def get_nubmer_of_pass(sex, data = None):
    setsex = data.value_counts()
    if sex == 'male':
        return setsex['male']
    else:
        return setsex['female']
    
data = pd.read_csv('train.csv', index_col='PassengerId')
male_int = get_nubmer_of_pass('male', data['Sex'] )
female_int = get_nubmer_of_pass('female', data['Sex'])
#print(data['Sex'])
#print (male_int, female_int)

"""
    Подсчитайте сколько пассажиров загрузилось на борт в различных портах? 
    Приведите три числа через пробел.
"""
data = pd.read_csv('train.csv')
# группируем людей по портам отправления и считаем их отдельно для каждого порта
embarked = (data.groupby(['Embarked'])['PassengerId'].count())
# выводим количество людей для каждого порта через пробел
for i in list(embarked):
    print (i, end = ' ')  
    
"""
   Какие доли составляли пассажиры первого, второго, третьего класса?
"""
def get_number_pass_of_class(rec):
    data = pd.read_csv(rec)
    elem = data['Pclass']
    
    a = 0 # первый класс
    b = 0 # второй класс
    c = 0 # третий класс

    for el in elem:
            if el == 1:
                a += 1
            elif el == 2:
                b += 1
            elif el == 3:
                c += 1
    sum = a + b + c
    a_count = 100 * a / sum
    b_count = 100 * b / sum
    c_count = 100 * c / sum
    return  a_count, b_count, c_count
#get_number_pass_of_class('train.csv')

"""
    Посчитайте среднюю цену за билет 
"""
def price(rec):
    data = pd.read_csv(rec)
    return data['Fare'].mean()
#price('train.csv')

"""
    Посчитайте медиану за билет 
"""
def median(rec):
    data = pd.read_csv(rec)
    return data['Fare'].median()
#median('train.csv')

"""
    Коэффициент корреляции Пирсона между двумя столбцами
"""
def corr_Pirson(x, y):
    data = pd.read_csv('train.csv')
    res = data[x].corr(data[y])
    return res
#corr_Pirson('Age','Survived' )

"""
    Какое самое популярное мужское имя на корабле?
"""
def get_name(name):
    # Первое слово до запятой - фамилия
    fam = re.search('^[^,]+, (.*)', name)
    if fam:
        name = fam.group(1)

    # Если есть скобки - то имя пассажира в них
    fam = re.search('\(([^)]+)\)', name)
    if fam:
        name = fam.group(1)
 
    # Удаляем обращения
    name = re.sub('(Master\. |Mr\. |Mrs\. )', '', name)

    # Берем первое оставшееся слово и удаляем кавычки
    name = name.split(' ')[0].replace('"', '')

    return name
names = data[data['Sex'] == 'male']['Name'].map(get_name)
name_counts = names.value_counts()
#print(name_counts.head(1).index.values[0])


