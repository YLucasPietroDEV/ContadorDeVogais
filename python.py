def contador_vogais(string):
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in string:
            if char in vogais:
                  contador += 1
    return contador
frase = input("Digite uma frase, vamos contar as vogais: ")
num_vogais = contador_vogais(frase)
print("O número de vogais na frase é:", num_vogais)
