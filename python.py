# Função contador que recebe uma string como argumento.
def contador_vogais(string):
# Definimos uma string chamada vogais, que contém todas as vogais em maiúsculas e minúsculas.
    vogais = 'aeiouAEIOU'
# Também inicializamos uma variável contador como 0, que será usada para contar o número de vogais na string.
    contador = 0
# Utilizamos um loop for para iterar sobre cada caractere na string fornecida pelo usuário.
# Em cada iteração, verificamos se o caractere atual está presente na string vogais.
    for char in string:
            if char in vogais:
            # Se o caractere for uma vogal, incrementamos o contador.
                  contador += 1
                # Após percorrer toda a string, retornamos o valor do contador, que representa o número total de vogais encontradas na string.
    return contador
frase = input("Digite uma frase, vamos contar as vogais: ")
# Chamamos a função contar_vogais com a frase fornecida pelo usuário como argumento.
# O retorno da função (o número de vogais na frase) é armazenado na variável num_vogais.
num_vogais = contador_vogais(frase)
print("O número de vogais na frase é:", num_vogais)
# or fim, exibimos o número de vogais na frase ao usuário.
