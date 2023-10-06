a=str(input())


def func(n):
    c = ''
    n=n.replace(' ', '')
    for i in n:
        if (i in c):
            return True
        else:
            c=c+''+i
    else:
        return False

b=func(a)
print(b)
