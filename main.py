print("***********************************************")
print("Seja bem vindo ao sistema de contagem de letras")
print("***********************************************")

palavra = input("escolha uma palavra: ")
letra = input("Escolha a letra que deseja contar: ")

from funções import contar_letra

palavra = palavra
letra = letra
resultado = contar_letra(palavra, letra)
print(f"A letra {letra} aparece {resultado} vezes na palavra {palavra}")
