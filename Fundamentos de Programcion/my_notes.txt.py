# Escritura de Archivo de Texto
# Creamos un nuevo archivo llamado my_notes.txt y escribimos algunas notas personales en él.

file_write = open("my_notes.txt", "w")
file_write.write("Estas son mis notas personales:\n")
file_write.write("1. Recordar que tengo que hacer la tarea por la tarde.\n")
file_write.write("2. Escribirle a mi compañera a las 4pm para realizar el proyecto.\n")
file_write.write("3. Revisar el proyecto antes de enviarlo.\n")
file_write.close()  # Cerramos el archivo después de escribir en él

# Lectura de Archivo de Texto
# Abrimos el archivo my_notes.txt y leemos su contenido línea por línea.

file_read = open("my_notes.txt", "r")
print("Contenido del archivo my_notes.txt:")
for line in file_read.readlines():
    print(line.strip())  # strip() para eliminar caracteres de nueva línea
file_read.close()  # Cerramos el archivo después de leerlo

# Cierre de Archivos
# Aseguramos cerrar los archivos después de realizar las operaciones necesarias.