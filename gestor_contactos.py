
#Clase para generar contactos
class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"Contacto: {self.nombre} | {self.telefono} | {self.correo}\n"
    
    #
    def insercion_contacto(self):
        return f"{self.nombre},{self.telefono},{self.correo}\n"
    
#Clase para generar los métodos de gestión
class GestionContactos:

    def __init__(self):
        self.lista_contactos=lista_contactos_vacia=[]

    def agregar_contactos(self):
        pass
    
    def mostrar_contactos(self):
        pass

    def buscar_contactos(self):
        pass
    
    def eliminar_contactos(self):
        pass

#Clase para generar el menú interactivo
class MenuApp:

    pass
  