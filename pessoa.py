class Pessoa:
	
	def __init__(self):
		self._name = ''
		self._rg = ''
		self._cpf = ''
		self._anoNasc = 0
		self._mesNasc = 0
		self._diaNasc = 0
		self._sexo = ''
		self._pessoa = {}
	
	def _cadastrar(self):
		self._name = input('Nome: ')
		self._rg = input('RG: ')
		self._cpf = input('CPF: ')
		dateOfBirth = input('Data de Nascimento [DD/MM/YYYY]: ')
		self._diaNasc, self._mesNasc, self._anoNasc = dateOfBirth.split('/')
		self._sexo = input('Sexo: ')
		self._pessoa = {'nome':self._name, 'rg':self._rg, 'cpf':self._cpf,'diaNasc':self._diaNasc,
						'mesNasc':self._mesNasc,'anoNasc':self._anoNasc,'sexo':self._sexo}

	def _exibir(self):
		return self._pessoa