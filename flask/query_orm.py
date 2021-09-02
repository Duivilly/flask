from create_db_orm import Pessoas

def insere():
    pessoa = Pessoas(nome='TESTE', idade=25)
    pessoa.save()

def consulta():
    pessoa =  Pessoas.query.all()
    for i in pessoa:
        print(i.nome, i.idade)

def altera():
    pessoa = Pessoas.query.filter_by(nome="TESTE").first()
    pessoa.idade = 21
    pessoa.save()

def exclui():
    pessoa = Pessoas.query.filter_by(nome="TESTE").first()
    pessoa.delete()

if __name__ == '__main__':
    #insere()
    #altera()
    #exclui()
    consulta()