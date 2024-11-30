print (" ") #Salto de linea
print ("Velazquez Mares Jesus Eliu 3W ") #Nombre del creador del codigo
print (" ") #Salto de linea

#Creasion de una clase llamada Alumno
class Alumno:
    def __init__(self, nombre, nota): #Define self, nombre y nota como atributos de la clase
        self.nombre = nombre #Asigna el valor de nombre a self.nombre
        self.nota = nota #Asigna el valor de nota a self.nota
q = Alumno(str(input("Ingresa tu nombre: ")), float(input("ingresa la calificacion de tu nota: "))) 
#Le pedimos al usuario su nombre y nota
if q.nota < 6: #Si q.nota es menor que 6 reprobastes 
    print (q.nombre , "has reprobado con una nota de ", q.nota)
else: #Sino
    print (q.nombre , "has aprobado con una nota de ", q.nota) #Aprobastes