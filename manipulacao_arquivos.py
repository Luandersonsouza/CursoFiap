# utilizamos as letras:
# R para realizar a leitura do arquivo
# W para escrever um novo arquivo
# A tanto para ler como para atualizar um arquivo
# X  torna exclusivo a visualização e manipulação do arquivo somente por 1 pessoa


with open("primeiro_arquivo.txt", "a") as arquivo:
	arquivo.write("\n Hakuna Matata")