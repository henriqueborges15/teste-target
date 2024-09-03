print('-'*30)
string = input("Digite o que deseje inverter: ")


def modificar_string(s):
    inverter_string = ""
    for i in range(len(s) -1, -1, -1):
        inverter_string = inverter_string + s[i]
    return inverter_string

string_invertida = modificar_string(string)

print('-'*30)
print(f"A palavra {string} invertida: {string_invertida} ")
print('-'*30)