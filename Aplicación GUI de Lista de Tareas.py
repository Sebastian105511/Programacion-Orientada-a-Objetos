import tkinter as tk
from tkinter import messagebox


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        self.task_list = []  # Lista para almacenar tareas

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind('<Return>', self.add_task)  # Añadir tarea al presionar Enter

        # Botón para añadir tareas
        self.add_task_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)

        # Lista de tareas
        self.task_box = tk.Listbox(root, selectmode=tk.SINGLE, width=50)
        self.task_box.pack(pady=10)

        # Botón para marcar como completada
        self.complete_task_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:  # Comprobar si el campo no está vacío
            self.task_list.append(task)
            self.update_task_box()
            self.task_entry.delete(0, tk.END)  # Limpiar campo de entrada

    def complete_task(self):
        try:
            selected_index = self.task_box.curselection()[0]
            completed_task = self.task_list[selected_index] + " (Completada)"
            self.task_list[selected_index] = completed_task
            self.update_task_box()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_index = self.task_box.curselection()[0]
            del self.task_list[selected_index]
            self.update_task_box()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar.")

    def update_task_box(self):
        self.task_box.delete(0, tk.END)  # Limpiar la lista actual
        for task in self.task_list:
            self.task_box.insert(tk.END, task)  # Añadir tareas actualizadas


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
