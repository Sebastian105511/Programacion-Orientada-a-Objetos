import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea
def add_task(event=None):
    task = entry_task.get().strip()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

# Función para marcar una tarea como completada
def complete_task(event=None):
    try:
        selected_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_index)
        if not task.startswith("[COMPLETADA] "):
            listbox_tasks.delete(selected_index)
            listbox_tasks.insert(selected_index, "[COMPLETADA] " + task)
        else:
            messagebox.showinfo("Información", "La tarea ya está completada.")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada.")

# Función para eliminar una tarea
def delete_task(event=None):
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminarla.")

# Función para cerrar la aplicación
def close_app(event=None):
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas Pendientes")

# Campo de entrada para nuevas tareas
entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

# Botón para añadir nueva tarea
button_add_task = tk.Button(root, text="Añadir Tarea", command=add_task)
button_add_task.pack(pady=5)

# Listbox para mostrar las tareas
listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)

# Botones para marcar como completada y eliminar tarea
button_complete_task = tk.Button(root, text="Marcar como Completada", command=complete_task)
button_complete_task.pack(pady=5)

button_delete_task = tk.Button(root, text="Eliminar Tarea", command=delete_task)
button_delete_task.pack(pady=5)

# Asignar atajos de teclado
root.bind('<Return>', add_task)           # Enter para añadir tarea
root.bind('<F2>', complete_task)           # Tecla 'C' para marcar como completada
root.bind('<F3>', delete_task)             # Tecla 'D' para eliminar tarea
root.bind('<Escape>', close_app)          # Tecla 'Escape' para cerrar la aplicación

# Iniciar el loop de la aplicación
root.mainloop()
