n=int(input())

m=n
for i in range (1, n+1):
    a = [ [i]*m  for i in range(1, n+1)]


for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
print()

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[j][i], end=' ')
    print()
