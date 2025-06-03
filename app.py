from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from newspaper import Article
from langdetect import detect
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")  # Configure essa variável no Render

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resumir', methods=['POST'])
def resumir():
    data = request.json
    url = data.get('url')

    try:
        # 1. Extrair o conteúdo do link
        artigo = Article(url)
        artigo.download()
        artigo.parse()
        texto = artigo.text

        # 2. Detectar idioma
        idioma = detect(texto)

        # 3. Gerar o resumo com base no idioma
        prompt = f"Resuma o texto abaixo de forma objetiva e clara em {idioma}:\n\n{texto}"

        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=600
        )

        resumo = resposta['choices'][0]['message']['content'].strip()
        return jsonify({'resumo': resumo})

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
