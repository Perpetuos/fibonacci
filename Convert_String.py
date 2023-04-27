string = "exemplo de string"

# Transforma a string em uma lista de caracteres
lista_chars = list(string)

# Inverte a ordem dos caracteres na lista
for i in range(len(lista_chars)//2):
    temp = lista_chars[i]
    lista_chars[i] = lista_chars[-i-1]
    lista_chars[-i-1] = temp

# Transforma a lista de caracteres de volta em uma string
string_invertida = "".join(lista_chars)

print(string_invertida)
