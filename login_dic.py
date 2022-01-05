#criando login e percorrendo dados do dicionario
from funcoes import *
usuarios={}
opcao=perguntar()
while opcao=="1" or opcao=="2" or opcao=="3" or opcao=="4":
	if opcao=="1":
		inserir(usuarios)
	if opcao=="2":
		pesquisar(usuarios, input("Qual login deseja pesquisar?\n").upper())
	if opcao=="3":
		excluir(usuarios, input("Qual login deseja excluir?\n").upper())
	if opcao=="4":
		listar(usuarios)	
	opcao=perguntar()