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

ii=0
jj=0

count = len(str)

for i in range (count):
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
      
count = len(a)

for i in range (count):
  if ii > 4:
      matr.append(matr1)
      matr1 = []
      ii = 0
      jj += 1
  matr1.append(a[0])
  dict[a[0]] = ii * 10+ jj
  a = a.replace(a[0],'')
  ii += 1

matr.append(matr1)
file1 = open('message.txt', 'r')
print(matr)
print(" ")

messages = file1.read()
messages = messages.lower()
messages = messages.replace('j','i')
i = 0
num = 0

while i < len(messages):
  if b.find(messages[i])== -1:
    messages = messages.replace(messages[i],'')
  else:
      i+=1

newstr = ''
itog = ''

for i in range(len(messages)):

    zn = dict[messages[i]]
    zn2 = zn / 10
    zn1 = zn % 10
    num = i % 4

    if num == 0:
        newstr = matr[zn1-1][zn2]
    elif num == 1:
        if zn2 == 4: zn2 = -1
        newstr = matr[zn1][zn2+1]
    elif num == 2:
        if zn1 == 4: zn1 = -1
        newstr= matr[zn1+1][zn2]
    elif num == 3:
        newstr= matr[zn1][zn2-1]
    itog += newstr

print("result:")
print(itog)

file2 = open('itog.txt', 'w')
file2.write(itog)