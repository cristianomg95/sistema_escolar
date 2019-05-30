from funcionario import Funcionario

class CoordenadorAdm(Funcionario):

	def __init__(self):
		self._area = ''
		self._plusSalario = 1.135

	def cadastrarCoordenadorAdm(self):
		self.cadastrarFuncionario()
		self._area = input('Area: ')
		new = {'area':self._area}
		self._pessoa.update(new)
	
	def calcularPlus(self):
		salario = self.calcularSalario()*self._plusSalario
		return salario
