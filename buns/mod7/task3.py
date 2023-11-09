import time
start=0
end=0
def timer(func):
    def wrapper(*args, **kwargs):
        global start
        start = time.time()
        result = func(*args, **kwargs)
        global end
        end = time.time()
        return result
    return wrapper

def validate_args(func):
    def wrapper(*args, **kwargs):
        if len(args) != 1:
            return "Слишком много аргументов"

        arg = args[0]
        if not isinstance(arg, int):
            return "Неверные типы"
        if arg < 0:
            return "Отрицательный аргумент"

        return func(*args, **kwargs)
    return wrapper

def memoize(func):
    dict = {}
    def wrapper(*args, **kwargs):
        if args in dict:
            return dict[args]
        else:
            result = func(*args, **kwargs)
            dict[args] = result
            return result
    return wrapper

@validate_args
@timer
@memoize
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n=7
for i in range(n):
    res=fibonacci(i)
print(res)
sum_time=end-start
print(sum_time)

n=7
for i in range(n):
    ress=fibonacci(i)
print(res)
sum_time=end-start
print(sum_time)

n=8
for i in range(n):
    res=fibonacci(i)
print(res)
sum_time=end-start
print(sum_time)

