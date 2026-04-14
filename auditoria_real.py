"""Auditoria rapida de archivos en reportes_diarios.

Este script recorre los archivos CSV y Excel de la carpeta de entrada,
detecta sus columnas y muestra una vista previa de registros.

Uso:
    python auditoria_real.py
"""

import glob
import os

import pandas as pd


def leer_reporte(archivo: str) -> pd.DataFrame | None:
    """Lee un archivo CSV o Excel y devuelve un DataFrame.

    Si la extension no es soportada, devuelve None.
    """
    if archivo.endswith(".csv"):
        return pd.read_csv(archivo)
    if archivo.endswith((".xlsx", ".xls")):
        return pd.read_excel(archivo)
    return None


def auditar_reportes(carpeta_entrada: str = "reportes_diarios") -> None:
    """Muestra columnas y primeras filas de cada archivo del directorio."""
    if not os.path.exists(carpeta_entrada):
        os.makedirs(carpeta_entrada)

    archivos = glob.glob(os.path.join(carpeta_entrada, "*.*"))
    print(
        f"📂 Archivos encontrados en '{carpeta_entrada}': "
        f"{[os.path.basename(a) for a in archivos]}"
    )

    for archivo in archivos:
        print(f"\n--- Analizando: {os.path.basename(archivo)} ---")
        df = leer_reporte(archivo)
        if df is None:
            print("Formato no soportado. Se omite.")
            continue

        print("Columnas detectadas en este archivo:")
        print(df.columns.tolist())
        print("Vista previa de datos:")
        print(df.head(3))


if __name__ == "__main__":
    auditar_reportes()