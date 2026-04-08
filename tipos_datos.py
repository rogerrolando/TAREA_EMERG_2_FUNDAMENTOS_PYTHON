@app.route('/numero/<int:num>')
def numero(num):
    return f"El número es {num}"

@app.route('/precio/<float:precio>')
def precio(precio):
    return f"Precio: {precio}"

@app.route('/archivo/<path:ruta>')
def archivo(ruta):
    return f"Ruta completa: {ruta}"

if __name__ == '__main__':
    app.run(debug=True)