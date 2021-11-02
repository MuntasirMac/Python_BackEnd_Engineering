lst = []
dct = {}

while 1:
    a = input()
    if a == "STOP":
        break
    lst.append(int(a))

for i in lst:
    if i not in dct:
        dct[i] = 1
    else:
        dct[i] += 1
    
# print(dct.keys() - dct.values(), " times")
for key in dct:
    print(key, "-", dct[key], "times")