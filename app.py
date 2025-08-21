import tkinter as tk
from tkinter import messagebox
import os

# -------------------
# Funciones
# -------------------

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Atención", "No puedes añadir una tarea vacía")

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except:
        messagebox.showwarning("Atención", "Selecciona una tarea para eliminar")

def mark_done():
    try:
        index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(index)
        listbox_tasks.delete(index)
        listbox_tasks.insert(index, f"✔ {task}")
    except:
        messagebox.showwarning("Atención", "Selecciona una tarea para marcar como completada")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox_tasks.insert(tk.END, task.strip())

def save_tasks():
    tasks = listbox_tasks.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# -------------------
# Crear ventana principal
# -------------------
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# -------------------
# Widgets
# -------------------
entry_task = tk.Entry(root, width=35)
entry_task.grid(row=0, column=0, padx=10, pady=10)

btn_add = tk.Button(root, text="Añadir", width=10, command=add_task)
btn_add.grid(row=0, column=1, padx=10)

listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

btn_delete = tk.Button(root, text="Eliminar", width=10, command=delete_task)
btn_delete.grid(row=2, column=0, padx=10, pady=5, sticky="w")

btn_done = tk.Button(root, text="Completada", width=10, command=mark_done)
btn_done.grid(row=2, column=1, padx=10, pady=5, sticky="e")

# Cargar tareas al iniciar
load_tasks()

# Guardar tareas al cerrar la ventana
root.protocol("WM_DELETE_WINDOW", lambda: [save_tasks(), root.destroy()])

# Ejecutar app
root.mainloop()
