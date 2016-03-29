file = open('text.txt','r')
stroka = file.read()
str = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
dict = {}

for line in stroka:
    for i in line:
        if str.find(i) > -1:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 0
l = lambda x: x[1]
print(sorted(dict.items(), key=l, reverse = True))
