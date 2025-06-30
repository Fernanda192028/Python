# 6. Calculo das médias 
# Peça do usuário dois números inteiros
#calcule a média aritmética simples 
#calcule a média ponderada
#considere os pesos 3 e 2
#calcule a média geométrica 
# utilize a biblioteca math para calcular a raiz quadrada
# math.sqrt(x*y)
#mostre o resultado das médias 

import math


x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))


media_simples = (x + y) / 2
media_ponderada = (3 * x + 2 * y) / (3 + 2)
media_geometrica = math.sqrt(x * y)


print(f"Média Simples: {media_simples:.2f}")
print(f"Média Ponderada: {media_ponderada:.2f}")
print(f"Média Geométrica: {media_geometrica:.2f}")



# 7. Descobrindo o número de lados de um polígono
# Peça a soma dos ângulos internos do usuário
#calcule o número de lados do polígono
#mostre a quantidade de lados


soma_dos_angulos = int(input("Digite a soma dos ângulos internos (em graus): "))

lados = (soma_dos_angulos // 180) + 2

if lados >= 3:
    print(f"O polígono tem {lados} lados.")
else:
    print("A soma informada não corresponde a um polígono válido.")


#8.Número elevado ao quadrado 
# Peça um número inteiro do usuário
# calcule quanto vale esse numero elevado ao quadrado
#mostre o resultado


numero = int(input("Digite um número inteiro: "))

quadrado = numero ** 2

print(f"{numero} elevado ao quadrado é {quadrado}.")


#9.Conversão de temperatura 
#Solicite ao usuário uma temperatura em graus Celsius
#Converta essa temperatura para graus Fahrenheit
#Mostre a temperatura 


C = float(input("Digite a temperatura em Celsius: "))

F = (9/5 * C) + 32

print(f"A temperatura em Fahrenheit é: {F:.2f}°F")


#10. Juntando texto com números 
#Solicite ao usuário seu nome
#Solicite ao usuário sua idade 
# Mostre uma mensagem no seguinte formato
# Olá, [nome]! Você tem [idade] anos.


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print("Olá, " + nome + "! Você tem " + str(idade) + " anos.")
