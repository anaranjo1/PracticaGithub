#PRÁCTICA GIT:
# Joan Bril, Andrés Naranjo

import numpy as np

np.random.seed(4)

x = np.random.randint(10)
y = np.random.randint(10)
z = np.random.randint(10)
suma = (x+y)+z

print("'x' es igual a: " + str(x) + "\n'y' es igual a: " + str(y) + "\n'z' es igual a: " + str(z))
print("La suma total de estos números es: " + str(suma))