import os
os.system('cls')

import tkinter as tk
from tkinter import ttk, messagebox

# ------------------------------
# MÉTODO CONGRUENCIAL MULTIPLICATIVO
# ------------------------------
def metodo_congruencial_multiplicativo(semilla, a, m, cantidad):
    resultados = []
    x = semilla
    for i in range(cantidad):
        x = (a * x) % m
        r = x / (m - 1)
        resultados.append((i + 1, x, round(r, 5)))
    return resultados

# ------------------------------
# FUNCIÓN PARA GENERAR LOS NÚMEROS
# ------------------------------
def generar():
    try:
        semilla = int(entry_semilla.get())
        a = int(entry_a.get())
        m = int(entry_m.get())
        cantidad = int(entry_cantidad.get())
        
        if semilla <= 0 or a <= 0 or m <= 0 or cantidad <= 0:
            raise ValueError
        
        resultados = metodo_congruencial_multiplicativo(semilla, a, m, cantidad)
        
        # Limpiar tabla
        tabla.delete(*tabla.get_children())
        for iteracion, x, r in resultados:
            tabla.insert("", "end", values=(iteracion, x, r))
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese solo números válidos y mayores que cero.")

# ------------------------------
# INTERFAZ GRÁFICA
# ------------------------------
ventana = tk.Tk()
ventana.title("Método Congruencial Multiplicativo")
ventana.geometry("600x450")
ventana.configure(bg="#e8f0fe")

tk.Label(ventana, text="Método Congruencial Multiplicativo", font=("Arial", 16, "bold"), bg="#e8f0fe").pack(pady=10)

frame_inputs = tk.Frame(ventana, bg="#e8f0fe")
frame_inputs.pack(pady=5)

# Entradas
tk.Label(frame_inputs, text="Semilla (X₀):", font=("Arial", 12), bg="#e8f0fe").grid(row=0, column=0, padx=5, pady=5)
entry_semilla = tk.Entry(frame_inputs, font=("Arial", 12))
entry_semilla.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Constante multiplicativa (a):", font=("Arial", 12), bg="#e8f0fe").grid(row=1, column=0, padx=5, pady=5)
entry_a = tk.Entry(frame_inputs, font=("Arial", 12))
entry_a.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Módulo (m):", font=("Arial", 12), bg="#e8f0fe").grid(row=2, column=0, padx=5, pady=5)
entry_m = tk.Entry(frame_inputs, font=("Arial", 12))
entry_m.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Cantidad de números:", font=("Arial", 12), bg="#e8f0fe").grid(row=3, column=0, padx=5, pady=5)
entry_cantidad = tk.Entry(frame_inputs, font=("Arial", 12))
entry_cantidad.grid(row=3, column=1, padx=5, pady=5)

# Botón
tk.Button(ventana, text="Generar", command=generar, bg="#1a73e8", fg="white",
          font=("Arial", 12, "bold"), relief="flat").pack(pady=10)

# Tabla de resultados
columns = ("Iteración", "Xₙ", "Número Rₙ")
tabla = ttk.Treeview(ventana, columns=columns, show="headings", height=10)
for col in columns:
    tabla.heading(col, text=col)
    tabla.column(col, anchor="center")
tabla.pack(padx=10, pady=10, fill="both", expand=True)

ventana.mainloop()
