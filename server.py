#from operator import truediv
from flask import Flask
from mock_data import catalog
from about_me import me
import json

#Servidor/app
app = Flask("server")

#Creacion de rutas.
@app.route("/", methods=["get"])
def home_page():
    return "Under construction!"

@app.route("/about")
def about_me():
    return"Page About"

@app.route("/myAddress")
def get_address():
    address = me["address"]
    return f"{address['street']} {address['city']} {address['state']}"

@app.route("/test")
def test():
    return"I'm a simple test"
    
#API ENDPOINT
@app.route("/api/catalog")
def get_catalog():
    return json.dumps(catalog)

#con la funcion get(en Thunder Client) /api/catalog/count y regresar el num total de los productos
@app.route("/api/catalog/count")
def get_count():
    count=len(catalog)
    return json.dumps(count)

#con la funcion get(en Thunder Client) /api/catalog/sum y regresar el total de los precios de los productos
@app.route("/api/catalog/total")
def get_total():
    total=0
    for i in catalog:
        total += i["price"]
    res = f"${total}"
    return json.dumps(total)

#con la funcion get(en Thunder Client) /api/catalog/<id> y buscar el producto desde el id 
@app.route("/api/product/<id>")
def get_product(id):
    for i in catalog:
        if(id==i["id"]):
            return json.dumps(i)    
    return abort(404)

#con la funcion get(en Thunder Client) /api/catalog/most_expensive y mostrar el producto mas caro
@app.route("/api/product/most_expensive")
def get_most_expensive():
    pivot = catalog[0]
    for i in catalog:
        if i["price"] > pivot["price"]  :
            pivot=i
    return json.dumps(pivot)    
#Iniciar el servidor
app.run(debug=True)