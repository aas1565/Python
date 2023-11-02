def searchNum():
    num=25
    while True:
        new_num = len(str(num))
        res = 0
        b = num
        while b > 0:
            a = b % 10
            res = res + (a ** new_num)
            b = b // 10
            if res == num and b<=0:
                yield res
        num += 1

armstrong = searchNum()
for i in range(8):
    print(next(armstrong), end=' ')
