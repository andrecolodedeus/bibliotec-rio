from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/resumir', methods=['POST'])
def resumir():
    data = request.json
    url = data.get('url')
    # código para processar o link e gerar resumo
    resumo = "Aqui vai o resumo gerado..."
    return jsonify({'resumo': resumo})

if __name__ == "__main__":
    app.run(debug=True, port=5001)  # roda o Flask na porta 5001