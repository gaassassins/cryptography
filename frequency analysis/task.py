import simplejson
file = open('text.txt','r')
stroka = file.read()
str = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
dict = {}
stroka = stroka.lower()
for line in stroka:
    for i in line:
        if str.find(i) > -1:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 0

l = lambda x: x[1]
ans = sorted(dict.items(), key=l, reverse = True)
print(ans)
f = open('itog.txt', 'w')
simplejson.dump(ans, f, ensure_ascii = False)
f.close()

