a, b = input().split()

d=str(a)
c=int(b)

num= ord(d)

res1= num+c
if (res1> ord('z')):
    res1-=26
res2=num-c
if(res2 < ord('a')):
    res2+=26

result1=chr(res1)
result2=chr(res2)


print(result1, result2)