nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print("Resultado:", nome, "Adulto")
elif idade >= 12:
    print("Resultado:", nome, "Adolescente")
else:
    print("Resultado:", nome, "Criança")