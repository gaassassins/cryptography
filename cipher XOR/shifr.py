import math
global alphabet

alphabet ='абвгдеёжзиклмнопрстуфхцчшщыъьэюя0123456789.,:;!?abcfvyuiopqwerzm'
kol = len(alphabet)

l = math.ceil(math.log(kol)/math.log(2))

def repl(keytxt, messagetxt):
    stroka_key = keytxt.read()
    stroka_key = stroka_key.lower()
    stroka_messages = messagetxt.read()
    stroka_messages = stroka_messages.lower()

    for i in stroka_key:
        if alphabet.find(i) == -1:
             stroka_key = stroka_key.replace(i,'')

    for i in stroka_messages:
        if alphabet.find(i) == -1:
             stroka_messages = stroka_messages.replace(i,'')
    return stroka_key, stroka_messages

def to_value_(a):
    return alphabet[int(a,2)]

def to_str_(a, alphabet):
    kol = len(alphabet)
    l = math.ceil(math.log(kol)/math.log(2))
    pos = bin(alphabet.find(a))
    pos = pos[2:]

    res = ''
    for i in range(l):
       if pos!='':
          res += pos[0]
          pos = pos[1:]
       else:
          res = '0' + res
    return res

def xor(a, b):
    return (a + b) % 2


def xor_str(a,b):
    res = ''
    for i in range(len(a)):
        res += str (xor(int(a[i]),int(b[i])))
    return res 

def str_to_bin(stroka_key, alphabet):
    res = ''
    for i in stroka_key:
        res += to_str_(i, alphabet)
    return res 

def shifr(keytxt, messagetxt, file_out):
    stroka_key, stroka_messages = repl(keytxt, messagetxt)
    bin_kl = (str_to_bin(stroka_key, alphabet))
    print('\n' + 'key = ' + bin_kl)
    bin_mes = (str_to_bin(stroka_messages, alphabet))
    print('\n' + 'messages = ' + bin_mes)

    if len(bin_kl) < len(bin_mes):
         kol = len(bin_kl) - 1
         start = 0
         while len(bin_kl) < len(bin_mes):
             val = xor_str(bin_kl[start], bin_kl[start+kol])
             start += 1
             bin_kl += val
    print('\n' + 'key now = ' + bin_kl)
    res = xor_str(bin_kl, bin_mes)
    itog = ''

    for i in range(len(stroka_messages)):
        itog += to_value_(res[:l] + '\n')
        res = res[l:]
    print('\n' + 'result = ' + itog )
    file_out.write(itog)
    file_out.close()

if int(input('1 - Rashifruy menya' + '\n')) == 1:
    keytxt = open('key.txt', 'r')
    messagetxt = open('message.txt', 'r')
    resulttxt = open('itog.txt', 'w')
    shifr(keytxt, messagetxt, resulttxt)
else:
    print()

# mes mother cod cat => mes = 011000 cod = 0010 , cod => 0010 first xor last => 00100 => first + 1 xor last =>  001000


