file = open('text.txt', 'r')
str1 = file.read()

a = str1.split()
a = [int(x) for x in a]

matr = []
kol = 0
check = False
null = 0
ed = 1
type = True

while a != []:
    matr1 = a[:9]
    matr.append(matr1)
    a = a[9:]
    kol += 1

def add(matr1, matr2): # сложение по модулю 2
        matr3 = []
        for i in range(len(matr1)):
            matr3.append((matr1[i] + matr2[i]) % 2)
        return matr3

def mul(matr1, matr2):
    matr3 = []
    for j in range(3):
        for i in range(3):
            matr11 = matr1[3 * j:][:3]
            matr22 = matr2[i::3]
            s = 0
            for i in range(len(matr22)):
                      s += (matr11[i] * matr22[i])
            matr3.append(s % 2)
    return matr3

for i in range(kol): # нахождение нулевой матрицы (при сложении получается нулевая)
    for j in range(kol):
        if add(matr[j],matr[i]) == matr[j]:
            check = True
            print('Нулевой элемент найден: ')
            q = matr[j]
            print(q[0],q[1], q[2])
            print(q[3],q[4],q[5])
            print(q[6],q[7], q[8])
            null = q
            break
if not(check):
     print('Нулевой элемент не найден')
     type = False
if 1 > 0:
    check = False # нахождение единичного элемента (при умножении на себя дает себя)
    for i in range(kol):
        for j in range(kol):
            if mul(matr[j], matr[i]) == matr[j] and matr[j] != null:
                check = True
                print('Единичный элемент найден: ')
                q = matr[i]
                print(q[0],q[1],q[2])
                print(q[3],q[4],q[5])
                print(q[6],q[7],q[8])
                ed = q
                break
    if not(check):
        print('Единичный элемент не найден')
        type = False

if 1 > 0:
    check = False # проверка коммутативности
    # a + b = b + a?
    for i in range(kol):
        for j in range(kol):
            if add(matr[j], matr[i]) != add(matr[i], matr[j]):
                check = True
                break
    if check:
        print('Коммутативность сложения не выполняется')
        type = False
    else:
        print('Коммутативность сложения выполняется')

    h = 0 # определения противоположных элементов
    # если сумма 2х элементов равна нулевому элементу
    for i in range(kol):
        check = False
        if matr[i] != null:
            for j in range(kol):
                if add(matr[j], matr[i]) == null:
                    check = True
                    break
            if not(check):
                print('Противоположные элементы не найдены')
                print(matr[i])
                h = 1
                type = False
    if h != 1:
        print('Противоположные элементы существуют')

    # определение существования обратного элемента для всех остальных элементов
    if ed != 1: # если есть единичный элемент
        s = 0
        for i in range(kol):
            if matr[i] != null:
                check = False
                for j in range(kol):
                    if mul(matr[i], matr[j]) == ed: # если произведение двух элементов дает единичный элемент
                        check = True
                        break
                if not(check):
                    print('Не найдены обратные элементы для некотрого элемента')
                    print(matr[i])
                    s = 1
                    type = False
        if s != 1:
            print('Обратные элементы найдены')
        else:
            print('Не для всех элементов найдены обратные')
            type = False
    else:
     print('Единичного элемента не существует, невозможно найти обратные элементы')
     type = False

check = False # нахождение ассоциативности сложения
# (a + b) + c = a + (b + c)?
for i in range(kol):
    for j in range(kol):
        for k in range(kol):
            if add(add(matr[i], matr[j]), matr[k]) != add(matr[i], add(matr[j], matr[k])):
                check = True
                break
if check:
    print('Ассоциативность сложения не выполняется')
    type = False
else:
    print('Ассоциативность сложения выполняется')

check = False # нахождение коммутативности умножения
# ab = ba?
for i in range(kol):
    for j in range(kol):
        if mul(matr[j], matr[i]) != mul(matr[i], matr[j]):
            check = True
            break
if check:
    print('Коммутативность умножения не выполняется')
    type = False
else:
    print('Коммутативность умножения выполняется')

check = False # определение ассоциативности умножения
# (a * b) * c = a * (b * c)?
for i in range(kol):
    for j in range(kol):
        for k in range(kol):
            if mul(mul(matr[i], matr[j]), matr[k]) != mul(matr[i], mul(matr[j], matr[k])):
                check = True
                break
if check:
    print('Ассоциативность умножения не выполняется')
    type = False
else:
    print('Ассоциативность умножения выполняется')

check = False # определение дистрибутивности умножения относительно сложения
# (a + b) * c = a * c + b * c?
for i in range(kol):
    for j in range(kol):
        for k in range(kol):
            if mul(add(matr[i],matr[j]),matr[k]) != add(mul(matr[i],matr[k]),mul(matr[j],matr[k])):
                check = True
                break
if check:
    print('Дистрибутивность умножения относительно сложения не выполняется')
    type = False
else:
    print('Дистрибутивность умножения относительно сложения выполняется')

if type:
    for i in matr:
        w = []
        for j in range(2):
            w = add(i, i)
        if w == i:
            print('Является полем характеристики 2')
            exit(0)
        else:
            print('Не является полем характеристики 2')
            exit(0)
else:
    print('Не является полем')