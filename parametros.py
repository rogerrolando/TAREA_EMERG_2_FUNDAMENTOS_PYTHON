@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"Hola {nombre}, bienvenido"

if __name__ == '__main__':
    app.run(debug=True)