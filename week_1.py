# Function one
def add_numbers(x, y, z):
    return x+y+z

print(add_numbers(1, 2, 3))

# Function two
def do_math(a, b, kind):
    if (kind == 'add'):
        return a + b
    else:
        return a - b

do_math(1, 2, kind = 'add')
