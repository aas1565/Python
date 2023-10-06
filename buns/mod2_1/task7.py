a=str(input())

one=0
zero=0

for i in a:
    if (i=="1"):
        one+=1
    else:
        zero+=1
if (one==zero):
    print("yes")
else:
    print("no")