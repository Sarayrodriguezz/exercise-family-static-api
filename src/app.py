"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# el objeto de la familia Jackson
jackson_family = FamilyStructure("Jackson")

# Manejo de errores como objetos JSON
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# todos los endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# 1) GET /members - Obtener todos los miembros
@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# 2) GET /member/<int:member_id> - Obtener un miembro específico
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member is None:
        return jsonify({"error": "Member not found"}), 404
    return jsonify(member), 200

# 3) POST /member - Añadir un nuevo miembro
@app.route('/member', methods=['POST'])
def add_member():
    data = request.get_json()
    if not data or "first_name" not in data or "age" not in data or "lucky_numbers" not in data:
        return jsonify({"error": "Invalid data"}), 400
    if not isinstance(data["age"], int) or data["age"] <= 0:
        return jsonify({"error": "Age must be a positive integer"}), 400
    if not isinstance(data["lucky_numbers"], list):
        return jsonify({"error": "Lucky numbers must be a list"}), 400
    
    new_member = jackson_family.add_member(data)
    return jsonify(new_member), 200

# 4) DELETE /member/<int:member_id> - Eliminar un miembro
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    success = jackson_family.delete_member(member_id)
    if not success:
        return jsonify({"error": "Member not found"}), 404
    return jsonify({"done": True}), 200

# Iniciar la aplicación
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)