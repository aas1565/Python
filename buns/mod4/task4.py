a=input()
dic={}
for letter in a:
    if (letter in dic):
        dic[letter]+=1
    else:
        dic[letter]=1

count=0
for i in dic.values():
    if (i%2!=0):
        count+=1
if count>1:
    print("не палиндром")

res=''
dif_letter=''

for letter, count in dic.items():
    if (count%2==1):
        dif_letter=letter
    res += letter*(count//2)
print(res+dif_letter+ res[::-1])