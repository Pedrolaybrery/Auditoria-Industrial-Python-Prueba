"""Pipeline simple de generacion y limpieza de datos de inventario.

Flujo:
1) Genera un archivo de ejemplo con datos inconsistentes.
2) Ejecuta una limpieza basica.
3) Exporta el resultado final.

Uso:
    python auditor.py
"""

import pandas as pd


def generar_datos_sucios(archivo_salida: str = "datos_sucios.xlsx") -> None:
    """Crea un archivo de ejemplo con duplicados, nulos y diferencias de texto."""
    print("Generando datos industriales sucios...")
    data = {
        "ID_Producto": [101, 102, 101, 103, 104, 105, 105],
        "Nombre": [
            "Engranaje",
            "Perno",
            "Engranaje",
            "Tuerca",
            "Eje",
            "Rodamiento",
            "rodamiento",
        ],
        "Cantidad": [50, 20, 50, -10, 15, None, 30],
    }
    df_sucio = pd.DataFrame(data)
    df_sucio.to_excel(archivo_salida, index=False)
    print(f"✅ Archivo '{archivo_salida}' creado.")


def limpiar_reporte(
    archivo_entrada: str = "datos_sucios.xlsx", archivo_salida: str = "reporte_final.xlsx"
) -> None:
    """Aplica limpieza basica y exporta el resultado consolidado."""
    print("\nIniciando limpieza...")
    df = pd.read_excel(archivo_entrada)

    df_limpio = df.drop_duplicates(subset=["ID_Producto"]).copy()
    df_limpio["Nombre"] = df_limpio["Nombre"].str.capitalize()
    df_limpio["Cantidad"] = df_limpio["Cantidad"].fillna(0)

    df_limpio.to_excel(archivo_salida, index=False)
    print("✅ ¡REPORTE FINAL GENERADO CON EXITO!")


if __name__ == "__main__":
    generar_datos_sucios()
    limpiar_reporte()