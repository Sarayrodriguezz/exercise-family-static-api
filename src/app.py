import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the Jackson family instance
jackson_family = FamilyStructure("Jackson")

# Handle exceptions and return them as JSON
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generate sitemap with all available routes
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Get all family members
@app.route('/members', methods=['GET'])
def get_all_members():
    try:
        members = jackson_family.get_all_members()
        return jsonify(members), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get one member by ID
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

# Add a new member
@app.route('/member', methods=['POST'])
def add_member():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    try:
        new_member = jackson_family.add_member(data)
        return jsonify(new_member), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a member by ID
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = jackson_family.get_member(member_id)
    if not member:
        return jsonify({"error": "Member not found"}), 404

    jackson_family.delete_member(member_id)
    return jsonify({"done": True}), 200

# Start the server
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
