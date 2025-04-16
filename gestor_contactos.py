import re # biblioteca para trabajar con regex (expresiones regulares)
import os #biblioteca necesaria para poder validar la ruta del txt

#Clase para generar contactos
class Contacto:
    
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.nombre_archivo="agenda.txt"
        

    def __str__(self):
        return f"Nombre: {self.nombre} Tel: {self.telefono} Email:{self.correo}\n"
    
    #Usaremos este método para escribir en al txt
    def inserccion_contactos(self):

        try:

            with open(self.nombre_archivo,"r",encoding="utf8") as archivo:

                lineas=archivo.readlines()
                if lineas: #Si el archivo está creado y hay lineas escritas en el archivo

                    id_ultimo_encontrado=int(lineas[-1].split(",")[0])
                    #[-1] representa el último valor de la lista
                    #[0]Indica que solo imprima el indice 0 de la lista, en este caso es el ID
                    id=id_ultimo_encontrado+1
                    #sumamos 1 al id encontrado y ya tenemos el id para el próximo contacto

                else: #Si no hay lineas en el archivo, entoces es que está vacío y no hay ningún id

                    id=1 #El primer id será 1
                
                

        except FileNotFoundError:
                #Si el archivo no existe el primer id que se cree en un futuro sera 1
                id=1
                print(f"Archivo {self.nombre_archivo} no encontrado. Añade algún contacto para crearlo.")

        return f"{id},{self.nombre},{self.telefono},{self.correo}\n"

    
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
                id,nombre, telefono, correo=linea.strip().split(",") #limpiamos con strip y cortamos usando la coma.
                #Desmpaquetamos cada corte en una variable para conformar el diccionario
                #Creamos el diccionario con los 3 datos.
                contacto_diccionario={
                    "id":id,
                    "nombre":nombre,
                    "telefono":telefono,
                    "correo":correo
                }

                lista_agenda_diccionarios.append(contacto_diccionario) #Añadimos cada diccionario a la lista
            
            #Recorremos la lista de diccionarios e imprimimos cada valor
            for diccionario in lista_agenda_diccionarios:
                print(f"> Id: {diccionario['id']}")
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
                id,nombre, telefono, correo=linea.strip().split(",") #limpiamos con strip y cortamos usando la coma.
                #Desmpaquetamos cada corte en una variable para conformar el diccionario
                #Creamos el diccionario con los 3 datos.
                contacto_diccionario={
                    "id":id,
                    "nombre":nombre,
                    "telefono":telefono,
                    "correo":correo
                }

                lista_agenda_diccionarios.append(contacto_diccionario) #Añadimos cada diccionario a la lista

            print("*** Buscar contacto en la agenda ***")

            nombre_a_buscar=input("Introduce el nombre a buscar: ")


        resultados=[diccionario for diccionario in lista_agenda_diccionarios if diccionario["nombre"].lower()==nombre_a_buscar.strip().lower()]
            
        if resultados: #Si la lista resultados existe entoces hace lo siguiente:
            
            for nombre in resultados: #recorre la lista por si hay varios nombres de contactos iguales e imprime en pantalla
                print("\n¡Contacto encontrado!\n")
                print(f"> Id: {nombre['id']}")
                print(f"> Nombre: {nombre['nombre'].title()}") #title capitaliza nombre y apellido
                print(f"> Telefono: {nombre['telefono']}")
                print(f"> E-mail: {nombre['correo']}\n")

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
        self.mostrar_contactos()
        lista_contactos_actual=[]
        try:

            with open(self.nombre_archivo, "r", enconding="utf8"): #leemos el archivo
                contenido_archivo=archivo.readlines()
                for linea in contenido_archivo:
                    id,nombre,telefono,correo=linea.strip().split(",")

                    diccionario={
                        "id":id,
                        "nombre":nombre,
                        "telefono":telefono,
                        "email":correo
                    }
                    lista_contactos_actual.append(diccionario)

            id_a_eliminar=int(input("Escribe el id del contacto que deseas eliminar: "))

           #VAMOS POR AQUI. FALTA RECORRER LA LISTA COMPARANDO CON ELEMENO A ELIMINAR
           #Y GENERAR UNA NUEVA LISTA SIN ESE ELEMENO Y SOBREESCRIBIR EL TXT



        except FileNotFoundError as error01:
            print(f"Archivo no encontrado {error01}")

        except ValueError as error02:
            print(f"Valor introducido incorrecto. Debe ser un número positivo: {error02}")






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