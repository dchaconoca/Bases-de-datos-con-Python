##################################
# EJEMPLO BASE DE DATOS
# Siguiendo los pasos del curso
# Utilizando MySQL
##################################

import mysql.connector

# Conexión

basedatos = mysql.connector.connect(
    host = "localhost",
    user = "dchaconoca",
    passwd = "Diana-2074",
    database = "bd_prueba_python"
)

# Comandos SQL

crearBD = "CREATE DATABASE IF NOT EXISTS bd_prueba_python"

crearTabla = """CREATE TABLE IF NOT EXISTS persona(
                id int(10) auto_increment not null, 
                nombre varchar(40) not null,
                cedula varchar(10),
                edad int(3),
                cumpleanos date,
                CONSTRAINT pk_persona PRIMARY KEY(id)
                )
                """

leerPersonas = "SELECT * FROM PERSONA"

borrarPersonas = "DELETE FROM PERSONA"

######################################################
# Funciones generales que modifican la base de datos
# En una aplicación, deberían ir en un módulo aparte
# dedicado a comunicarse con la BD
######################################################


# Agregar persona. Persona es un diccionario con los
# datos de la persona a insertar
def insertarPersona(persona):
    insertPersona = """INSERT INTO persona VALUES (null, 
        %(nombre)s, 
        %(cedula)s,
        %(edad)s, 
        %(cumpleanos)s)
        """
    cursor.execute(insertPersona, persona)
    basedatos.commit()

# Suprime una persona dado su nombre
def suprimirPersona(nombre):
    deletePersona = f"DELETE FROM persona WHERE nombre = '{nombre}' "

    cursor.execute(deletePersona, nombre)
    basedatos.commit()

# Muestra la lista de todas las personas de la BD
def listaPersonas():
        cursor.execute(leerPersonas)

        laPersona = persona()

        rows = cursor.fetchall()

        if rows == []:
            print("No hay elementos para mostrar")
        else:
            for item in rows:

                laPersona.nombre =  item[1]
                laPersona.cedula =  item[2]
                laPersona.edad =  item[3]
                laPersona.cumpleanos =  item[4]

                print(laPersona)


# Manejo de persona

class persona:
    
    # Crea una instancia de la clase
    def __init__(self, nombre='', cedula='', edad='', cumpleanos=''):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.cumpleanos = cumpleanos

    # Define cómo se "imprime" una instancia de la clase
    def __str__(self):
        estapersona = "\nEsta persona se llama " + self.nombre
        estapersona = estapersona + " su cédula es: " + self.cedula
        estapersona = estapersona + " nació el " + str(self.cumpleanos)
        estapersona = estapersona + " y tiene " + str(self.edad) + " años"

        return estapersona

    # Inserta una persona 
    def insertar(self):
        datosPersona = {
            "nombre": self.nombre,
            "cedula": self.cedula,
            "edad": str(self.edad),
            "cumpleanos": str(self.cumpleanos)
        }

        insertarPersona(datosPersona)

    # Borrar persona(s) con un nombre dado
    def borrar(self):
        suprimirPersona(self.nombre)
    


##################################
############   MAIN   ############
##################################

# El cursor se obtiene de la conexión y permite trabajar con la BD
cursor = basedatos.cursor()

# Insertando personas en la BD
diana = persona("Diana", "V-12345678", "45", "1974/08/20")
diana.insertar()

ines = persona("Inés", "V-98765432", "32", "1988/05/31")
ines.insertar()

aura = persona("Aura", "V-34567890", "66", "1955/01/07")
aura.insertar()

gracia = persona("Gracia", "V-12345678", "37", "1983/02/18")
gracia.insertar()

listaPersonas()

# Borramos elementos
print("Borramos Diana")
diana.borrar()
print("Borramos Aura")
aura.borrar()
print("Borramos Gracia")
gracia.borrar()
print("Borramos Inés")
ines.borrar()

listaPersonas()





