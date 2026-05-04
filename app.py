from flask import Flask, jsonify
from services.procesador import obtener_datos
import pandas as pd

app = Flask(__name__)

@app.route("/ventas/<producto>")
def ventas_producto(producto):
    ranking = obtener_datos()
    
    resultado= ranking[ranking["producto"].str.lower() == producto.lower()]
    
    if resultado.empty:
        return jsonify({"error":"Producto no encontrado"}),404
    
    return jsonify(resultado.to_dict(orient="records"))

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Ruta no encontrada"}), 404

@app.route("/ventas")
def ventas():
    ranking=obtener_datos()
    return jsonify(ranking.to_dict(orient="records"))

@app.route("/top")
def top_productos():
    ranking = obtener_datos().sort_values("total",ascending=False)
    return jsonify(ranking.to_dict(orient="records"))

@app.route("/top/<int:n>")
def top_n_productos(n):
    ranking = obtener_datos().sort_values("total",ascending=False)
    top_n=ranking.head(n)
    return jsonify(top_n.to_dict(orient="records"))

@app.route("/")
def home():
    return "API de ventas funcionando"

if __name__=="__main__":
    app.run(debug=True)