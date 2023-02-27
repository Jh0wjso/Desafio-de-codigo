
string = input(str("Insira um texto para ser invertido: "))

lista_caracteres = list(string)

pos_inicial = 0
pos_final = len(lista_caracteres) - 1

while pos_inicial < pos_final:
    lista_caracteres[pos_inicial], lista_caracteres[pos_final] = lista_caracteres[pos_final], lista_caracteres[pos_inicial]
    pos_inicial += 1
    pos_final -= 1

string_invertida = "".join(lista_caracteres)
print(string_invertida)