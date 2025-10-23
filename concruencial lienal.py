import os
os.system('cls')

import csv
import math

def lcg(a: int, c: int, m: int, seed: int, n: int):
    """
    Generador congruencial lineal.
    Retorna una lista con n valores enteros (0..m-1).
    """
    if m <= 0:
        raise ValueError("m debe ser > 0")
    if not (0 <= seed < m):
        raise ValueError("seed debe estar en 0 <= seed < m")
    x = seed
    seq = []
    for _ in range(n):
        x = (a * x + c) % m
        seq.append(x)
    return seq

def normalize_sequence(seq, m):
    """Convierte secuencia de enteros a flotantes en [0,1)."""
    return [x / m for x in seq]

def mean(values):
    return sum(values) / len(values) if values else float('nan')

def variance(values):
    # varianza muestral (n-1) si n>1, sino 0
    n = len(values)
    if n <= 1:
        return 0.0
    mu = mean(values)
    return sum((x - mu)**2 for x in values) / (n - 1)

def save_csv(filename, seq, normalized=False):
    header = ["index", "value"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i, v in enumerate(seq, start=1):
            writer.writerow([i, v])
    print(f"Secuencia guardada en '{filename}' (normalized={normalized})")

def sample_run():
    # Ejemplo de parámetros recomendados:
    # Minimal standard LCG (Park & Miller) uses c=0, a=16807, m=2**31-1
    return {
        "a": 1664525,
        "c": 1013904223,
        "m": 2**32,
        "seed": 123456789,
        "n": 20
    }

def main():
    print("Generador Congruencial Lineal (LCG)\n")
    try:
        use_example = input("¿Usar ejemplo rápido? (s/n) [s]: ").strip().lower() or "s"
        if use_example == "s":
            params = sample_run()
            a = params["a"]; c = params["c"]; m = params["m"]
            seed = params["seed"]; n = params["n"]
            print("Usando parámetros de ejemplo:")
            print(f" a={a}, c={c}, m={m}, seed={seed}, n={n}\n")
        else:
            a = int(input("Ingrese multiplicador a: ").strip())
            c = int(input("Ingrese incremento c: ").strip())
            m = int(input("Ingrese módulo m: ").strip())
            seed = int(input("Ingrese semilla (0 <= seed < m): ").strip())
            n = int(input("¿Cuántos números desea generar? n = ").strip())

        as_float = input("¿Mostrar como flotantes en [0,1)? (s/n) [n]: ").strip().lower() or "n"
        normalized = (as_float == "s")

        seq = lcg(a, c, m, seed, n)

        if normalized:
            seq_norm = normalize_sequence(seq, m)
            print("\nSecuencia normalizada [0,1):")
            for i, v in enumerate(seq_norm, 1):
                print(f"{i:3d}: {v:.10f}")
            mu = mean(seq_norm)
            var = variance(seq_norm)
        else:
            print("\nSecuencia (enteros):")
            for i, v in enumerate(seq, 1):
                print(f"{i:3d}: {v}")
            mu = mean(seq)
            var = variance(seq)

        print("\nEstadísticas:")
        print(f" Media = {mu}")
        print(f" Varianza (muestral) = {var}")

        guardar = input("\n¿Guardar la secuencia en CSV? (s/n) [n]: ").strip().lower() or "n"
        if guardar == "s":
            filename = input("Nombre de archivo (ej: salida.csv): ").strip() or "lcg_output.csv"
            # Si se pide normalizada guardamos la secuencia normalizada
            to_save = seq_norm if normalized else seq
            save_csv(filename, to_save, normalized=normalized)

        print("\n¡Generación finalizada!")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
