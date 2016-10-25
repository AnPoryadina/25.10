import string
A = []
with open('en-ru.txt', 'r') as dic:
    for i in dic:
        A.append(i.rstrip())
B = []
with open('input.txt', 'r') as text:
    for i in text:
        B.append(i)

en = []
ru = []
for i in range(len(A)):
    A[i] = A[i].split('\t-\t')
    en.append(A[i][0])
    ru.append(A[i][1])
ru_en = {en: ru for ru, en in zip(ru, en)}

def ruen(A):
    p = set(string.punctuation)
    sp = ''.join(x for x in A if x not in p)
    s = sp.lower().split(' ')
    for i in range(len(s)):
        if s[i] in ru_en:
            s[i] = ru_en[s[i]]
    return ' '.join(s)
for i in range(len(B)):
    print(B[i])
    print(ruen(B[i]))
