class Salario:
	def __init__(self, salarioBruto):
		self.salarioBruto = salarioBruto
		self.salarioLiquido = 0.0
		self.inss = 0.0
		self.irrf = 0.0
		self.planoSaude = 125.00

	def calcularSalario(self):
		self.salarioLiquido = (self.salarioBruto - self.inss - self.irrf - self.planoSaude)
		return self.salarioLiquido