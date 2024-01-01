import re  # importar a biblioteca

# pedir texto ao utilizador
def pedir_texto():
    texto = input("Digite o texto: ")
    return texto

# calcular o número de letras
def calcular_numero_letras(texto):
    letras = re.findall(r'[a-zA-Z]', texto)
    return len(letras)

# calcular o número de palavras
def calcular_numero_palavras(texto):
    palavras = texto.split()
    return len(palavras)

# calcular o número de frases
def calcular_numero_frases(texto):
    # considera que as frases terminam com ".", "!" ou "?"
    frases = re.split(r'[.!?]', texto)
    # remove elementos vazios resultantes do split
    frases = [frase for frase in frases if frase.strip()]
    return len(frases)

# calcula o L
def calcular_L(texto):
    num_letras = calcular_numero_letras(texto)
    num_palavras = calcular_numero_palavras(texto)
    L = num_letras / num_palavras
    return L

# calcula o S
def calcular_S(texto):
    num_frases = calcular_numero_frases(texto)
    num_palavras = calcular_numero_palavras(texto)
    S = num_frases / num_palavras
    return S

# calcula o CLI
def calcular_CLI(texto):
    L = calcular_L(texto)
    S = calcular_S(texto)
    CLI = 0.0588 * L - 0.296 * S - 15.8
    return CLI

# informa os limites do indice
def informar_indice(CLI):
    if CLI < 1:
        return "Inferior ao nível 1"
    elif CLI >= 16:
        return "Superior ao nível 16"
    else:
        return f"{CLI:.2f}"

# exemplo de uso
texto = pedir_texto()
num_letras = calcular_numero_letras(texto)
num_palavras = calcular_numero_palavras(texto)
num_frases = calcular_numero_frases(texto)
CLI = calcular_CLI(texto)

print(f"Número de letras: {num_letras}")
print(f"Número de palavras: {num_palavras}")
print(f"Número de frases: {num_frases}")
print(f"L: {calcular_L(texto):.2f}")
print(f"S: {calcular_S(texto):.2f}")
print(f"CLI: {CLI:.2f}")
print("Índice:", informar_indice(CLI))
