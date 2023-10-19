a=input().split()

uniq=set(a)

if (len(uniq)==len(a)):
    print("Все числа разные")
elif (len(uniq)==1):
    print("все числа равны")
else:
    print("есть одинаковые и разные")