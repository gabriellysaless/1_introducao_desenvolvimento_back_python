# for
for numero in range(5):
    print(numero)

# continue
for num in range(1, 6):
    if num == 3:
        continue

    print(num)

# Iterando dados
frutas = ["maçã", "banana", "uva"]

for fruta in frutas:
    print(fruta)

# Iterando strings
for letra in "Python":
    print(letra)

# Iterando objetos
usuario = {"nome": "Carlos", "idade": 30, "cargo": "Desenvolvedor"}

for chave, valor in usuario.items():
    print(f"{chave}: {valor}") # f-string, ao invés de concatenar com + 