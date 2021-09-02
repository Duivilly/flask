from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:key1>/<int:key2>')
def soma(key1, key2):
    soma= key1 + key2
    return jsonify({'soma': soma})

@app.route('/post', methods=['POST'])
def sum():
    dados= json.loads(request.data)
    return jsonify({'soma': sum(dados['dados'])})

#return 'Olá {}'.format(key)

if __name__ == "__main__":
    app.run(debug=True)