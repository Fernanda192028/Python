# 1. Olá, mundo!
# Mostre na tela a mensagem "Olá, mundo!"
# Utilize a função print
print("Olá, mundo!")

# 2. Soma, subtração, multiplicação e divisão simples!
# Peça dois números inteiros ao usuário.
# Mostre a soma, subtração, multiplicação e divisão deles.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)

# 3. Maior de dois números
# Leia dois números inteiros.
# Mostre o maior deles.
# Utilize o condicional if / else.
# Não esqueça de considerar se forem iguais.

if n1 > n2:
    print("O maior número é:", n1)
elif n2 > n1:
    print("O maior número é:", n2)
else:
    print("Os dois números são iguais.")

# 4. Par ou ímpar
# Peça um número inteiro ao usuário.
# Diga se ele é par ou ímpar.
# Utilize o condicional if / else.

n = int(input("Digite um número: "))

if n % 2 == 0:
    print("É par.")
else:
    print("É ímpar.")

# 5. Calculadora de IMC
# Peça o peso e a altura de uma pessoa.
# IMC = peso / (altura ** 2)
# Mostre o resultado do IMC.

peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))
imc = peso / (altura ** 2)
print(f"IMC: {imc:.2f}")

