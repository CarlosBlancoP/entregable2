# analisis.py
import pandas as pd
from src.funciones import (
    cargar_datos,
    manejar_nulos,
    estandarizar_texto,
    limpiar_precios
)

# 1. Cargar datos
productos = cargar_datos("data/productos.csv")
envios = cargar_datos("data/envios.csv")

print(f"✅ Datos cargados: productos ({productos.shape[0]} filas), envios ({envios.shape[0]} filas)")

# 2. Limpiar datos
productos = manejar_nulos(productos)
envios = manejar_nulos(envios)

productos = estandarizar_texto(productos, ["nombre", "categoría"])
envios = estandarizar_texto(envios, ["estado", "bodega"])

productos = limpiar_precios(productos, "precio")

# 3. Preguntas de análisis

# --- 1. Análisis de Frecuencia ---
producto_mas_vendido = envios["id_producto"].value_counts().idxmax()
print("\n🔹 Producto con más envíos:", producto_mas_vendido)

# --- 2. Análisis de Agregación ---
unidades_por_bodega = envios.groupby("bodega")["id_producto"].count()
print("\n🔹 Total de envíos por bodega:")
print(unidades_por_bodega)

# --- 3. Análisis con Filtrado y Conteo ---
retrasados = envios[envios["estado"] == "retrasado"].shape[0]
print("\n🔹 Cantidad de envíos retrasados:", retrasados)

# --- Extra: Merge para enriquecer análisis ---
df_merged = envios.merge(productos, on="id_producto", how="left")
ventas_por_categoria = df_merged.groupby("categoría")["id_envio"].count()
print("\n🔹 Total de envíos por categoría de producto:")
print(ventas_por_categoria)

