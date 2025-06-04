from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resumir', methods=['POST'])
def resumir():
    try:
        data = request.json
        url = data.get('url')

        if not url:
            return jsonify({'erro': 'Nenhum link foi enviado.'}), 400

        # Aqui será o lugar para resumir o conteúdo real da página
        resumo = f"Resumo gerado para o link: {url}"

        return jsonify({'resumo': resumo})

    except Exception as e:
        # Exibe erros claros no console e retorna para o frontend
        print(f"[ERRO] Ocorreu um erro: {e}")
        return jsonify({'erro': 'Erro interno no servidor.', 'detalhes': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)


