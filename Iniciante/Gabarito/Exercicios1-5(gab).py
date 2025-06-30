# 1.Olá mundo! 
# Mostre na tela uma mensegem "Olá mundo!" 
# Utilize a função print 
print("Olá mundo!")


# 2.Soma, subtração, multiplicação e divisão simples! 
# Peça dois números inteiros ao usário
# Mostre a soma,subtração, multiplicação e divisão deles 


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


# 3.Maior de dois números
# Leia dois números inteiros
# mostre o maior deles
# utilize o condional if / else
# não esqueça de considerar se forem iguais


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print("O maior número é:", n1)
elif n2 > n1:
    print("O maior número é:", n2)
else:
    print("Os dois números são iguais.")


# 4.Par ou ímpar
# Peça um número inteiro ao usúario
# diga se ele é par ou ímpar
# utilize o condicional if / else

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


# 5.Calculadora de IMC
# Peça o peso e a altura de uma pessoa
# IMC = peso / (altura ** 2)
# Mostre o resultado do IMC

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print("Seu IMC é:", round(imc, 2))
