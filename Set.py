#set son colecciones de elementos únicos
#grupo = {"Rock","Tropipop","Pop","Jazz","Metal","Rock"}
#print(grupo) # {'Rock', 'Tropipop', 'Pop', 'Jazz', 'Metal'}

#numero = {1,2,3,4,5,6,7,8,9,10,2,3,5,8,10}
#print(numero)
#tipos de set mutables:
#a = set("Hola mijitos") #mutables, podemos añadir nuevos elementos
#a.add ("bendiciones para todos")# {'a', 'H', 'i', 'j', 'l',
#print(a)

#tipos de set inmutables:
'''b = frozenset("Hola mijitos")  #inmutables, no podemos añadir nuevos elementos
add.b ("bendiciones para todos")  # Esto causará un error porque frozenset es inmutable
print(b)  # frozenset({'a', 'H', 'i', 'j', 'l', 'm', 'o', 's', 't'})
'''
'''
#Intersección de los 
miSet = {7, 8, 9, 10}.intersection({5,6,7,8})
print(miSet)  # {8, 7} - Elementos comunes entre los dos sets
'''
'''
# Unión de los sets
miSet = {7, 8, 9, 10}.union({5, 6, 7, 8})
print(miSet)  # {5, 6, 7, 8,
'''

#miSet = {7, 8, 9, 10}.difference({5, 6, 7, 8})
#print(miSet)

#miSet = {7, 8, 9, 10}.symmetric_difference({5, 6, 7, 8})
#print(miSet)

#conjuntos y subconjuntos
set1 = {1,2,3}.issuperset({1,2,3}) #verificamos si el set1 es un superconjunto de {1,2,3}
#print(set1)  # True - set1 contiene todos los elementos de {1,2,3}

set2 = {1,2,3}.issubset({1,2,3,4,5})
#print(set2) #verificamos si el set2 es un subconjunto de {1,2,3,4,5}'''

set2 = {1, 2, 3}#verifica si {1,2} es un conjunto de {1,2,3}
set1 = {1, 2, 3, 4, 5}
print(len (set1))