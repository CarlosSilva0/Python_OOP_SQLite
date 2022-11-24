#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
poyatos = Pessoa(1, "Henrique Poyatos")
print(poyatos)

#Quero mostrar só o nome
print(poyatos.nome)

#Chama o objeto de banco de dados
db = Database() 

pessoaDAO= PessoaDAO(db.conexao, db.cursor)
pessoas = pessoaDAO.getall()
for pessoa in pessoas:
  print(pessoa)

