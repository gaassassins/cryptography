# чтение ключа
file = open('key.txt', 'r')
str2 = file.read()
str2 = str2.lower()

# класс, который помогает считывать в строке каждый элемент
class SomeObject(object):
    def __init__(self, name):
       self.name = name

    def __str__(self):
       return '%s' % self.name


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя!.,?-:;"()0123456789'
b = SomeObject(alphabet)
strr = ''

# добавление ключа в алфавит "alphabet"
for i in range(len(str2)):
    if alphabet.find(str2[i]) != -1 and strr.find(str2[i]) == -1:
        strr += str(SomeObject(str2[i])) # если у нас символ находится в алфавите, то добавляем его в результ-строку
for i in range(len(alphabet)):
    if strr.find(alphabet[i]) == -1:
        strr += str(SomeObject(alphabet[i]))

# показываем всем наш алфавит
print(" ")
alphabet = strr
print(strr)

# процедура шифрования
def Atbash(file, file1):
    for line in file: # для каждой строчки в сообщении для шифровки/дешифровки
        for i in range(len(line)): # по длине строки
            pos = strr.find(line[i]) # добавляем позицию символа в переменную
            if pos > -1: #если этот символ существует в алфавите, то тогда
                         #меняем i-символ на (n - i + 1)-символ
                file1.write(strr[len(strr) - pos - 1]) # записываем результат в файл
            else:
                file1.write(line[i])
                print(line[i])


print('шифрование или дешифрование?')
s = str(input())
s = s.lower()

if s == 'ш':
    file = open('message_shifr.txt', 'r')
    file1 = open('shifr.txt', 'w')
    Atbash(file,file1)

elif s == 'д':
    file = open('message_deshifr.txt', 'r')
    file1 = open('deshifr.txt', 'w')
    Atbash(file,file1)