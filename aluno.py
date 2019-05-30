from pessoa import Pessoa
from banco_de_dados import DataBase

class Aluno(Pessoa):
	def __init__(self):

		self.id = len(DataBase('database/aluno.pickle').loadObject())+1
		self.interest = ''
		self.discount = 0.0

	def cadastrarAluno(self):
		self._cadastrar()
		self.interest = input('Qual Interesse do aluno: ')
		self.discount = float(input('Desconto: '))
		new = {'codigo':self.id, 'interesse':self.interest, 'desconto':self.discount}
		self._pessoa.update(new)
	
	def exibir(self):
		return self._pessoa
