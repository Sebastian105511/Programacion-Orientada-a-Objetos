import tkinter as tk
from tkinter import messagebox

# Función para agregar el texto del campo de entrada a la lista
def agregar():
    texto = entrada.get()
    if texto:
        lista.insert(tk.END, texto)
        entrada.delete(0, tk.END)  # Limpiar campo de texto
    else:
        messagebox.showwarning("Entrada vacía", "Por favor ingresa un texto.")

# Función para limpiar la selección de la lista
def limpiar():
    seleccion = lista.curselection()
    if seleccion:
        lista.delete(seleccion)
    else:
        messagebox.showwarning("Ninguna selección", "Por favor selecciona un ítem para eliminar.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Crear etiqueta
label = tk.Label(ventana, text="Ingrese información:")
label.pack(pady=10)

# Crear campo de texto
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Crear botón "Agregar"
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)
boton_agregar.pack(pady=5)

# Crear listbox para mostrar los datos
lista = tk.Listbox(ventana)
lista.pack(pady=10)

# Crear botón "Limpiar"
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
