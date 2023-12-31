'''Напишите программу, которая вычисляет длину отрезка (т.е. расстояние между двумя точками), заданного двумя значениями x1 и x2 (вещественные числа).



🚀>P.S.: Подсказка для решения 🚀
Вы уже догадались, что нужно из одной точки вычитать другую, допустим возьмем формулу x2 - x1. Проблема в этой задаче в том, что мы не знаем в какой точке будет максимум. И я могу подсказать вам два решения

1) Например, возьмем две значения 8 и 4. У нас есть два варианта

 x1=8 тогда x2=4. Тогда по нашей формуле x2 - x1 = 4
x1=4 тогда x2=8. Тогда по нашей формуле x2 - x1 = -4
С одной стороны получили разные значения, но если отбросить минус, то они будут равны. Какая функция позволяет отбросить знак?

2) При помощи функция min max определить максимальное и минимальное значение, и тогда вы точно будете из большего отнимать меньшее и никаких минусов не возникнет'''

a = float(input())
b = float(input())

c = max(a, b)
d = min(a, b)

e = c - (d)

print (abs(e))

