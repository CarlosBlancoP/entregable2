import pandas as pd

# 1. Función para cargar datos
def cargar_datos(ruta):
    """
    Carga un archivo CSV en un DataFrame de pandas.
    """
    try:
        df = pd.read_csv(ruta)
        print(f"✅ Datos cargados desde {ruta}, {df.shape[0]} filas, {df.shape[1]} columnas")
        return df
    except Exception as e:
        print(f"❌ Error al cargar {ruta}: {e}")
        return None


# 2. Función para manejar valores nulos
def manejar_nulos(df, metodo="drop", valor=None):
    """
    Maneja valores nulos en un DataFrame.
    - metodo="drop": elimina filas con nulos
    - metodo="fill": rellena con el valor indicado
    """
    if metodo == "drop":
        return df.dropna()
    elif metodo == "fill":
        return df.fillna(valor)
    else:
        print("⚠️ Método no reconocido, usa 'drop' o 'fill'")
        return df


# 3. Función para estandarizar texto
def estandarizar_texto(df, columnas):
    """
    Convierte a minúsculas y quita espacios extra en columnas de texto.
    """
    for col in columnas:
        df[col] = df[col].astype(str).str.lower().str.strip()
    return df


# 4. Función de limpieza específica (ejemplo: quitar $ de precios)
def limpiar_precios(df, columna):
    """
    Limpia símbolos de moneda y convierte a número.
    """
    df[columna] = (
        df[columna]
        .astype(str)
        .str.replace("[$, ]", "", regex=True)
        .replace("null", None)
    )
    df[columna] = pd.to_numeric(df[columna], errors="coerce")
    return df
