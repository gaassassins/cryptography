import math
global alphabet

alphabet ='абвгдеёжзиклмнопрстуфхцчшщыъьэюя0123456789.,:;!?abcfvyuiopqwerzm'
kol = len(alphabet)

l = math.ceil(math.log(kol)/math.log(2)) # мат.операция выделения логарифма
                                         # из 8 получается длинна 3 сообщения 2^3 = 8

def repl(keytxt, messagetxt):
    stroka_key = keytxt.read() #считываем ключ и сообщение из файлов
    stroka_key = stroka_key.lower()
    stroka_messages = messagetxt.read()
    stroka_messages = stroka_messages.lower() #преобразуем заглавные в строчные

    for i in stroka_key: #заменяем i на пустой символ
        if alphabet.find(i) == -1:
             stroka_key = stroka_key.replace(i,'')

    for i in stroka_messages: #заменяем i на пустой символ
        if alphabet.find(i) == -1:
             stroka_messages = stroka_messages.replace(i,'')
    return stroka_key, stroka_messages

def to_value_(a): #функция, которая в двоичном формате число 11, например, переводит в 3
    return alphabet[int(a,2)]

def to_str_(a, alphabet): #функция, которая выводит целое слово в двоичном формате
    kol = len(alphabet)  #берем длинну алфавита
    l = math.ceil(math.log(kol)/math.log(2)) #если длинна алфавита 64, то l = 6. максимальное число 111111 мин 000000
    pos = bin(alphabet.find(a)) #возвращает позицию символа из алфавита в двоичный формат
    pos = pos[2:] #чистит число

    res = '' #заводим переменную под результат
    for i in range(l):
       if pos!='':
          res += pos[0]
          pos = pos[1:]
       else:
          res = '0' + res #добавление значащих нулей, если они нужны перед числом
    return res

def xor(a, b): #операция ксора, сложение по модулю два
    return (a + b) % 2


def xor_str(a,b): #функция, которая берет каждый символ из одной строки и делает ксор с другим символом из другой строки
    res = ''
    for i in range(len(a)):
        res += str (xor(int(a[i]),int(b[i])))
    return res 

def str_to_bin(stroka_key, alphabet): #функци, которая получает для ключа его бинарную последовательность символов
    res = ''
    for i in stroka_key:
        res += to_str_(i, alphabet)
    return res 

def shifr(keytxt, messagetxt, file_out):
    stroka_key, stroka_messages = repl(keytxt, messagetxt) #считываем ключ и сообщение
    bin_kl = (str_to_bin(stroka_key, alphabet)) #переводим ключ в бин последоватльность символов
    print('\n' + 'key = ' + bin_kl)
    bin_mes = (str_to_bin(stroka_messages, alphabet)) #переводим строку в бин последовательность симовлов
    print('\n' + 'messages = ' + bin_mes)

#если длинна ключа будет меньше длинны сообщения
    if len(bin_kl) < len(bin_mes):
         kol = len(bin_kl) - 1 #мы берем от длинны предпоследний элемент за кол-во
         start = 0 #ставим счетчик
         while len(bin_kl) < len(bin_mes): #и до тех пор, пока длинна ключа не станет равной длинне сообщения
             val = xor_str(bin_kl[start], bin_kl[start+kol]) #мы ксорим первый элемент из ключа с его последним элементом
             start += 1 #и далее двигаемся в правую сторону, пока количество символов не совпадет с кол-вом символов в сообщении
             bin_kl += val
    print('\n' + 'key now = ' + bin_kl)
    res = xor_str(bin_kl, bin_mes) #если количество символов одинаковое, делаем ксор бин последовательностей ключа и сообщения
    itog = ''

    for i in range(len(stroka_messages)): #все преобазуется в строковые данные и добавляется в итог
        itog += to_value_(res[:l])
        res = res[l:]
    print('\n' + 'result = ' + itog)
    file_out.write(itog)
    file_out.close()

if int(input('1 - shifr, 0 - deshifr' + '\n')) == 1:
    keytxt = open('key.txt', 'r')
    messagetxt = open('message.txt', 'r')
    resulttxt = open('itog.txt', 'w')
    shifr(keytxt, messagetxt, resulttxt)
else:
    keytxt = open('key.txt', 'r')
    resulttxt = open('message.txt', 'w')
    messagetxt = open('itog.txt', 'r')
    shifr(keytxt, messagetxt, resulttxt)


# mes mother cod cat => mes = 011000 cod = 0010 , cod => 0010 first xor last => 00100 => first + 1 xor last =>  001000


