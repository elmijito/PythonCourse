'''

a = 2550;
b = a * 10;
c = a * 10 + 5;
# print (a,b,c); esta linea es comentada con ctrl + k + c

if a < c:
    print("a es menor que c")
else:
    print("a no es menor que c");


# varieble de tipo entero
entero = 10;
print(entero);

#Variable de tipo cadena 
cadena = "Hola, soy una cadena de texto";
#print(cadena);

#Variable de tipo flotante
flotante = 3.1416;
print (flotante);

#Variable de tiepo booleano
booleano = True;# Variable de tipo entero
booleano2 = False

print (booleano, booleano2)

#Variable de tipo lista
lista = [1, 2, 20 ,50]
print(lista)

#Variable de tipo tupla
tupla = (1, 2, 20 ,50)

#variable de tipo diccionario
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

print(diccionario)
'''

#Listas
#lista = [1, 2, 3, 4, 5,'Hola mijitos', 3,1416, False, 'H']
#print(lista)

Lista_musica = ['Rock', 'Pop', 'Jazz', 'Reggae','Regeaton', 'Salsa Rosa', 'Merengue']
Lista_musica.append('Trap')
#print(Lista_musica)

#print(Lista_musica[7])  # Imprime el primer elemento de la lista

# 0 -- Rock
# 1 -- Pop
# 2 -- Jazz

#Tuplas 

coordenadas = (10, 100)
print(coordenadas[0])  # Imprime el primer elemento de la tupla

#ROADMAP.SH
#BOOKS.GOALKICKER.COM

def division(a,b):
   return (a // b, a % b)
    
    
cociente, resta = division(10, 100)
print(cociente, resta)


