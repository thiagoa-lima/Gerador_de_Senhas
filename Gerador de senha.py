import random
import string

senha = []

# gerador de letras minúsculas
for i in range(0, 2):
    letra_maiuscula = random.choice(string.ascii_uppercase)
    senha.append(letra_maiuscula)

# gerador de letras maísculas
for i in range(0, 2):
    letra_minuscula = random.choice(string.ascii_lowercase)
    senha.append(letra_minuscula)

# gerador de números
for i in range(0, 2):
    numeros = random.choice(string.digits)
    senha.append(numeros)

# gerador de caracteres especiais
for i in range(0, 2):
    caracteres_especiais = random.choice(string.punctuation)
    senha.append(caracteres_especiais)

# embaralhar as letras
# print(senha)
random.shuffle(senha)
senha = "".join(senha)
print("")
print("-" * 20)
print(f"Sua senha é {senha}")
print("-" * 20)
print("")


# nome1 = string.ascii_lowercase
# print(nome1)
# nome2 = string.ascii_uppercase
# print(nome2)
# nome3 = string.digits
# print(nome3)
# nome4 = string.punctuation
# print(nome4)
# # letra_maiscula = chr(random.randint(ord("A"), ord("Z")))
# # print(letra_maiscula)