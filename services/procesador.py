import pandas as pd

def obtener_datos():
    df = pd.read_csv("data/ventas.csv")  #convierte el archivo en un Data Frame, tabla en python
    df = df.dropna()
    df["total"] = df["cantidad"]*df["precio"]  #se crea una nueva columna con el cálculo total
    
    ventas_producto = df.groupby("producto")["total"].sum().reset_index() #sumo la venta de los productos y los almaceno en total, producto por producto
    
    return ventas_producto