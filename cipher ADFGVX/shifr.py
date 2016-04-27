from __future__ import print_function
import math
import random

file = open('random.txt', 'r')
strr = file.read()
strr = strr.lower()

b = ''
dict = {}
matr = []
matr1 = []

for i in range(97, 123):
    b += chr(i)
for i in range(48, 58):
    b += chr(i)

print("")
print("alphabet")
a = b
print(a)
print(" ")

adv = 'ADFGVX'
ii = 0
jj = 0
kol = len(strr)

# удаляем элементы, не входящие в алфавит и формируем матрицу 6х6
for i in range(kol):
  if ii > 5:
      matr.append(matr1)
      matr1 = []
      ii = 0
      jj += 1
  if a.find(strr[i]) != -1:
      matr1.append(strr[i])
      dict[strr[i]] = jj * 10 + ii
      a = a.replace(strr[i],'')
      ii += 1

kol = len(a)

for i in range(kol):
  if ii > 5:
      matr.append(matr1)
      matr1 = []
      ii = 0
      jj += 1
  matr1.append(a[0])
  dict[a[0]] = jj * 10 + ii # сохраняем позиции строчки и столбца последнего элемента
  a = a.replace(a[0],'') # здесь хранится просто алфавит
  ii += 1

print('матрица:')
matr.append(matr1)
for i in range(6):
    for j in range(6):
        print(matr[i][j], end = '')
    print()


def help(kluch, itog, posl): # функция для формирования шифра
    matr2 = []
    matr1 = []
    print(itog)

    # len(itog) = длинна каждого блока (каждый блок = len(kluch)^2)
    # если блок имеет такой же размер, как и len(kluch)
    # добавляем все элементы в этом блоке в матрицу matr1(по строчке)
    # иначе (если размер блока < len(kluch)
    # добавляем необходимый символ "A" в матрицу matr1

    for i in range(len(kluch)):
        for j in range(int(math.ceil(float(len(itog)) / len(kluch)))):
            if (j * (len(kluch)) + i) < len(itog):
               matr1.append(itog[j * len(kluch) + i])
            else:
              matr1.append(random.choice(adv))
        matr2.append(matr1)
        matr1 = []

    i = 0
    kol = len(matr2[0])

    for i in range(kol):
        for j in range(len(matr2)):
            print(matr2[j][i], end = '')
        print()

    i = 1
    print('')
    print('последовательность шифровки:')
    print(posl)
    print('')
    # сортируем колонки в матрице как по ключу
    # posl поможет при сортировке
    while i < len(posl):
        l = matr2[int(posl[i])]
        matr2[int(posl[i])] = matr2[int(posl[i - 1])]
        matr2[int(posl[i - 1])] = l
        i += 2

    newstr = ''
    print('итоговая матрица шифр:')
    # выводится финальная матрица с отсортированными колонками
    kol = len(matr2[0])
    for i in range(kol):
        for j in range(len(matr2)):
            print(matr2[j][i], end = '')
        print()

    for i in range(len(kluch)):
        for j in range(int (math.ceil(float(len(itog)) / len(kluch)))):
            newstr += matr2[i][j]
    print(newstr)
    print('')
    return newstr

def help1(kluch, itog, posl):
    matr2 = []
    matr1 = []
    print(itog)

    # len(itog) = длинна каждого блока (каждый блок = len(kluch)^2)
    # если блок имеет такой же размер, как и len(kluch)
    # добавляем все элементы в этом блоке в матрицу matr1(по строчке)
    # иначе (если размер блока < len(kluch)
    # добавляем необходимый символ "A" в матрицу matr1

    for i in range(len(kluch)):
        for j in range(int(math.ceil(float(len(itog))/ len(kluch)))):
             if (j * (len(kluch)) + i) < len(itog):
                matr1.append(itog[j + i* (int(math.ceil(float(len(itog))/ len(kluch)))) ])
             else:
              matr1.append(random.choice(adv))
        matr2.append(matr1)
        matr1 = []

    i = 0
    kol = len(matr2[0])
    for i in range(kol):
        for j in range(len(matr2)):
            print(matr2[j][i], end = '')
        print()

    i = 1
    print(posl)
    print('')


    while i < len(posl):
        l = matr2[int(posl[i])]
        matr2[int(posl[i])] = matr2[int(posl[i - 1])]
        matr2[int(posl[i - 1])] = l
        i += 2

    newstr = ''
    print('итоговая матрица дешифр:')

    kol = len(matr2[0])
    for i in range(kol):
        for j in range(len(matr2)):
            print(matr2[j][i], end = '')
        print()
    for j in range(int (math.ceil(float(len(itog))/ len(kluch)))):
        for i in range(len(kluch)):
            newstr += matr2[i][j]

    print(newstr)
    return newstr

