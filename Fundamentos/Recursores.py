'''def contador(n):
    if n <= 0:
        print("Hecho!")
    else:
        print(n)
        contador(n - 1)

contador(5)


def factoria(n):
    #Caso base
    if n == 0 or n == 1:
        return 1
    #Caso recursivo
    else:
        return n * factoria (n - 1)
    
print (factoria(5))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1)) + fibonacci (n - 2)
print (fibonacci(7))'''


#Recursividad con listas
'''def sum_list(numeros):
    if len(numeros) == 0:
        return 0
    else:
        return numeros [0] + sum_list (numeros[1:])
    
mi_lista = [1,2,3,4,5]
print(sum_list(mi_lista))'''

#Recursividad con limites

import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
