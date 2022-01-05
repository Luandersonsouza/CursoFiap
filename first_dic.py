#listas
#lista serve para estruturar um conjunto de informações.

#BigData trabalha com banco de dados não relacional

#Dicionario de dados pegamos um conjunto de valores e vinculamos a ele uma chave de busca.

#Criando um dicionário.

usuarios={}
print(usuarios)

usuarios={"chaves" : ["Chaves do 8", "24/12/2017", "Recp_01"], "quico": ["Quico das Flores", "20/12/2017, Raox_03"]}

print(usuarios)
usuarios["florinda"] = ["Dona florinda", "24/17/2017", "Raiox_01"]
print(usuarios)

print("####----####")

print(usuarios.get("quico"))