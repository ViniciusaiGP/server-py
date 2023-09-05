from flask import Flask, jsonify, request
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/test-post', methods=['POST'])
def teste():
    # Verifica se a requisição é do tipo JSON
    if request.is_json:
        data = request.get_json()
        # Verifica se as chaves 'sobrenome' e 'nome' estão presentes nos dados recebidos
        if 'sobrenome' in data and 'nome' in data:
            nome = data['nome']
            sobrenome = data['sobrenome']
            # Faça o que quiser com o sobrenome e o nome aqui
            return jsonify({'mensagem': f'Recebi  Nome: {nome} e sobrenome: {sobrenome}'})
        else:
            return jsonify({'erro': 'Dados incompletos'}), 400
    else:
        return jsonify({'erro': 'Requisição não é JSON'}), 400

if __name__ == '__main__':
    app.run(debug=True)
