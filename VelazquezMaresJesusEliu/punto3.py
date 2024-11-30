print (" ") #Salto de linea
print ("Velazquez Mares Jesus Eliu 3W ") #Nombre del creador del codigo
print (" ") #Salto de linea

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1# Inicializa los lados del triángulo
        self.lado2 = lado2
        self.lado3 = lado3
    def lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)# Devuelve el valor del lado con mayor tamaño
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:# Determina el tipo de triángulo
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"
    def __str__(self):
        # Devuelve una cadena con la información del triángulo
        return f"Lados del triángulo: {self.lado1}, {self.lado2}, {self.lado3}\n" \
               f"Lado mayor: {self.lado_mayor()}\n" \
               f"Tipo de triángulo: {self.tipo_triangulo()}"
def main():# Función principal para cargar los datos y mostrar la información
    lado1 = float(input("Ingrese el valor del primer lado: "))
    # Solicitar al usuario los valores de los lados del triángulo
    lado2 = float(input("Ingrese el valor del segundo lado: "))
    lado3 = float(input("Ingrese el valor del tercer lado: "))
    triangulo = Triangulo(lado1, lado2, lado3)# Crear una instancia de la clase Triangulo
    print(triangulo)# Imprimir los resultados
if __name__ == "__main__":
    main()
