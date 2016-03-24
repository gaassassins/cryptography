file = open('code.txt', 'r')

str = file.read()
str = str.lower()

b = ''
dict = {}
matr = []
matr1 = []

for i in range(97,123):
    b += (chr(i))
a = b.replace('j','')
print("alphabet is: " + a)

ii=0
jj=0
kol = len(str)

#записывается ключ и алфавит в строчку
for i in range (kol):
  if ii > 4:
      matr.append(matr1)
      matr1 = []
      ii = 0
      jj+=1
  if a.find(str[i])!=-1:
      matr1.append(str[i])
      dict[str[i]] = ii * 10 + jj
      a = a.replace(str[i],'')
      ii+=1
kol = len(a)

#элементы записываются в матрицу 5х5
for i in range (kol):
  if ii > 4:
      matr.append(matr1)
      matr1 = [] #каждая новая строка
      ii = 0
      jj+=1
  matr1.append(a[0])
  dict[a[0]] = ii * 10 + jj
  a = a.replace(a[0],'') #проверется алфавит
  ii+=1
matr.append(matr1)


def shifr():
    file1 = open('message.txt', 'r')
    for i in range(5):
        for j in range(5):
            print(matr[i][j], end = '')
        print() # на экран печатаем нашу оригинальную матрицу

    STROKA = file1.read() #сообщение, которое надо зашифровать
    STROKA = STROKA.lower()
    STROKA = STROKA.replace('j','i')
    i = 0

    while i <len(STROKA): #считаем, сколько символов в сообщении
       if b.find(STROKA[i])== -1:
            STROKA = STROKA.replace(STROKA[i],'') #наша строчка в message
       else:
            i+=1

    i = 0 #записывается количество букв избегая пробелов
    newstr = ''

    while i < len(STROKA): #биграммы добавляются в словарь
        zn1 = int(dict[STROKA[i]])
        zn2 = 0

        if i+1 < len(STROKA):
            zn2 = int(dict[STROKA[i+1]])

        zn12 = int(zn1 / 10) #выделяются индесы у элементов биграммы
        zn11 = zn1 % 10
        zn22 = int(zn2 / 10)
        zn21 = zn2 % 10

        if zn11 == zn21 and zn12 == zn22:  #если два символа биграммы совпадают

            if STROKA[i+1] == 'x': #вставляем вместо повторяющегося символа х.
                zn2  = int(dict['х'])
                zn22 = int(zn2 / 10)
                zn21 = zn2 % 10

            if STROKA[i+1] != 'x': #если остался символ пустой без пары, к нему добавляется х.
                zn2  = int(dict['x'])
                zn22 = int(zn2 / 10)
                zn21 = zn2 % 10
            i-=1

        if zn11 == zn21: #если символы биграммы исходного текста встречаются в одной строке.

          if zn12 == 4: zn12 = -1 #символы замещаются на символы, расположенные в ближайших столбцах справа
                                  #от соответствующих символов.
          if zn22 == 4: zn22 = -1
          newstr += matr[zn11][zn12 + 1]
          newstr += matr[zn21][zn22 + 1]

        elif zn12 == zn22: #если символы биграммы исходного текста встречаются в одном столбце,
                           #то они преобразуются в символы того же столбца, находящиеся непосредственно под ними.
          if zn11 == 4: zn11 = -1
          if zn21 == 4: zn21 = -1
          newstr += matr[zn11+1][zn12]
          newstr += matr[zn21+1][zn22]

        else: #если символы биграммы исходного текста находятся в разных столбцах и разных строках,
              #то они заменяются на символы, находящиеся в тех же строках, но соответствующие другим углам прямоугольника.
          newstr += matr[zn11][zn22]
          newstr += matr[zn21][zn12]
        i+=2


    file2 = open('itog.txt', 'w')
    file2.write(newstr)
    print('\n')
    print(newstr)
    file2.close()



def deshifr():
    file1 = open('itog.txt', 'r')
    for i in range(5):
        for j in range(5):
            print(matr[i][j], end = '')
        print()

    STROKA = file1.read() #сообщение, которое надо зашифровать
    print('')
    print(STROKA)
    print('')
    STROKA = STROKA.lower()
    STROKA = STROKA.replace('j','i')
    i = 0

    while i <len(STROKA): #считываем, сколько символов в сообщении
       if b.find(STROKA[i])== -1:
            STROKA = STROKA.replace(STROKA[i],'') #смотрим на повтояющиеся элементы
       else:
            i+=1

    i = 0
    newstr = ''

    while i <len(STROKA): #биграммы добавляются в словарь и их соотв.индексы
        zn1 = int(dict[STROKA[i]])
        zn2 = int(dict[STROKA[i+1]])
        zn12 = int(zn1 / 10)
        zn11 = zn1 % 10
        zn22 = int(zn2 / 10)
        zn21 = zn2 % 10

        if zn11 == zn21: #если символы биграммы исходного текста встречаются в одной строке.

          if zn12 == 4: zn12 = -1 #символы замещаются на символы, расположенные в ближайших столбцах справа
                                  #от соответствующих символов.
          if zn22 == 4: zn22 = -1
          newstr += matr[zn11][zn12 - 1]
          newstr += matr[zn21][zn22 - 1]

        elif zn12 == zn22:  #если символы биграммы исходного текста встречаются в одном столбце,
                            #то они преобразуются в символы того же столбца, находящиеся непосредственно под ними.
          if zn11 == 4: zn11 = -1
          if zn21 == 4: zn21 = -1
          newstr += matr[zn11-1][zn12]
          newstr += matr[zn21-1][zn22]

        else: #если символы биграммы исходного текста находятся в разных столбцах и разных строках,
              #то они заменяются на символы, находящиеся в тех же строках, но соответствующие другим углам прямоугольника.
          newstr += matr[zn11][zn22]
          newstr += matr[zn21][zn12]
        i+=2
    i = 1

    itog = newstr[0]
    print(newstr)

    while i < len(newstr) -1:
        itog += newstr[i]
        i+=1
    itog += newstr[-1]
    newstr = itog

    file2 = open('message.txt', 'w')
    file2.write(newstr)
    file2.close()

if int(input("For shift press 1\nFor deshifr press 0 \n")) == 1:
    print('')
    print('cipher result matrx')
    shifr()

else:
    print('')
    print('deshifr result matrx')
    deshifr()