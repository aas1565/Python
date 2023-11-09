def validate_args(func):
    def wrapper(*args, **kwargs):
        if len(args) != 1:
            return "Too many arguments"

        arg = args[0]
        if not isinstance(arg, int):
            return "Wrong types"

        if arg < 0:
            return "Negative argument"

        return func(*args, **kwargs)
    return wrapper
@validate_args
def example_func(x):
    print("Argument is valid:", x)

result = example_func(5)
print(result)

result = example_func("hello")
print(result)

result = example_func(-2)
print(result)

result = example_func(1, 2)
print(result)
