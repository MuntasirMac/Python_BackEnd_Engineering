r,c = map(int,input().split(','))

#print(r, c)

for i in range(r):
    for j in range(c):
        print(j+1, end='')
    print("\n")