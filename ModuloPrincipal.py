#modulo principal
#identificação de funções
from IdentificacaoDeFuncoes import *

minhaLista=[]
print("\nPreenchendo: ")
preencherInventario(minhaLista)
print("\nExibindo:")
exibirInventario(minhaLista)

print("\nPesquisando:")
localizarPorNome(minhaLista)
print("\nAlterando:")
depreciarPorNome(minhaLista)

print("\nExcluindo:")
excluirPorSerial(minhaLista)
exibirInventario(minhaLista)

print("\nResumindo:")
resumirValores(minhaLista)
print("\nFim do Script.")