import menu

def cabecalho(funcaoCarregaBanco):
	print(' ', end=' ')
	for i in funcaoCarregaBanco()[0].exibir():
		print('{:<12}'.format(i), end= '')
	print()

def exibirObjeto(objeto):
	for j in objeto.exibir().values():
		print('{:<12}'.format(j), end='')
	print()

def mostrarLista(funcaoCarregaBanco):  #parametro passado em forma de lambda
	try:
		cabecalho(funcaoCarregaBanco)
		for i,k in enumerate(funcaoCarregaBanco()):
			print(i+1, end=' ')
			exibirObjeto(k)
	except:
		print('Erro, nenhum cadastro encontrado!!!')
		opc = input('Press enter to return to menu!!!')
		if opc == '':
			m = menu.Menu()
			m.menuInicial()

def buscarObjetoNaLista(funcaoCarregaBanco, msg):
	try:
		nomeObjeto = input(msg)
		for i in funcaoCarregaBanco():
			if nomeObjeto == i.exibir()['nome']:
				return i
			else: 
				continue
	except:
		print('Erro, nenhum cadastro encontrado!!!')
		opc = input('Press enter to return to menu!!!')
		if opc == '':
			m = menu.Menu()
			m.menuInicial()
		
def buscarObjetoCursoNaLista(funcaoCarregaBanco, msg):
	try:
		nomeObjeto = input(msg)
		for i in funcaoCarregaBanco():
			if nomeObjeto == i.exibir()['titulo']:
				return i
			else: 
				continue
	except:
		print('Erro, nenhum cadastro encontrado!!!')
		opc = input('Press enter to return to menu!!!')
		if opc == '':
			m = menu.Menu()
			m.menuInicial()