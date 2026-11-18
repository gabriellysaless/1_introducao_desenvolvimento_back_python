contador = 1

while contador <= 10:
    print(contador)
    contador += 1

# while com input
senha = ""

while senha != "1234":
    senha = input("Digite a senha: ")

print("Acesso permitido!")

# break
cont = 1

while cont <= 10:
    if cont == 5:
        break

    print(cont)
    cont += 1

# while True (lembra o do while)
while True:
    password = input("Digite a senha: ")
    if password == "python123":
        break
    else:
        print("Senha Incorreta")
print("Acesso permitido!")