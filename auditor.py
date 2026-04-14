import pandas as pd

# --- PARTE 1: CREAR LOS DATOS (EL INSUMO) ---
print("Generando datos industriales sucios...")
data = {
    'ID_Producto': [101, 102, 101, 103, 104, 105, 105],
    'Nombre': ['Engranaje', 'Perno', 'Engranaje', 'Tuerca', 'Eje', 'Rodamiento', 'rodamiento'],
    'Cantidad': [50, 20, 50, -10, 15, None, 30]
}
df_sucio = pd.DataFrame(data)
# Lo guardamos con un nombre sencillo
df_sucio.to_excel('datos_sucios.xlsx', index=False)
print("✅ Archivo 'datos_sucios.xlsx' creado.")

# --- PARTE 2: AUDITORÍA Y LIMPIEZA ---
print("\nIniciando limpieza...")
df = pd.read_excel('datos_sucios.xlsx')

# Limpieza básica
df_limpio = df.drop_duplicates(subset=['ID_Producto']).copy()
df_limpio['Nombre'] = df_limpio['Nombre'].str.capitalize()
df_limpio['Cantidad'] = df_limpio['Cantidad'].fillna(0)

# Guardar resultado final
df_limpio.to_excel('reporte_final.xlsx', index=False)
print("✅ ¡REPORTE FINAL GENERADO CON ÉXITO!")