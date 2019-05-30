from banco_de_dados import DataBase
from funcionario import Funcionario
from professor import Professor
from aluno import Aluno
from coordenadorAdm import CoordenadorAdm
from coordenadorProf import CoordenadorProfessor
from matricula import Matricula
from curso import Curso
import utilitarios as ut
from os import system


class Menu:
	def __init__(self):
		self.__aluno = Aluno()
		self.__professor = Professor()
		self.__funcionario = Funcionario()
		self.__coordenadorAdm = CoordenadorAdm()
		self.__coordenadorProf = CoordenadorProfessor()
		self.__curso = Curso()
		self.__matricula = Matricula()
		self.__dbFuncionario = DataBase('database/funcionario.pickle')
		self.__dbProfessor = DataBase('database/professor.pickle')
		self.__dbAluno = DataBase('database/aluno.pickle')
		self.__dbCoordenadorADM = DataBase('database/coordenadorAdm.pickle')
		self.__dbCoordenadorPro = DataBase('database/coordenadorPro.pickle')
		self.__dbMatricula = DataBase('database/matricula.pickle')
		self.__dbCurso = DataBase('database/curso.pickle')

	def menuInicial(self):
		system('clear')
		print('''1 - Menu de Cadastro
2 - Menu de Exibição
3 - Menu de Utilitarios ''')
		p = False
		while p is False:
			opc = int(input('Escola uma opção: '))
			if opc in [1,2,3]:
				if opc == 1:
					p == True
					self.__menuCadastrar()
					break
				elif opc == 2:
					p == True
					self.__menuExibicao()
					break
				elif opc == 3:
					p == True
					self.__menuUtilitarios()
					break
			else:
				print('Opção invalida, digite um numero correto!!!')
				
	def __menuCadastrar(self):
		system('clear')
		print('''1 - Cadastrar Aluno
2 - Cadastrar Professor
3 - Cadastrar Funcionario
4 - Cadastrar Coordenador Administrativo
5 - Cadastrar Curso
6 - Fazer Matricula''')
		p = False
		while p is False:
			opc = int(input('Escolhar uma opção: '))
			if opc in [1,2,3,4,5,6]:
				if opc == 1:
					system('clear')
					self.__aluno.cadastrarAluno()
					self.__dbAluno.saveObject(self.__aluno)
					break
				elif opc == 2:
					system('clear')
					self.__professor.cadastrarProfessor()
					self.__dbProfessor.saveObject(self.__professor)
					break
				elif opc == 3:
					system('clear')
					self.__funcionario.cadastrarFuncionario()
					self.__dbFuncionario.saveObject(self.__funcionario)
					break
				elif opc == 4:
					system('clear')
					self.__coordenadorAdm.cadastrarCoordenadorAdm()
					self.__dbCoordenadorADM.saveObject(self.__coordenadorAdm)
					break
				elif opc == 5:
					system('clear')
					self.__curso.cadastrarCurso()
					self.__dbCurso.saveObject(self.__curso)
					break
				elif opc == 6:
					system('clear')
					self.__matricula.matricular()
					self.__dbMatricula.saveObject(self.__matricula)
					break
			else:
				print('Opção invalida, digite um numero correto!!!')

	def __menuExibicao(self):
		system('clear')
		print('''1 - Exibir Alunos
2 - Exibir Professores
3 - Exibir Funcionarios
4 - Exibir Coordenador Admininstrativo
5 - Exibir Coordenador Professor
6 - Exibir Cursos
7 - Exibir Matricula''')
		p = False
		while p is False:
			opc = int(input('Escolhar uma opção: '))
			if opc in [1,2,3,4,5,6,7]:
				if opc == 1:
					system('clear')
					ut.mostrarLista(lambda: self.__dbAluno.loadObject())
					break
				elif opc == 2:
					system('clear')
					ut.mostrarLista(lambda: self.__dbProfessor.loadObject())
					break
				elif opc == 3:
					system('clear')
					ut.mostrarLista(lambda: self.__dbFuncionario.loadObject())
					break
				elif opc == 4:
					system('clear')
					ut.mostrarLista(lambda: self.__dbCoordenadorADM.loadObject())
					break
				elif opc == 5:
					system('clear')
					ut.mostrarLista(lambda: self.__dbCoordenadorProf.loadObject())
					break
				elif opc == 6:
					system('clear')
					ut.mostrarLista(lambda: self.__dbCurso.loadObject())
					break
				elif opc == 7:
					system('clear')
					ut.mostrarLista(lambda: self.__dbMatricula.loadObject())
					break
			else:
				print('Opção invalida, digite um numero correto!!!')

	def __menuUtilitarios(self):
		system('clear')
		print('''1 - Calcular Salario Líquido 
2 - Calcular Bonificação
3 - Calcular Numero de Alunos Minimos para pagar o Curso
''')
		p = False
		while p is False:
			opc = int(input('Escolhar uma opção: '))
			if opc in [1,2,3]:
				if opc == 1:
					system('clear')
					opc = input('Qual o tipo de funcionario? [professor, coordenadorProf, coordenadorAdm, funcionarioAdm]: ')
					if opc == 'professor':
						system('clear')
						obj = ut.buscarObjetoNaLista(lambda: self.__dbProfessor.loadObject(), 'Digite o nome do Professor: ')
						print('Salario = {}'.format(obj.calcularSalario()))
						break
					elif opc == 'coordenadorProf':
						system('clear')
						obj = ut.buscarObjetoNaLista(lambda: self.__dbCoordenadorPro.loadObject(), 'Digite o nome do Coordenador Professor: ')
						print('Salario = {}'.format(obj.calcularSalario()))
						break
					elif opc == 'coordenadorAdm':
						system('clear')
						obj = ut.buscarObjetoNaLista(lambda: self.__dbCoordenadorADM.loadObject(), 'Digite o nome do Coordenador Admnistrativo: ')
						print('Salario = {}'.format(obj.calcularSalario()))
						break
					elif opc == 'funcionarioAdm':
						system('clear')
						obj = ut.buscarObjetoNaLista(lambda: self.__dbFuncionario.loadObject(), 'Digite o nome do Funcionario: ')
						print('Salario = {}'.format(obj.calcularSalario()))
						break
				elif opc == 2:
					system('clear')
					opc = input('Qual o tipo de coordenador? [professor, administrativo]: ')
					if opc == 'professor':
						system('clear')
						obj = ut.buscarObjetoNaLista(lambda: self.__dbCoordenadorPro.loadObject(), 'Digite o nome do Coordenador: ')
						print('Bonificação = {}'.format(obj.calcularSalario()))
						break
					elif opc == 'administrativo':
						system('clear')
						obj = ut.buscarObjetoNaLista(lambda: self.__dbCoordenadorADM.loadObject(), 'Digite o nome do Coordenador: ')
						print('Bonificação = {}'.format(obj.calcularSalario()))
						break
				elif opc == 3:
					system('clear')
					obj = ut.buscarObjetoCursoNaLista(lambda: self.__dbCurso.loadObject(), 'Digite o nome do Curso: ')
					print('Numero de Alunos Necessarios = {}'.format(obj.calcularMinAluno()))
					break