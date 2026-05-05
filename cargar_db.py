import pandas as pd
import sqlite3
0.


#conectar a DB
conn = sqlite3.connect("data/ventas.db")

#guardar en tabla
df.to_sql("ventas", conn, if_exists="replace", index=False)

conn.close()

print("Datos cargados en la base de datos")