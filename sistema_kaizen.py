"""Sistema Kaizen para limpieza masiva y analisis Pareto de reportes.

El script procesa archivos Excel desde reportes_diarios, genera archivos limpios en
reportes_procesados y calcula un resumen global de movimientos por producto.

Uso:
    python sistema_kaizen.py
"""

import glob
import os

import pandas as pd


def limpiar_archivo(archivo: str) -> pd.DataFrame:
    """Limpia un archivo de inventario y devuelve el DataFrame resultante."""
    df = pd.read_excel(archivo)
    df_limpio = df.drop_duplicates(subset=["ID_Producto"]).copy()
    df_limpio["Nombre"] = df_limpio["Nombre"].str.capitalize()
    # abs() evita cantidades negativas en el reporte final.
    df_limpio["Cantidad"] = df_limpio["Cantidad"].fillna(0).abs()
    return df_limpio


def procesar_reportes(
    carpeta_entrada: str = "reportes_diarios", carpeta_salida: str = "reportes_procesados"
) -> list[pd.DataFrame]:
    """Procesa reportes Excel, guarda version limpia y devuelve dataframes limpios."""
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    archivos_excel = glob.glob(os.path.join(carpeta_entrada, "*.xlsx"))
    print(f"🔍 Se encontraron {len(archivos_excel)} archivos para procesar.\n")

    lista_para_analisis: list[pd.DataFrame] = []

    for archivo in archivos_excel:
        print(f"⚙️ Procesando: {os.path.basename(archivo)}")
        df_limpio = limpiar_archivo(archivo)

        nombre_salida = os.path.join(carpeta_salida, "limpio_" + os.path.basename(archivo))
        df_limpio.to_excel(nombre_salida, index=False)
        lista_para_analisis.append(df_limpio)

    return lista_para_analisis


def analizar_pareto(lista_para_analisis: list[pd.DataFrame]) -> None:
    """Imprime resumen de movimientos y porcentaje acumulado estilo Pareto."""
    print("\n--- 📊 INFORME DE MOVIMIENTOS Y PARETO ---")

    if not lista_para_analisis:
        print("No hay archivos para analizar en la carpeta de entrada.")
        return

    df_total = pd.concat(lista_para_analisis)
    resumen = (
        df_total.groupby("Nombre")["Cantidad"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    resumen["Porcentaje"] = (resumen["Cantidad"] / resumen["Cantidad"].sum()) * 100
    resumen["Porc_Acumulado"] = resumen["Porcentaje"].cumsum()

    print(resumen)

    productos_top = resumen[resumen["Porc_Acumulado"] <= 85]
    print(
        "\n✅ Analisis finalizado. "
        f"Tienes {len(productos_top)} productos que representan el 80% de tu movimiento."
    )


if __name__ == "__main__":
    dataframes_limpios = procesar_reportes()
    analizar_pareto(dataframes_limpios)