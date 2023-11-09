def memoize(func):
    dict = {}
    def wrapper(*args, **kwargs):
        if args in dict:
            return dict[args]
        else:
            result=func(*args)
            dict[args]=result
            return result
    return wrapper
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

res=fibonacci(6)
print(res)

res=fibonacci(6)
print(res)

