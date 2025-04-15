import re # biblioteca para trabajar con regex (expresiones regulares)
import os #biblioteca necesaria para poder validar la ruta del txt

#Clase para generar contactos
class Contacto:
    
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        

    def __str__(self):
        return f"Nombre: {self.nombre} Tel: {self.telefono} Email:{self.correo}\n"
    
    #Usaremos este método para escribir en al txt
    def inserccion_contactos(self):
        return f"{self.nombre},{self.telefono},{self.correo}\n"
    
#Clase para generar los métodos de gestión
class GestionContactos:

    def __init__(self):
        
        self.nombre_archivo="agenda.txt"

    def agregar_contactos(self,contacto):#recibe el objeto contacto desde MenuApp, que es el lugar donde se crea
        with open(self.nombre_archivo,"a",encoding="utf8") as archivo:
            archivo.write(contacto.inserccion_contactos())
            print("\nContacto añadido correctamente\n")
    
    def mostrar_contactos(self):

        # Verificar si el archivo existe
        if not os.path.exists(self.nombre_archivo):
            print(f"\n¡Atención! El archivo '{self.nombre_archivo}' no existe.")
            print("Por favor, agregue contactos primero antes de buscar.")
            return  # Salimos de la función

        #creamos una lista vacia para almacenar los diccionarios de 3 elementos.
        lista_agenda_diccionarios=[]
        with open(self.nombre_archivo, "r", encoding="utf8") as archivo: #abrimos el archivo en modo lectura con "r"
            print("\n*** Contactos disponibles ***\n")
            archivo_contactos=archivo.readlines() #Readlines genera una lista almacenando cada linea en un espacio de la lista.

            for linea in archivo_contactos: #recorremos cada espacio de la lista que será una cadena de ste tipo"nombre,telegono,correo"
                nombre, telefono, correo=linea.strip().split(",") #limpiamos con strip y cortamos usando la coma.
                #Desmpaquetamos cada corte en una variable para conformar el diccionario
                #Creamos el diccionario con los 3 datos.
                contacto_diccionario={
                    "nombre":nombre,
                    "telefono":telefono,
                    "correo":correo
                }

                lista_agenda_diccionarios.append(contacto_diccionario) #Añadimos cada diccionario a la lista
            
            #Recorremos la lista de diccionarios e imprimimos cada valor
            for diccionario in lista_agenda_diccionarios:
                print(f"> Nombre: {diccionario['nombre'].title()}") #title capitaliza nombre y apellido si lo tuviera
                print(f"> Telefono: {diccionario['telefono']}")
                print(f"> E-mail: {diccionario['correo']}\n")

          
            


    def buscar_contactos(self):
        # Verificar si el archivo existe
        if not os.path.exists(self.nombre_archivo):
            print(f"\n¡Atención! El archivo '{self.nombre_archivo}' no existe.")
            print("Por favor, agregue contactos primero antes de buscar.")
            return  # Salimos de la función

        #creamos una lista vacia para almacenar los diccionarios de 3 elementos.
        lista_agenda_diccionarios=[]

        with open(self.nombre_archivo, "r", encoding="utf8") as archivo: #abrimos el archivo en modo lectura con "r"
            
            archivo_contactos=archivo.readlines() #Readlines genera una lista almacenando cada linea en un espacio de la lista.

            for linea in archivo_contactos: #recorremos cada espacio de la lista que será una cadena de ste tipo"nombre,telegono,correo"
                nombre, telefono, correo=linea.strip().split(",") #limpiamos con strip y cortamos usando la coma.
                #Desmpaquetamos cada corte en una variable para conformar el diccionario
                #Creamos el diccionario con los 3 datos.
                contacto_diccionario={
                    "nombre":nombre,
                    "telefono":telefono,
                    "correo":correo
                }

                lista_agenda_diccionarios.append(contacto_diccionario) #Añadimos cada diccionario a la lista

            print("*** Buscar contacto en la agenda ***")

            nombre_a_buscar=input("Introduce el nombre a buscar: ")


        resultados_busqueda=[diccionario for diccionario in lista_agenda_diccionarios if diccionario["nombre"].lower()==nombre_a_buscar.strip().lower()]
            
        if resultados:
            
            for nombre in resultados:
                print("\n¡Contacto encontrado!\n")
                print(f"> Nombre: {diccionario['nombre'].title()}") #title capitaliza nombre y apellido
                print(f"> Telefono: {diccionario['telefono']}")
                print(f"> E-mail: {diccionario['correo']}\n")

        else:
                print("No hay resultados")
            # for diccionario in lista_agenda_diccionarios:
            #     if nombre_a_buscar.strip().lower()==diccionario["nombre"]:
            #         print("\n¡Contacto encontrado!\n")
            #         print(f"> Nombre: {diccionario['nombre'].title()}") #title capitaliza nombre y apellido
            #         print(f"> Telefono: {diccionario['telefono']}")
            #         print(f"> E-mail: {diccionario['correo']}\n")
            #     else:
            #         pass
            


    def eliminar_contactos(self):
        pass

#Clase para generar el menú interactivo
class MenuApp:

    def __init__(self):
        self.gestion_contactos=GestionContactos() #creamos el objeto gestion_contactos para poder usar los métodos de clase de GestionContactos
        self.email_patron= r"^[\w\.-]+@[\w\.-]+\.\w+$" #expresión regular para validar correos electrónicos
        self.telefono_patron= r"\d{9}" #expresión regular para validar teléfonos
        self.nombre_patron= r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$" #expresión regular para validar nómbres
    def menu(self):
        try:
            print("***Agenda de contactos***")
            
            while True:

                print("""
1. Añadir contacto.
2. Mostrar contactos.
3. Buscar contacto por nombre.
4. Eliminar contacto.
5. Salir.\n""")
                
                opcion=int(input("Selecciona opción (1-5): "))
                
                if opcion==1:
                    nombre=input("Nombre: ")
                    while re.fullmatch(self.nombre_patron,nombre)==None: #fullmuch devuelve None si no hay coincidencia completa con el patron 
                         print("\nFormato de nombre incorrecto.")
                         correo=input("Nombre: ")


                    telefono=input("Teléfono: ")
                    while re.fullmatch(self.telefono_patron,telefono)==None: #fullmatch devuelve None si no hay coincidencia con el patron 
                         print("\nFormato de telefono incorrecto.")
                         telefono=input("Teléfono: ")

                    correo=input("E-mail: ")
                    while re.fullmatch(self.email_patron,correo)==None: #fullmatch devuelve None si no hay coincidencia con el patron 
                         print("\nFormato de e-mail incorrecto.")
                         telefono=input("E-mail: ")
                        
                    contacto=Contacto(nombre.lower().strip(),telefono.strip(),correo.lower().strip()) 
                    #creamos el objero contacto y aprovechamos para guardar los datos en mínuscula y limpios de espacios
            
                    self.gestion_contactos.agregar_contactos(contacto)#pasamos objeto contacto a gestion_contactos


                elif opcion==2:
                    self.gestion_contactos.mostrar_contactos()


                elif opcion==3:
                    self.gestion_contactos.buscar_contactos()


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


#Creamos la instancia de MenuApp para iniciar el programa
agenda_contactos=MenuApp()
agenda_contactos.menu()