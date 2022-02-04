# Funcao 1 -
def add_numbers(x, y, z):
    return x + y + z

print(add_numbers(1, 2, 3))

# Funcao 2 - Conditional
def do_math(a, b, kind):
    if (kind == 'add'):
        return a + b
    else:
        return a - b

do_math(1, 2, kind = 'add')

# Funcao 3 - Separacao de nomes
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()

list(map(split_title_and_name, people))

# OU

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

list(map(split_title_and_name, people))
