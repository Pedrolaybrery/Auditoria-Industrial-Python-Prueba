# Auditoria de Datos - Guia Rapida

Proyecto orientado a limpieza y auditoria de reportes de inventario con Python + pandas.

## Estructura

- `auditor.py`: genera un archivo de datos sucios de ejemplo y crea un reporte limpio.
- `auditoria_real.py`: inspecciona archivos CSV/Excel en `reportes_diarios` y muestra columnas + vista previa.
- `sistema_kaizen.py`: procesa archivos Excel de `reportes_diarios`, guarda salidas limpias en `reportes_procesados` y calcula un resumen Pareto.
- `reportes_diarios/`: carpeta de entrada para archivos fuente.
- `reportes_procesados/`: carpeta de salida para reportes limpios.

## Requisitos

- Python 3.10 o superior (recomendado)
- Paquete `pandas`
- Motor de Excel para pandas (`openpyxl` recomendado)

Instalacion sugerida:

```bash
pip install pandas openpyxl
```

## Ejecucion

### 1) Ejemplo simple de limpieza

```bash
python auditor.py
```

Salida esperada:
- `datos_sucios.xlsx`
- `reporte_final.xlsx`

### 2) Auditoria exploratoria de reportes

```bash
python auditoria_real.py
```

Resultado:
- Lista archivos detectados en `reportes_diarios`
- Columnas por archivo
- Primeras 3 filas por archivo

### 3) Proceso masivo + Pareto

```bash
python sistema_kaizen.py
```

Resultado:
- Archivos `limpio_*.xlsx` en `reportes_procesados`
- Resumen agregado por producto
- Porcentaje y porcentaje acumulado (enfoque Pareto)

## Notas de calidad de datos aplicadas

- Eliminacion de duplicados por `ID_Producto`
- Normalizacion de texto en `Nombre`
- Relleno de nulos en `Cantidad` con 0
- Conversion de cantidades negativas a valor absoluto (solo en `sistema_kaizen.py`)

## Sugerencias de mejora

- Agregar validacion de columnas requeridas antes de procesar.
- Exportar el resumen Pareto a un archivo Excel/CSV.
- Incorporar pruebas automatizadas para reglas de limpieza.
