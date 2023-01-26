import os

ls = [i for i in os.listdir() if i.endswith('.txt')]
ls1 = {}
ls2 = {}

for j in ls:
    name_file = j
    file = open((j), encoding='utf-8').readlines()
    len_file = len(file)
    ls1[name_file] = len_file
    ls2[name_file] = file

sorted_dict = {}
sorted_keys = sorted(ls1, key=ls1.get)
for w in sorted_keys:
    sorted_dict[w] = ls1[w]

with open('result.txt','w', encoding='utf-8') as f:
    for key in sorted_dict.keys():
        for i in ls2[key]:
            text = i.strip()
            f.write(f'{key}, \n'
                    f'{ls1[key]}, \n'
                    f'{text}, \n')