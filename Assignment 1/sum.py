sum = 0
lst = []

while 1:
    a = int(input())
    if a == -1:
        break
    lst.append(a)
    sum = sum + a

for i in lst:
    print(i)
print("Sum = ", sum)