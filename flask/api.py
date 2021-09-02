from flask import Flask, request
from flask_restful import Resource, Api
from create_db_orm import Pessoas, Atividades
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)
api = Api(app)

USERS = {
    'rafael':'123',
    'admin':'123'
}

@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return USERS.get(login) == senha
    

class Dev(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'erro na request'
            }

        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        pessoa.save()
        return dados


class NewDev(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return response

    def post(self):
        data = request.json
        pessoa= Pessoas(nome=data['nome'], idade=data['idade'])
        pessoa.save()
        response = {
            'nome':pessoa.nome,
            'idade':pessoa.idade,
            'id':pessoa.id
        }
        return response

class Atividade(Resource):
    @auth.login_required
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id':i.id, 'nome':i.pessoa.nome, 'atividade': i.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            "pessoa" :  atividade.pessoa.nome,
            "nome" :  atividade.nome
        }
        return response


api.add_resource(Dev, '/dev/<string:nome>')
api.add_resource(NewDev, '/people')
api.add_resource(Atividade, '/atividade')


if __name__ == '__main__':
    app.run(debug=True)
