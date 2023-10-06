a,b,c =map(int,input().split())

if (a>=b and a>=c):
    if (b>=c):
        print(b)
    else:
        print(c)
elif (b>=c and b>=a):
    if (a>=c):
        print(a)
    else:
        print(c)
else:
    if (c>=a and c>=b):
        if(b>=a):
            print(b)
        else:
            print(a)





