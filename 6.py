dic = dict()
s1 = open('en_ru2.txt')
s2 = open('output.txt', 'w')
s = s1.readline().rstrip()
while len(s) > 0:
    en_trans, ru_trans = list(s.split('\t-\t'))
    if ',' in ru_trans:
        for i in ru_trans.split(','):
            i = i.lstrip()
            if i in dic:
                dic[i] = dic[i]+', '+en_trans
            else:
                dic[i] = en_trans
    else:
        if ru_trans in dic:
            dic[ru_trans] = dic[ru_trans]+', '+en_trans
        else:
            dic[ru_trans] = en_trans

    s = s1.readline().rstrip()

key_sort = sorted(dict.keys())
for i in key_sort:
    print('\t-\t'.join((i, dict[i])), file=s2)
