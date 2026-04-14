import pandas as pd
import os
import glob

# 1. Configuración de carpetas
carpeta_entrada = 'reportes_diarios'
if not os.path.exists(carpeta_entrada):
    os.makedirs(carpeta_entrada)

# Buscamos TODO: .xlsx, .xls y .csv
archivos = glob.glob(os.path.join(carpeta_entrada, "*.*"))

print(f"📂 Archivos encontrados en '{carpeta_entrada}': {[os.path.basename(a) for a in archivos]}")

for archivo in archivos:
    print(f"\n--- Analizando: {os.path.basename(archivo)} ---")
    
    # 2. Lector Universal (Detecta si es CSV o Excel)
    if archivo.endswith('.csv'):
        df = pd.read_csv(archivo)
    elif archivo.endswith(('.xlsx', '.xls')):
        df = pd.read_excel(archivo)
    else:
        continue # Si es otra cosa, ignóralo

    # 3. ¡EL TRUCO! Ver los nombres reales de las columnas
    print("Columnas detectadas en este archivo:")
    print(df.columns.tolist())
    
    # 4. Mostrar las primeras 3 filas para entender los datos
    print("Vista previa de datos:")
    print(df.head(3))