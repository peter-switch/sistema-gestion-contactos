![Sistema de Gestión de Contactos en Python](https://repository-images.githubusercontent.com/965984078/11454188-b3b7-4c1d-b67e-6db05d4afbc0)

# Sistema de Gestión de Contactos

## Descripción

Este proyecto consiste en crear un programa en Python que simule un **sistema de gestión de contactos**. El programa permite al usuario realizar varias operaciones sobre una lista de contactos.

### Funcionalidades:

1. **Agregar un contacto**  
   Permite al usuario agregar un nuevo contacto a la lista, con nombre, número de teléfono y correo electrónico.

2. **Mostrar todos los contactos**  
   Muestra una lista completa de todos los contactos almacenados.

3. **Buscar un contacto**  
   Permite buscar un contacto por su nombre.

4. **Eliminar un contacto**  
   Permite eliminar un contacto existente de la lista.

---

## Requisitos

- Uso de **clases** para representar contactos y el sistema de gestión.
- Implementación de **métodos** para:
  - Agregar
  - Mostrar
  - Buscar
  - Eliminar contactos
- Uso de **estructuras de control** y **ciclos** para la interacción con el usuario.
- **Manejo de archivos** para guardar y cargar los contactos desde un archivo de texto.
- **Gestión de errores** para manejar casos como:
  - Formato inválido de correo electrónico.
  - Buscar o eliminar contactos inexistentes.
  - Errores al leer o escribir en el archivo.

---

## Instrucciones de Implementación

1. Crear una clase `Contacto` con los atributos:
   - `nombre`
   - `telefono`
   - `correo`

2. Crear una clase `GestionContactos` que contenga:
   - Una lista de contactos.
   - Métodos para agregar, mostrar, buscar y eliminar contactos.

3. Implementar un **menú interactivo** para que el usuario pueda seleccionar las acciones.

4. Utilizar un archivo de texto para:
   - **Guardar** la lista de contactos.
   - **Cargar** los datos al iniciar el programa.

5. Validar:
   - El formato del correo electrónico.
   - Que los campos obligatorios no estén vacíos.

6. Manejar excepciones para:
   - Errores en la lectura/escritura del archivo.
   - Operaciones sobre contactos inexistentes.

---

## Entrega

Los estudiantes deben entregar:
- El **código fuente** del programa (`.py`).
- Un **archivo de texto** con algunos contactos de ejemplo.

---

¡Buena suerte programando!

