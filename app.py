from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    # Lógica para salvar o usuário no banco de dados
    return jsonify({"message": "User registered successfully!"})

if __name__ == '__main__':
    app.run()
