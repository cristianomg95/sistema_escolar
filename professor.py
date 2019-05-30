from funcionario import Funcionario
from salario import Salario

class Professor(Funcionario):
	
	def __init__(self):
		self._formacao = ''
		self._disciplina = ''
		self._nivel = 0
		self._salario = 0

	def cadastrarProfessor(self):
		self.cadastrarFuncionario()
		self._formacao = input('Formação: ')
		self._disciplina = input('Disciplina: ')
		new = {'formação':self._formacao, 'disciplina':self._disciplina}
		self._pessoa.update(new)

	def calcularSalario(self):
		if self._nivel == '1':
			salario = Salario(6500.00)
			self._salario = salario.calcularSalario()
		elif self._nivel == '2':
			salario = Salario(8325.50)
			self._salario = salario.calcularSalario()
		elif self._nivel == '3':
			salario = Salario(12568.43)
			self._salario = salario.calcularSalario()
		return self._salario