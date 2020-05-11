
file = open('text.txt', encoding='UTF-8')
my_new_text = file.read()


#1) методами строк очистить текст от знаков препинания;

punctuation = ['.', ',', ':', ';', '!', '?', '«', '»', '(', ')', ' —', ' — ', '—']
for p in range(len(punctuation)):
    my_new_text = my_new_text.replace(punctuation[p], '')
    print(my_new_text)


# 2) сформировать list со словами (split);

my_new_text = list(my_new_text.split())
print(type(my_new_text), len(my_new_text), my_new_text)


# 3) Привести все слова к нижнему регистру (map)
my_new_text = list(map(str.lower, my_new_text))
print(type(my_new_text), len(my_new_text), my_new_text)

#  4) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;

from collections import Counter
mydict = dict(Counter(my_new_text))
print(type(mydict), len(mydict), mydict)

# 5) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).

top_ofdict = list(mydict.items())
top_ofdict.sort(key=lambda i: i[1])
top_ofdict.reverse()
five_top_ofdict = dict(top_ofdict[0:5])
five_top_ofdict = list(five_top_ofdict.keys())
print('5 наиболее часть встречающихся слов:', five_top_ofdict)

# Количество разных слов в тексте set

mydict = set(mydict)
print('Количество разных слов в тексте:', len(mydict))