from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from langdetect import detect

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resumir', methods=['POST'])
def resumir():
    data = request.json
    url = data.get('url')

    # Aqui você insere o código para baixar e resumir a página na língua original
    resumo = f"Resumo gerado para o link: {url}"
    return jsonify({'resumo': resumo})

if __name__ == "__main__":
    app.run(debug=True, port=5001)


