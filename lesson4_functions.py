x = 5
def func_name():
    x = 10
    return x
print(x)

x = func_name()
print(func_name())

def param_func(a, b, c):
    param_sum = a + b + c
    return param_sum

x = 10
param_sum = param_func(x, 10, 3)
print(param_sum)

y = 15
param_sum = param_func(str(x), 'hi', '3')
print(param_sum)

def default(a=5, b=10):
    param_sum = a + b
    return param_sum
print(default(b=1))

def arbitrary(*args):
    print(args)
    return sum(args)
print(arbitrary(1,2))

def keyword(a=0, b=0):
    return a + b
print(keyword(a=5, b=10))

def arb_keyword(**kwargs):
    print((kwargs))
    for key, value in kwargs.items():
        print(value)

arb_keyword(a=10, b=35, foo='hi')

