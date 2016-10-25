N = int(input())
file = open('input.txt')
s = file.read().split('\n')
tng = []
o = {}
for i in range(N):
    tng.append(input())
for i in tng:
    for j in s:
        if i in j.split(':')[1].split():
            o[j] = i
res = []
for i in o:
    res.append(i.split(' : '))
for i in res:
    print(i[0], ':', i[1])
