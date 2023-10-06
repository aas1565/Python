a,b =map(str,input().split())

c=0

for i in a:
    if (i==b):
        c+=1
    elif (c==0):
        print(0)
        break
    else:
        print(c)
        break