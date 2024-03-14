def contar_letra(palavra, letra):
    contagem = 0
    for caractere in palavra:
        if caractere == letra:
            contagem +=1
    return contagem
