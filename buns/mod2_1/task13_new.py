def sum_even_odd_digits(number):
    ch = 0
    nch = 0
    position = 1

    while number > 0:
        digit = number % 10
        if position % 2 == 0:
            ch += digit
        else:
            nch += digit
        number //= 10
        position += 1

    return ch, nch


number = int(input())
ch, nch = sum_even_odd_digits(number)

result=nch+ch*3
if (result%10==0):
    print("yes")
else:
    print("no")