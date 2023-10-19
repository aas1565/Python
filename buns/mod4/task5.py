a=input()

dic={}

for letter in a:
    if letter in dic:
        dic[letter]+=1
    elif(letter==' '):
        continue
    else:
        dic[letter]=1

sorted_dict = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))

for key, value in sorted_dict.items():
    print(key, value)