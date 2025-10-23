import os
os.system('cls')

import tkinter as tk
from tkinter import ttk, messagebox

# --- Lógica del método del cuadrado medio ---
def metodo_cuadrado_medio(semilla, cantidad):
    resultados = []
    n = semilla
    longitud = len(str(semilla))
    
    for i in range(cantidad):
        n_cuadrado = n ** 2
        n_str = str(n_cuadrado).zfill(longitud * 2)
        mitad = len(n_str) // 2
        inicio = mitad - longitud // 2
        fin = inicio + longitud
        n_central = int(n_str[inicio:fin])
        num_normalizado = round(n_central / (10 ** longitud), 4)
        
        resultados.append({
            "iteracion": i + 1,
            "cuadrado": n_cuadrado,
            "extraido": n_central,
            "normalizado": num_normalizado
        })
        n = n_central
    return resultados

# --- Función para generar y mostrar los resultados ---
def generar():
    try:
        semilla = entry_semilla.get().strip()
        cantidad = entry_cantidad.get().strip()
        
        if not semilla.isdigit() or not cantidad.isdigit():
            raise ValueError("Debe ingresar números enteros válidos.")
        
        semilla = int(semilla)
        cantidad = int(cantidad)
        
        if semilla <= 0 or cantidad <= 0:
            raise ValueError("Los valores deben ser mayores que cero.")
        
        if len(str(semilla)) < 3 or len(str(semilla)) > 6:
            messagebox.showwarning("Advertencia", "Usa una semilla de entre 3 y 6 dígitos para mejores resultados.")
        
        resultados = metodo_cuadrado_medio(semilla, cantidad)
        
        # Limpiar la tabla antes de insertar nuevos datos
        tabla.delete(*tabla.get_children())
        
        for r in resultados:
            tabla.insert("", "end", values=(
                r["iteracion"], r["cuadrado"], r["extraido"], r["normalizado"]
            ))
        
        messagebox.showinfo("Éxito", f"Se generaron {cantidad} números correctamente.")
    
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error inesperado", f"Ocurrió un problema: {e}")

# --- Configuración de la ventana principal ---
ventana = tk.Tk()
ventana.title("Método del Cuadrado Medio")
ventana.geometry("650x500")
ventana.resizable(False, False)
ventana.configure(bg="#e8eaf6")

# --- Título ---
tk.Label(
    ventana,
    text="Método del Cuadrado Medio",
    font=("Arial", 18, "bold"),
    bg="#e8eaf6",
    fg="#1a237e"
).pack(pady=15)

# --- Marco para entradas ---
frame_inputs = tk.Frame(ventana, bg="#e8eaf6")
frame_inputs.pack(pady=5)

tk.Label(frame_inputs, text="Semilla:", font=("Arial", 12), bg="#e8eaf6").grid(row=0, column=0, padx=8, pady=5)
entry_semilla = tk.Entry(frame_inputs, font=("Arial", 12), width=15)
entry_semilla.grid(row=0, column=1, padx=8, pady=5)

tk.Label(frame_inputs, text="Cantidad de números:", font=("Arial", 12), bg="#e8eaf6").grid(row=1, column=0, padx=8, pady=5)
entry_cantidad = tk.Entry(frame_inputs, font=("Arial", 12), width=15)
entry_cantidad.grid(row=1, column=1, padx=8, pady=5)

# --- Botones ---
frame_botones = tk.Frame(ventana, bg="#e8eaf6")
frame_botones.pack(pady=10)

tk.Button(
    frame_botones,
    text="Generar",
    command=generar,
    font=("Arial", 12, "bold"),
    bg="#3f51b5",
    fg="white",
    relief="flat",
    width=12
).grid(row=0, column=0, padx=10)

tk.Button(
    frame_botones,
    text="Limpiar",
    command=lambda: [entry_semilla.delete(0, tk.END), entry_cantidad.delete(0, tk.END), tabla.delete(*tabla.get_children())],
    font=("Arial", 12, "bold"),
    bg="#f44336",
    fg="white",
    relief="flat",
    width=12
).grid(row=0, column=1, padx=10)

# --- Tabla de resultados ---
columns = ("Iteración", "Cuadrado", "Extraído", "Normalizado")
tabla = ttk.Treeview(ventana, columns=columns, show="headings", height=12)

# Encabezados
for col in columns:
    tabla.heading(col, text=col, anchor="center")
    tabla.column(col, anchor="center", width=130)

# Estilo visual de la tabla
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", background="#3f51b5", foreground="white", font=("Arial", 11, "bold"))
style.configure("Treeview", background="white", font=("Arial", 10), rowheight=25)

tabla.pack(pady=10, fill="both", expand=True)

# --- Pie de página ---
tk.Label(
    ventana,
    text="Proyecto: Generador de números pseudoaleatorios • Cuadrado Medio",
    font=("Arial", 9),
    bg="#e8eaf6",
    fg="#424242"
).pack(pady=5)

ventana.mainloop()