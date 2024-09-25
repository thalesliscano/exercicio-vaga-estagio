'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

'''

texto = "Oi eu sou thales, um candidato forte para esta vaga, estou muito feliz por estar aqui hoje falando com vocês!"
texto_invertido = ""
for letra in range(0, len(texto) +1):
    texto_invertido = texto[letra::-1]
print(texto_invertido)