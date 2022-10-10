from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase  
from product import Product

db = dbase.dbConnection()

app = Flask(__name__)

#Rutas de la aplicación
@app.route('/')
def home():
    products = db['products']
    productsReceived = products.find()
    return render_template('index.html', products = productsReceived)

#Method Post
@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    name = request.form['name']
    fec_alta = request.form['fec_alta']
    codigo_zip = request.form['codigo_zip']
    credit_card_num = request.form['credit_card_num']
    credit_card_ccv = request.form['credit_card_ccv']
    geo_latitud = request.form['geo_latitud']
    geo_longitud = request.form['geo_longitud']
    color_favorito = request.form['color_favorito']
    foto_dni = request.form['foto_dni']
    auto = request.form['auto']
    auto_modelo = request.form['auto_modelo']
    auto_tipo = request.form['auto_tipo']
    auto_color = request.form['auto_color']





    if name and fec_alta and codigo_zip and credit_card_num and credit_card_ccv and geo_latitud and geo_longitud and color_favorito and foto_dni and auto and auto_modelo and auto_tipo and auto_color:
        product = Product(name, fec_alta, codigo_zip, credit_card_num, credit_card_ccv, geo_latitud, geo_longitud, color_favorito, foto_dni, auto, auto_modelo, auto_tipo, auto_color)
        products.insert_one(product.toDBCollection())
        response = jsonify({
            'name' : name,
            'fec_alta' : fec_alta,
            'codigo_zip' : codigo_zip,
            'credit_card_num' : credit_card_num,
            'credit_card_ccv' : credit_card_ccv,
            'geo_latitud' : geo_latitud,
            'geo_longitud' : geo_longitud,
            'color_favorito' : color_favorito,
            'foto_dni' : foto_dni,
            'auto' : auto,
            'auto_modelo' : auto_modelo,
            'auto_tipo' : auto_tipo,
            'auto_color' : auto_color
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Method delete
@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = db['products']
    products.delete_one({'name' : product_name})
    return redirect(url_for('home'))

#Method Put
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    products = db['products']
    name = request.form['name']
    fec_alta = request.form['fec_alta']
    codigo_zip = request.form['codigo_zip']
    credit_card_num = request.form['credit_card_num']
    credit_card_ccv = request.form['credit_card_ccv']
    cuenta_numero_direccion = request.form['cuenta_numero_direccion']
    geo_latitud = request.form['geo_latitud']
    geo_longitud = request.form['geo_longitud']
    color_favorito = request.form['color_favorito']
    foto_dni = request.form['foto_dni']
    auto = request.form['auto']
    auto_modelo = request.form['auto_modelo']
    auto_tipo = request.form['auto_tipo']
    auto_color = request.form['auto_color']


    if name and fec_alta and codigo_zip and credit_card_num and credit_card_ccv and geo_latitud and geo_longitud and color_favorito and foto_dni and auto and auto_modelo and auto_tipo and auto_color:
        products.update_one({'name' : product_name}, {'$set' : {'name' : name, 'fec_alta' : fec_alta, 'codigo_zip' : codigo_zip, 'credit_card_num' : credit_card_num,'credit_card_ccv' : credit_card_ccv, 'cuenta_numero_direccion' : cuenta_numero_direccion, 'geo_latitud' : geo_latitud,'geo_longitud' : geo_longitud,'color_favorito' : color_favorito,'foto_dni' : foto_dni,'auto' : auto,'auto_modelo' : auto_modelo, 'auto_tipo' : auto_tipo,'auto_color' : auto_color, }})
        response = jsonify({'message' : 'Producto ' + product_name + ' actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response



if __name__ == '__main__':
    app.run(debug=True, port=4000)