print (" ") #Salto de linea
print ("Velazquez Mares Jesus Eliu 3W ") #Nombre del creador del codigo
print (" ") #Salto de linea

#Creasion de una clase llamada Persona
class Persona:
    def __init__(self, nombre, edad): #Define self, nombre y edad como atributos de la clase
        self.nombre = nombre #Asigna el valor de nombre a self.nombre
        self.edad = edad #Asigna el valor de edad a self.edad
q = Persona(str(input("Ingresa tu nombre: ")), int(input("ingresa tu edad: "))) 
#Le pedimos al usuario su nombre y edad
if q.edad <= 17: 
    print (q.nombre , "de", q.edad, "años ", "es menor de edad") #Si la edad es igual o menor a 17 imprime el mensaje
else: #Sino
    print (q.nombre , "de", q.edad, "años ","es mayor de edad") #Imprime este mensaje en su lugar