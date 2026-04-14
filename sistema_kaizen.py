import pandas as pd
import os
import glob

# 1. Configuración de rutas
carpeta_entrada = 'reportes_diarios'
carpeta_salida = 'reportes_procesados'

# Crear la carpeta de salida si no existe
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)

# 2. Buscar todos los archivos Excel en la carpeta
archivos_excel = glob.glob(os.path.join(carpeta_entrada, "*.xlsx"))

print(f"🔍 Se encontraron {len(archivos_excel)} archivos para procesar.\n")

lista_para_analisis = []

for archivo in archivos_excel:
    print(f"⚙️ Procesando: {os.path.basename(archivo)}")
    
    # Lectura y Limpieza
    df = pd.read_excel(archivo)
    df_limpio = df.drop_duplicates(subset=['ID_Producto']).copy()
    df_limpio['Nombre'] = df_limpio['Nombre'].str.capitalize()
    df_limpio['Cantidad'] = df_limpio['Cantidad'].fillna(0).apply(lambda x: abs(x)) # abs() asegura que no haya negativos
    
    # Guardar archivo individual limpio
    nombre_salida = os.path.join(carpeta_salida, "limpio_" + os.path.basename(archivo))
    df_limpio.to_excel(nombre_salida, index=False)
    
    # Guardar en una lista para el análisis global
    lista_para_analisis.append(df_limpio)

# 3. ANÁLISIS DE DATOS GLOBAL (Movimientos)
print("\n--- 📊 INFORME DE MOVIMIENTOS Y PARETO ---")
df_total = pd.concat(lista_para_analisis)

# Agrupar por producto para ver el total de movimientos
resumen = df_total.groupby('Nombre')['Cantidad'].sum().sort_values(ascending=False).reset_index()

# Calcular el porcentaje acumulado para el análisis de Pareto
resumen['Porcentaje'] = (resumen['Cantidad'] / resumen['Cantidad'].sum()) * 100
resumen['Porc_Acumulado'] = resumen['Porcentaje'].cumsum()

print(resumen)

# Identificar productos Clase A (el 80% de la importancia)
productos_top = resumen[resumen['Porc_Acumulado'] <= 85]
print(f"\n✅ Análisis finalizado. Tienes {len(productos_top)} productos que representan el 80% de tu movimiento.")