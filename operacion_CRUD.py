from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = [
    {"id": 1, "nombre": "Juan"},
    {"id": 2, "nombre": "Ana"}
]

@app.route('/')
def inicio():
    return "API Flask CRUD funcionando"

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    for u in usuarios:
        if u["id"] == id:
            return jsonify(u)
    return {"error": "No encontrado"}, 404

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    nuevo = request.json
    usuarios.append(nuevo)
    return jsonify(nuevo), 201

@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    datos = request.json
    for u in usuarios:
        if u["id"] == id:
            u["nombre"] = datos.get("nombre", u["nombre"])
            return jsonify(u)
    return {"error": "No encontrado"}, 404

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    for u in usuarios:
        if u["id"] == id:
            usuarios.remove(u)
            return {"mensaje": "Eliminado"}
    return {"error": "No encontrado"}, 404

if __name__ == '__main__':
    app.run(debug=True)