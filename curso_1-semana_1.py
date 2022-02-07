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


#######################
# DESCOBRINDO O NUMPY #
#######################
# Importar bibliotecas
import numpy as np
import math

# Criar de array unidimensional com integers
a = np.array([1, 2, 3])
print(a)

# Criar de array multidimensional com integers
b = np.array([[1, 2, 3], [4, 5, 6]])
b

# Imprimir o comprimento de cada dimensão chamando o atributo shape, que retorna uma tupla,
#   e também podemos verificar o tipo de itens no array.
b.shape #verifica o comprimento
a.dtype #verifica o tipo

# Criar de array unidimensional com floats
c = np.array([2.2, 5, 1.1])
print(c)

# Criar array com 0, 1 e números aleatórios
d = np.zeros([2, 3])
print(d)

e = np.ones([2, 3])
print(e)

np.random.rands(2, 3)

# Criar array com uma "ordem"
#   Neste caso, o primeiro argumento é o limite inicial e o segundo argumento é o limite final e o terceiro argumento é a diferença entre cada número consecutivo.
f = np.arange(10, 50, 2)
f

# Criar array com floats e uma ordem
#   Neste caso,o terceiro argumento não é a diferença entre dois números, mas é o número total de itens que você deseja gerar.
np.linspace(0, 2, 15) #15 sendo do 0 (incluso) a 2 (incluso)


# Operações matemáticas com arrays
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

c = a - b #subtração de arrays
print(c)

d = a * b #multiplicação de arrays
print(d)


# Indexação
# de array unidimensional
a = np.array([1, 3, 5, 7])
a[2]

# de array multidimensional
#   insere-se o índice, que é composto por dois inteiros. O primeiro é referente a linha e o segundo a coluna.
b = np.array([[1, 2], [3, 4], [5, 6]])
b[1, 1]

# mostrar múltiplos números
print(b[[0, 1, 2], [0, 1, 1]])


# Boolean
print(b > 5) # esse comando irá retornar um array de verdadeiros e falsos dependendo se a condição foi "alcançada".


# Slicing
c = np.array([0, 1, 2, 3, 4, 5])
print(a[:3]) # pegar os três primeiros elementos



#######################
# DESCOBRINDO O NUMPY #
#######################
# Importar bibliotecas
import re

# Exemplo 1
text = "This is a good day."

if re.search("good", text):
    print("Wonderful")
else:
    print("Alas :(")
    
# Exemplo 2
text = "Amy works diligently. Amy gets good grades. Our student Amy is successful."

re.split("Amy", text)
re.findall("Amy", text)

# Exemplo 3
text = "Amy works diligently. Amy gets good grades. Our student Amy is successful."

re.search("^Amy", text)
