from pessoa import Pessoa
from salario import Salario

class Funcionario(Pessoa):

	def __init__(self):
		self._matricula = 0
		self._setor = ''
		self._cargo = ''
		self._nivel = 0
			
	def cadastrarFuncionario(self):
		self._matricula = int(input("Matricula: "))
		self._cadastrar()
		self._setor = input('Setor: ')
		self._cargo = input('Cargo: ')
		self._nivel = (input('Nivel: ')).lower()
		new = {'matricula':self._matricula, 'setor':self._setor, 'cargo':self._cargo, 'nivel':self._nivel}
		self._pessoa.update(new)
		
	def exibir(self):
		return self._pessoa

	def calcularSalario(self):
		if self._nivel == 'a':
			_salario = Salario(1520.25)
		elif self._nivel == 'b':
			_salario = Salario(2362.67)
		elif self._nivel == 'c':
			_salario = Salario(2988.92)
		elif self._nivel == 'd':
			_salario = Salario(3572.77)
		elif self.nivel == 'e':
			_salario = Salario(4878.67)
		return _salario.calcularSalario()