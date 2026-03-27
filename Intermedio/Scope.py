### Scope ###
'''
x  = 10
def mostrar():
    print(x)
mostrar() 
'''

### Scope Local ###
'''def saludar():
    mensaje = 'Hola Mundo'
    print(mensaje)

saludar()'''

### Scope Local errado ###
'''def saludar ():
    mensaje = "Hola mundo"
    
saludar()'''

### Scope Global ###


contador = 0

def aumentar():
    global contador
    contador += 1
aumentar()
print(contador)
















