print (" ") #Salto de linea
print ("Velazquez Mares Jesus Eliu 3W ") #Nombre del creador del codigo
print (" ") #Salto de linea

class Agenda: #Crea una clase llamada agenda
    def __init__(self): #Inicia la clase
        self.contactos = []
    def añadir_contacto(self):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        contacto = {'nombre': nombre, 'telefono': telefono, 'email': email}
        self.contactos.append(contacto)
        print("Contacto añadido correctamente.")
    def listar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            print("\nLista de Contactos:")
            for idx, contacto in enumerate(self.contactos, 1):
                print(f"{idx}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
    def buscar_contacto(self):
        nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
        encontrado = False
        for contacto in self.contactos:
            if contacto['nombre'].lower() == nombre_buscar.lower():
                print(f"\nContacto encontrado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado.")
    def editar_contacto(self):
        nombre_editar = input("Ingrese el nombre del contacto que desea editar: ")
        for contacto in self.contactos:
            if contacto['nombre'].lower() == nombre_editar.lower():
                print(f"Datos actuales del contacto {contacto['nombre']}:")
                print(f"Teléfono: {contacto['telefono']}")
                print(f"Email: {contacto['email']}")
                nuevo_nombre = input("Ingrese el nuevo nombre (deje en blanco para no cambiar): ")
                if nuevo_nombre:
                    contacto['nombre'] = nuevo_nombre
                nuevo_telefono = input("Ingrese el nuevo teléfono (deje en blanco para no cambiar): ")
                if nuevo_telefono:
                    contacto['telefono'] = nuevo_telefono
                nuevo_email = input("Ingrese el nuevo email (deje en blanco para no cambiar): ")
                if nuevo_email:
                    contacto['email'] = nuevo_email
                print("Contacto editado correctamente.")
                return
        print("Contacto no encontrado.")
    def mostrar_menu(self):
        while True:
            print("\n--- Menú de la Agenda ---")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.añadir_contacto()
            elif opcion == '2':
                self.listar_contactos()
            elif opcion == '3':
                self.buscar_contacto()
            elif opcion == '4':
                self.editar_contacto()
            elif opcion == '5':
                print("Cerrando agenda...")
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")
agenda = Agenda()# Crear una instancia de la agenda y mostrar el menú
agenda.mostrar_menu()