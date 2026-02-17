import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from datastructure import FamilyStructure


app = Flask(__name__)
CORS(app)

# Inicializar la familia Jackson
jackson_family = FamilyStructure("Jackson")

# Miembros iniciales con IDs fijos (1, 2, 3) para pasar el primer test
jackson_family.add_member({
    "first_name": "John",
    "age": 33,
    "lucky_numbers": [7, 13, 22]
})

jackson_family.add_member({
    "first_name": "Jane",
    "age": 35,
    "lucky_numbers": [10, 14, 3]
})

jackson_family.add_member({
    "first_name": "Jimmy",
    "age": 5,
    "lucky_numbers": [1]
})

# --- RUTAS ---

@app.route('/members', methods=['GET'])
def handle_get_all():
    return jsonify(jackson_family.get_all_members()), 200

@app.route('/members/<int:member_id>', methods=['GET'])
def handle_get_one(member_id):
    member = jackson_family.get_member(member_id)
    if member is None:
        return jsonify({"msg": "Member not found"}), 404
    return jsonify(member), 200

@app.route('/members', methods=['POST'])
def handle_add():
    request_body = request.get_json()
    new_member = jackson_family.add_member(request_body)
    return jsonify(new_member), 200


@app.route('/members/<int:member_id>', methods=['DELETE'])
def handle_delete(member_id):
    deleted = jackson_family.delete_member(member_id)
    if not deleted:
        return jsonify({"msg": "Member not found"}), 404
    return jsonify({"done": True}), 200
