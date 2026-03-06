#EXPLICACIÓN DE LOS CONCEPTOS
#IF/ELSE
#ELIF
'''
print("-- Bienvenido al club de Python")
#1. Neceistamos saber la edad del usuario

edad = int(input("¿Que edad tienes colega?: "))

if edad >= 18:
    print("Entre a la fiesta papacho")
    print("La primera bebida es gratis")

else: 
    print("Lo siento, pequeño saltamontes no puedes entrar")
    print("Vuelve cuando seas más grande, adiós")

print("-- fin de la interacción en la disco") '''

#****************************************************************************

print("\n El sombrero mágico")
cualidad = input("Elija una cualidad (valor, astucia, inteligencia)").lower()  

if cualidad == "valor":
    print("GRYFFINDOR")

elif cualidad == "inteligencia":
    print("Slytherin")

elif cualidad == "astucia":
    print("Hufflepuff")

else: 
    print("Mmm, cualidad desconocida quizas eres Hufflepuff o Slytherin")


    




