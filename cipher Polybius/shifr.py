from __future__ import print_function
import math

import random

random.shuffle([1,2,3])

file = open('key.txt', 'r')
str2 = file.read()
str2 = str2.lower()

# класс для выделения каждого элемента из строки алфавит
class SomeObject(object):
    def __init__(self, name):
       self.name = name
  
    def __str__(self):
       return '%s' % self.name

strokka = str(SomeObject(file.read()))
strokka = strokka.lower()

# заводим словарь для хранения позиций элементов
dict = {}
matr = []
matr1 = []

a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя!.,?-:;"()0123456789'
b = SomeObject(a)
strokka = ''

# добавление ключа
for i in (str2):
    if a.find(i) != -1 and strokka.find(i) == -1: # если символ еще не встречался
        strokka += str(SomeObject(i)) # добавляются все символы из ключа в новую строку
for i in a: # добавление алфавита
    if strokka.find(i) == -1: # если символ еще не встречался
        strokka += str(SomeObject(i)) # добавляется символ

a = strokka
b = a
kol_vo = (math.sqrt(len(b))) # берем квадратный корень из длинны строки для следующей проверки

def sqrtmatrix(kol_vo, l): # проверка на приближенность к квадратной матрицы
    if kol_vo % 1 > 0: # квдаратный корень деленный на 1 будет больше нуля, то все ок
       for i in range(int(kol_vo), -1, -1):
         if l % i == 0:
            kol_vo = i - 1
            return kol_vo
            break
    else:
      return (int(kol_vo) - 1) # если нет, то берем корень на единицу меньше и снова проверяем

# тогда в результате присваиваем приближенное число для построение матрицы
kol_vo = sqrtmatrix(kol_vo, len(b))

if kol_vo == 0: # если это простое число
  kol_vo = sqrtmatrix(math.sqrt(len(b)), len(b) + 1) # то добавляется другой символ в алфавит

# выводится результирующая длина матрицы
print(len(b))
print ()

# заводятся индексы
ii = 0
jj = 0
matr = []

# запись ключа в матрицу
for i in strokka:
  if ii > kol_vo:
      matr.append(matr1)
      matr1 = []
      ii = 0
      jj += 1

  if a.find(i) != -1: # если символа еще не было в матрице
      matr1.append(i)
      dict[i] = ii * 10 + jj # сохраняем номер строки и столбца у этого символа в словарь
      a = a.replace(i,'')
      ii += 1

kol = len(a)
ii = 0

for i in range (kol): # заполняем остальные символы алфавита в матрицу
  if ii > kol_vo:
      matr.append(matr1)
      matr1 = []
      ii = 0
      jj += 1
  matr1.append(a[0])
  dict[a[0]] = ii * 10 + jj # сохраняем номер строки и столбца у этого символа в словарь
  a = a.replace(a[0],'')
  ii += 1

if len(matr) <= jj: # если мы видим, что для полной квадратной матрицы не хватает символов в строке
    matr1.append('3') # добавляем еще один рандомный символ
matr.append(matr1)


file1 = open('message_shifr.txt', 'r')

# выводим матрицу
for i in range(jj + 1):
    for j in range(kol_vo + 1):
        print(matr[i][j], end = '')
    print()
STROKA = file1.read()
STROKA = STROKA.lower()
i = 0
num = 0

while i < len(STROKA):
  if b.find(STROKA[i]) == -1: # удаляем не нужные символы
    STROKA = STROKA.replace(STROKA[i], '')
  else:
      i += 1

newstr = ''
itog = ''

for i in (STROKA):
    zn = dict[i]
    zn1 = str(zn // 10) # конвертирование строки в стринг
    zn2 = str(zn % 10) # конвертирование колонки в стринг
    itog = itog + str(zn1) + str(zn2) # позиция символа в матрице (создание самого шифра)

print()
print(itog)
file2 = open('shifr.txt', 'w')
file2.write(itog)