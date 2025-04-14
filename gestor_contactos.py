
#Clase para generar contactos
class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"Contacto: {self.nombre} | {self.telefono} | {self.correo}\n"
    
    #
    def inserccion_contactos(self):
        return f"{self.nombre},{self.telefono},{self.correo}\n"
    
#Clase para generar los métodos de gestión
class GestionContactos:

    def __init__(self):
        
        self.nombre_archivo="agenda.txt"

    def agregar_contactos(self,contacto):
        with open(self.nombre_archivo,"a") as archivo:
            archivo.write(contacto.inserccion_contactos())
            print("\nContacto añadido correctamente\n")
    
    def mostrar_contactos(self):
        pass

    def buscar_contactos(self):
        pass
    
    def eliminar_contactos(self):
        pass

#Clase para generar el menú interactivo
class MenuApp:

    def __init__(self):
        self.gestion_contactos=GestionContactos() #creamos el objeto gestion_contactos para poder usar los métodos de clase de GestionContactos

    def menu(self):
        try:
            print("***Agenda de contactos***")
            
            while True:

                print("""
                01. Añadir contacto.
                02. Mostrar contactos.
                03. Buscar contacto.
                04. Eliminar contacto.
                05. Salir.

                \n""")
                
                opcion=int(input("Selecciona opción (1-5): "))
                
                if opcion==1:
                    nombre=input("Nombre: ")
                    telefono=input("Telefono: ")
                    correo=input("E-mail: ")
                    contacto=Contacto(nombre,telefono,correo)
            
                    self.gestion_contactos.agregar_contactos(contacto)


                elif opcion==2:
                    pass


                elif opcion==3:
                    pass


                elif opcion==4:
                    pass


                elif opcion==5:
                    print("Saliendo del sistema...")
                    break
                else:
                    print("Opción incorrecta. Selecciona una entre 1 y 5.")

        except ValueError:
            print("Valor introducido incorrecto. Selecciona una opción entre 1 y 5.")            

        except Exception as error:
            print(f"Ha ocurrido un error: {error}")


print("error")
agenda_contactos=MenuApp()
agenda_contactos.menu()