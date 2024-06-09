#Crear un diccionario llamado "Informacion Personal"
informacion_personal = {
    "Nombre": "Sebastian",
    "Edad": 18,
    "Cuidad": "Quito",
    "Profesion": "Profesor"
}

#Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["Ciudad"] = "Cuenca"

#Agregar nueva clave-valor al diccionaro que represente la "profesion"
informacion_personal["Profesion"] = "Estudiante"

#Verificar si la clave "telefono" existe y agragarla si no existe
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"]= "0967552886"

#Eliminar la clave "edad" del diccionario
if "Edad" in informacion_personal:
    del informacion_personal["Edad"]

#Imprimir el diccionario final
print(informacion_personal)