import pandas as pd
from src.funciones import cargar_datos, manejar_nulos, estandarizar_texto, limpiar_precios

# 1. Cargar datos
productos = cargar_datos("data/productos.csv")
print(productos.head()) 
envios = cargar_datos("data/envios.csv")

# 2. Limpieza de datos
productos = limpiar_precios(productos, "precio")
productos = estandarizar_texto(productos, ["nombre", "categoría"])
envios = estandarizar_texto(envios, ["estado", "bodega"])

# Manejo de nulos
productos = manejar_nulos(productos, metodo="fill", valor={"precio": 0})
envios = manejar_nulos(envios, metodo="drop")

# 3. MERGE (unir tablas por id_producto)
df = pd.merge(envios, productos, on="id_producto", how="inner")

# =========================
# PREGUNTAS DE ANÁLISIS
# =========================

# 1. Frecuencia: producto con más envíos
producto_top = df["nombre"].value_counts().idxmax()
print(f"📌 El producto con más envíos es: {producto_top}")

# 2. Agregación: total de productos por bodega
unidades_bodega = df.groupby("bodega")["id_producto"].count()
print("\n📦 Total de envíos por bodega:")
print(unidades_bodega)

# 3. Filtrado: cuántos envíos están en estado 'en camino'
en_camino = df[df["estado"] == "en camino"].shape[0]
print(f"\n🚚 Número de envíos 'en camino': {en_camino}")
def cargar_datos(ruta):
    try:
        df = pd.read_csv(ruta)
        print(f"✅ Datos cargados desde {ruta}, {df.shape[0]} filas, {df.shape[1]} columnas")
        return df
    except Exception as e:
        print(f"❌ Error al cargar {ruta}: {e}")
        return pd.DataFrame()  # 👈 Mejor devolver un DataFrame vacío en vez de None
