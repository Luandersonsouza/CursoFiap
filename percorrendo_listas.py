#inserção e busca de dados

equipamentos=[]
valores=[]
seriais=[]
departamentos=[]
resposta="S"
while resposta=="S":
	equipamentos.append(input("Equipamento: "))
	valores.append(float(input("Valor: ")))
	seriais.append(int(input("Número serial: ")))
	departamentos.append(input("Departamento: "))
	resposta=input("Digite \"S\"para continuar: ").upper()

busca=int(input("\n Digite o Número Serial do equipamento que deseja buscar: "))
for indice in range(0, len(seriais)):
	if busca==seriais[indice]:
		print("Valor..: ", valores[indice])
		print("Equipamento.: ", equipamentos[indice])
		print("Departamento: ", departamentos[indice])