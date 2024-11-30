print (" ") #Salto de linea
print ("Velazquez Mares Jesus Eliu 3W ") #Nombre del creador del codigo
print (" ") #Salto de linea

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1# Inicializa los dos números
        self.num2 = num2
    def suma(self):
        return self.num1 + self.num2# Realiza la suma
    def resta(self):
        return self.num1 - self.num2# Realiza la resta
    def multiplicacion(self):
        return self.num1 * self.num2# Realiza la multiplicación
    def division(self):
        if self.num2 != 0:# Realiza la división, verificando por división por cero
            return self.num1 / self.num2
def qwer():# Función principal para cargar los datos y mostrar los resultados
    num1 = int(input("Ingresa un numero: "))# Solicitar al usuario los valores de los dos números enteros
    num2 = int(input("Ingresa otro numero: "))
    calculadora = Calculadora(num1, num2)# Crear una instancia de la clase Calculadora
    print("\nResultados de las operaciones:") # Imprimir los resultados de las operaciones
    print(calculadora)
if __name__ == "__main__":
    qwer()