file = open('text.txt','r')
data = file.read()
str1 = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
dict = {}

kolvo = 0

for line in data:
	for i in line:
		if str1.find(i)>-1:
			kolvo += 1
			if i in dict:
				dict[i] += 1
			else:
				dict[i] = 1

n = max(dict.values())
a = []
for i in dict:
    a.append([round(dict[i]/kolvo, 3),i])

a = sorted(a, reverse = True)
print(a)
file1 = open('itog.txt','w')
[file1.write(i[1] + ' ' + '=' + ' ' + str(i[0]) + '\n') for i in a]
file1.close()

