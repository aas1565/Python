def evcl (a, b):
    if a==0:
        return b
    elif (b==0):
        return a
    else:
        return evcl(b, a%b)

a=int(input())
b=int(input())

if (a>=b):
    res= evcl(a, b)
elif (a<=b):
    res= evcl(b, a)
    
print(res)