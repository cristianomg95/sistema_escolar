from aluno import Aluno
from curso import Curso
from banco_de_dados import DataBase

class Matricula:
	def __init__(self):
		self._id = len(DataBase('database/matricula.pickle').loadObject())+1
		self._mesMatricula = 0
		self._anoMatricula = 0
		self._aluno = Aluno()
		self._curso = Curso()
		self._cursos = DataBase('database/curso.pickle').loadObject()
		self._alunos = DataBase('database/aluno.pickle').loadObject()
		
	def matricular(self):
		p = False
		while p is False:
			varAluno = input('Aluno: ')
			for aluno in self._alunos:
				if varAluno == aluno.exibir()['nome']:
					self._aluno = aluno
					p = True
					break
			if p is False:
				print('Aluno não existe no sistema!!')
		dataMatricula = input("Data de Matricula [DD,MM,YYYY]: ")
		dataSplit = dataMatricula.split('/')
		self._mesMatricula = dataSplit[1]
		self._anoMatricula = dataSplit[2]
		p1 = False
		while p1 is False:
			varCurso = input('Curso: ')
			for curso in self._cursos:
				if varCurso == curso.exibir()['titulo']:
					self._curso = curso
					p1 = True
					break
			if p is False:
				print('Curso não existe no sistema!!')
		print('Matricula Cadastrada')
			
	def exibir(self):
		return {'id': self._id, 'mesMatricula': self._mesMatricula,
				'anoMatricula': self._anoMatricula, 'aluno': self._aluno.exibir()['nome'],
				'curso':self._curso.exibir()['titulo'] }

