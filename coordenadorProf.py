from professor import Professor

class CoordenadorProfessor(Professor):
	def __init__(self):
		self._area = ''
		self._plusSalario = 1.15

	def cadastrarCoordenadorProf(self):
		self.cadastrarProfessor()
		self._area = input('Area: ')
		new = {'area':self._area}
		self._pessoa.update(new)
	
	def calcularPlus(self):
		salario = self.calcularSalario()*self._plusSalario
		return salario

