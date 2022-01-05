#listas dentro de listas
#Depreciação e Exclusão
inventario=[]
resposta="S"
while resposta=="S":

	equipamento=[input("Equipamento: "),
		 		float(input("Valor: ")),
	 			int(input("Número Serial: ")),
	 			input("Departamento: ")]
	inventario.append(equipamento)
	resposta=input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
	print("\nNome.........: ", elemento[0])
	print("Valor........: ", elemento[1])
	print("Serial.......: ", elemento[2])
	print("Departamento.: ", elemento[3])

busca=input("\nDigite o nome do Equipamento que deseja buscar: ")
for elemento in inventario:
	if busca==elemento[0]:
		print("Valor........: ", elemento[1])
		print("Serial.......: ", elemento[2])
		print("Departamento.: ", elemento[3])

depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
for elemento in inventario:
	if depreciacao==elemento[0]:
		print("Valor antigo..: ", elemento[1])
		elemento[1] = elemento[1] * 0.9
		print("Novo valor: ", elemento[1])


serial=int(input("\nDigite o Serial do equipamento que será excluído: "))
for elemento in inventario:
	if elemento[2]==serial:
		inventario.remove(elemento)
		print("\nO equipamento foi removido.")


for elemento in inventario:
	print("\nNome.......: ", elemento[0])
	print("Valor........: ", elemento[1])
	print("Serial.......: ", elemento[2])
	print("Departamento.: ", elemento[3])

valores=[]
for elemento in inventario:
	valores.append(elemento[1])
if len(valores)>0:
	print("\nO equipamento mais caro custa: ", max(valores))
	print("\nO equipamento mais barato custa: ", min(valores))
	print("\nO valor total em equipamentos é de: ", sum(valores))