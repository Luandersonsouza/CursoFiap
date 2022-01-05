#tuplas são imutaveis
# Metodo dicionário itens retorna uma tupla com chave valor
usuarios={}

emails=["leozinho@leo.com", "diana@dia.com"]

tupla = list(enumerate(emails))

#print(tupla)

for chave in range (0, len(tupla)):
	print("\nEmail: ", tupla[chave][1])
	usuarios[tupla[chave]] = [input("Digite o nome: "), input("Digite o nivel: ")] 

for chave, dado in usuarios.items():
	print("\nUsuario.:", chave[0])
	print("Email...:", chave[1])
	print("Nome....:", dado [0])
	print("Nivel...:", dado [1])
