a=str(input())

gl="а е ё и о у ы э ю я"
sg="б в г д ж з к л м н п р с т ф х ц ч ш щ"
a=a.replace(' ', '')
v=0
w=0

for i in a:
    if (i in gl):
        v+=1
    else:
        w+=1
print(v, w)
