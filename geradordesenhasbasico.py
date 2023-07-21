import random
import time

# Escolhe uma letra maiúscula aleatoriamente com base no código ASCII
letra_maiuscula = chr(random.randint(65, 90))

# Escolhe uma letra minúscula aleatoriamente com base no código ASCII
letra_minuscula = chr(random.randint(97, 122))

# Escolhe outra letra minúscula aleatoriamente com base no código ASCII
letra_minuscula2 = chr(random.randint(97, 122))

# Lista de caracteres especiais
caracteres_especiais = ['!,', '@', '#', '*']

# Escolhe um dos caracteres especiais aleatoriamente e remove a vírgula, se houver
caracteres_especiais = random.choice(caracteres_especiais).replace(',', '')

# Lista para armazenar os números gerados aleatoriamente
lista_numeros = []

# Imprime um cabeçalho para o gerador de senhas
print(" GERADOR DE SENHAS ".center(35, '='))

# Aguarda o usuário digitar qualquer coisa para continuar
input("Digite qualquer coisa para gerar uma senha. ")
time.sleep(0.3)

# Imprime uma mensagem indicando que a senha está sendo gerada
print("Gerando senha...")
time.sleep(0.8)

# Gera 4 números aleatórios e os adiciona à lista_numeros
for i in range(4):
    numero = random.randint(0, 9)
    lista_numeros.append(numero)

# Transforma a lista de números em uma string e remove os colchetes e vírgulas
lista_numeros = str(lista_numeros)[1:-1].replace(',', '')

# Imprime a senha formada pelas letras e números aleatórios, sem espaços
print('\033[1:32mA sua senha será: ', end='')
senha = f'{letra_maiuscula}{caracteres_especiais}{letra_minuscula}{letra_minuscula2}{lista_numeros}'.replace(' ', '')
print(senha)

