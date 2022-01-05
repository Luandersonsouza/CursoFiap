
def perguntar():
	return input("\nO que deseja realizar?\n"
		"\n<1> - Para Inserir um usuário.\n" + 
	 	"<2> - Para pesquisar um usuário.\n" + 
	 	"<3> - Para Excluir um usuário.\n" +
	 	"<4> - Para listar usuários.\n").upper()

def inserir(dicionario):
	chave=input("Digite o login: ").upper()
	dicionario[chave]=[input("Digite o nome: ").upper(),
				input("Digite a ultima data de acesso: "),
				input("Qual a ultima estação acessada: ").upper()]

def pesquisar(dicionario, chave):
	lista=dicionario.get(chave)
	if lista!= None:
		print("Nome...........: ", lista[0])
		print("Último acesso..: ", lista[1])
		print("Última estação.: ", lista[2])

def excluir(dicionario, chave):
	if dicionario.get(chave) !=None:
		del dicionario[chave]
	print("Objeto Excluido.")

def listar(dicionario):
	for chave,valor in dicionario.items():
		print("Objeto......")
		print("Login: ", chave)
		print("Dados: ", valor)