def shifr():
    print('=== шифровка ===')
    file3 = open('key.txt', 'r')
    kluch = file3.read()
    kluch = kluch.lower()

    kl = '' # добавляем верный ключ в переменную
    i = 0

    while i < len(kluch):
      if b.find(kluch[i]) == -1: # смотрим ненужные символы в ключе
         kluch = kluch.replace(kluch[i],'')
      else:
         if kl.find(kluch[i]) == -1:
             kl += kluch[i]
         i += 1

    print('')
    print('ключ:')
    print(kl)
    print('')
    kluch = kl
    posl = ''

  # ключ сортируется по алфавиту
    for i in reversed(range(len(kluch))):
       for j in range(1, i + 1):
           if kluch[j - 1] > kluch[j]:
                a = [kluch[0:j - 1],kluch[j],kluch[j - 1],kluch[j + 1:]] # словарь, в котором хранятся символы ключа
                kluch = ''.join(a)
                posl = posl + str(j) + str(j - 1) # записывается позиции символов которые надо поменять
    print('последовательность замены:')
    print(posl)

    file1 = open('message_shifr.txt', 'r') #сообщение на шифровку
    STROKA = file1.read()
    STROKA = STROKA.lower()

    i = 0
    num = 0

    while i < len(STROKA): # проверяем наличие неверных символов в сообщении
      if b.find(STROKA[i]) == -1:
        STROKA = STROKA.replace(STROKA[i],'')
      else:
          i += 1

    newstr = ''
    itog = '' #формируется сообщение вида ADFGVX из таблицы

    # добавляем в таблицу символы из сообщения
    for i in range(len(STROKA)):
        zn = dict[STROKA[i]]
        zn2 = int(zn / 10)
        zn1 = zn % 10
        itog += adv[zn2]+ adv[zn1] #ищем позиции по ADFGVX

    print(' ')
    matr2 = []
    matr1 = []
    jj = 0
    print('зашифрованное сообщение:')
    print(itog)
    print(' ')

    kol = (len(kluch)) * (len(kluch)) #последовательность делится на блоки длины kluc^2
    while jj < len(itog):
        newstr += help(kluch, itog[jj: jj + kol], posl)
        jj += kol

    print("шифр:")
    print(newstr)

    file2 = open('shifr.txt', 'w')
    file2.write(newstr)
    file2.close()


def deshifr():

    print('')
    print('=== дешифровка ===')

    file3 = open('key.txt', 'r')
    kluch = file3.read()
    kluch = kluch.lower()
    i = 0
    kl = ''

    while i < len(kluch):
      if b.find(kluch[i]) == -1:
         kluch = kluch.replace(kluch[i],'')
      else:
         if kl.find(kluch[i]) == -1:
             kl += kluch[i]
         i += 1

    print('')
    print('ключ для дешифровки:')
    print(kl)
    print('')
    kluch = kl

    file1 = open('shifr.txt', 'r')
    STROKA = file1.read()

    # ДЕШИФРОВКА

    i = 0
    num = 0
    matr2 = []
    matr1 = []
    posl = ''

    for i in reversed(range(len(kluch))):
       for j in range(1, i + 1):
           if kluch[j - 1] > kluch[j]:
                a = [kluch[0:j - 1],kluch[j],kluch[j - 1],kluch[j + 1:]]
                kluch = ''.join(a)
                posl = str(j - 1) + str(j) + posl

    print('последовательность дешифровки:')

    i = 0
    jj = 0
    newstr = ''
    itog = ''

    kol = (len(kluch)) * (len(kluch))
    while jj < len(STROKA):
        newstr += help1(kluch, STROKA[jj: jj + kol], posl)
        jj +=kol
    i = 0

    while i < len(newstr) - 1:
        itog += matr[adv.find(newstr[i])][adv.find(newstr[i + 1])]
        i+=2

    newstr = ''
    file2 = open('deshifr.txt', 'w')
    i = 0

    print('')
    print('расшифрованное сообщение:')
    print(itog)
    file2.write(itog)

    file2.close()

print ('')
if int(input("Для шифрования введите 1, для дешифрования - 0 \n")) == 1:
    shifr()
else:
    deshifr()
