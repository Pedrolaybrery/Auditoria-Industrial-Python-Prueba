import pandas as pd
import os
import matplotlib.pyplot as plt

# 1. Configuración de la ruta del archivo real
archivo_real = 'reportes_diarios/Base de datos 1.xls'

print(f"--- Procesando Base de Datos Real: {archivo_real} ---")

# 2. Carga de datos saltando la fila de basura (header=1)
df = pd.read_excel(archivo_real, header=1)

# 3. Limpieza: Quitamos filas donde el vendedor esté vacío
df_limpio = df.dropna(subset=['VENDEDOR']).copy()

# 4. ANÁLISIS: Aquí es donde CREAMOS la variable 'movimientos'
# Contamos cuántos registros tiene cada vendedor
movimientos = df_limpio['VENDEDOR'].value_counts().reset_index()
movimientos.columns = ['Vendedor_ID', 'Cantidad_Movimientos']

# 5. Cálculo de Pareto (Opcional pero útil para el reporte)
total = movimientos['Cantidad_Movimientos'].sum()
movimientos['Porc_Acumulado'] = (movimientos['Cantidad_Movimientos'] / total).cumsum() * 100

print("\n📊 TABLA DE MOVIMIENTOS GENERADA:")
print(movimientos.head())

# 6. VISUALIZACIÓN: Ahora Python ya sabe qué es 'movimientos'
print("\n🎨 Generando gráfico de movimientos...")

plt.figure(figsize=(10, 6))
# Usamos .astype(str) para que los IDs de vendedor se vean bien en el eje X
plt.bar(movimientos['Vendedor_ID'].astype(str), movimientos['Cantidad_Movimientos'], color='skyblue')

# Títulos y etiquetas profesionales
plt.title('Movimientos por Vendedor (Carga de Trabajo)', fontsize=14)
plt.xlabel('ID del Vendedor', fontsize=12)
plt.ylabel('Número de Movimientos', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Guardamos la imagen para tu portafolio
plt.savefig('grafico_movimientos.png')
print(df.head()) # Esto te muestra las primeras 5 filas que Python leyópython
print("✅ Gráfico guardado como 'grafico_movimientos.png'")

# Mostramos el gráfico
plt.show()