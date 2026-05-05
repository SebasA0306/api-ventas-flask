import pandas as pd
import sqlite3

def obtener_datos():
    conn = sqlite3.connect("data/ventas.db")
    df=pd.read_sql("SELECT * FROM ventas", conn)
    conn.close()
    
    df = df.dropna()
    df["total"] = df["cantidad"]*df["precio"]  #se crea una nueva columna con el cálculo total
    
    ventas_producto = df.groupby("producto")["total"].sum().reset_index() #sumo la venta de los productos y los almaceno en total, producto por producto
    
    return ventas_producto