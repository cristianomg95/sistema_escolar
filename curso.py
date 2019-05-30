from banco_de_dados import DataBase
from professor import Professor


class Curso:
	
	def __init__(self):
		self._titulo = ''
		self._descricao = ''
		self._valor = 865.23
		self._sala = ''
		self._professor = Professor()
		self._professores = DataBase('database/professor.pickle').loadObject()

	def cadastrarCurso(self):
		self._titulo = input('Titulo: ')
		self._descricao = input('Descrição: ')
		self._sala = input('Sala: ')
		p = False
		while p is False:
			prof_aux = input('Professor: ')
			for pr in self._professores:
				if prof_aux == pr._name:
					self._professor = pr
					p = True
					break
			if p is False:
				print('Professor não encontrado, indique outro professor!')

	def exibir(self):
		return {'titulo': self._titulo,'sala':self._sala,
		 'professor': self._professor.exibir()['nome'], 'descrição':self._descricao}
	
	def calcularMinAluno(self):
		if self._professor.exibir()['nivel'] == '1':
			custoCurso = round((6500.00 / self._valor))
		elif self._professor.exibir()['nivel'] == '2':
			custoCurso = round((8325.00 / self._valor))
		elif self._professor.exibir()['nivel'] == '3':
			custoCurso = round((12568.43 / self._valor))
		return custoCurso