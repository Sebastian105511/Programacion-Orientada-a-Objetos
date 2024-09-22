import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesitarás instalar tkcalendar

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Frame para la lista de eventos
        self.frame_lista = ttk.Frame(self.root)
        self.frame_lista.pack(pady=10)

        self.tree = ttk.Treeview(self.frame_lista, columns=("fecha", "hora", "descripcion"), show='headings')
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.pack()

        # Frame para entrada de datos
        self.frame_entrada = ttk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.fecha_entry = DateEntry(self.frame_entrada)
        self.fecha_entry.grid(row=0, column=1)

        ttk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0)
        self.hora_entry = ttk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=1, column=1)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.descripcion_entry = ttk.Entry(self.frame_entrada)
        self.descripcion_entry.grid(row=2, column=1)

        # Botones
        ttk.Button(self.root, text="Agregar Evento", command=self.agregar_evento).pack(pady=5)
        ttk.Button(self.root, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(pady=5)
        ttk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=5)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos")

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este evento?")
            if confirmacion:
                self.tree.delete(seleccionado)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")

    def limpiar_campos(self):
        self.fecha_entry.set_date("")
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
