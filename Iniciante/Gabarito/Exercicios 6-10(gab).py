# Exercícios 6, 7 e 10
# Autor: Adalove (2025)
# Estes exercícios são de minha autoria.

# 6. Cálculo das médias (difícil)
# Peça ao usuário dois números inteiros.
# Calcule a média aritmética simples.
# Calcule a média ponderada (pesos 3 e 2).
# Calcule a média geométrica (use math.sqrt(x * y)).
# Mostre o resultado das médias.

import math

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

media_simples = (x + y) / 2
media_ponderada = (x * 3 + y * 2) / 5
media_geometrica = math.sqrt(x * y)

print("Média aritmética:", media_simples)
print("Média ponderada:", media_ponderada)
print("Média geométrica:", media_geometrica)

# 7. Descobrindo o número de lados de um polígono
# Peça a soma dos ângulos internos ao usuário.
# Calcule o número de lados do polígono.
# Fórmula: soma = (lados - 2) * 180
# Mostre a quantidade de lados.

soma = int(input("Digite a soma dos ângulos internos (em graus): "))
lados = (soma // 180) + 2
print("O polígono tem", lados, "lados.")

# 8. Número elevado ao quadrado
# Peça um número inteiro ao usuário.
# Calcule quanto vale esse número elevado ao quadrado.
# Mostre o resultado.

numero = int(input("Digite um número inteiro: "))
quadrado = numero ** 2
print("O quadrado de", numero, "é", quadrado)

# 9. Conversão de temperatura
# Solicite ao usuário uma temperatura em graus Celsius.
# Converta essa temperatura para graus Fahrenheit.
# Fórmula: F = (9/5 * C) + 32
# Mostre a temperatura convertida.

C = float(input("Digite a temperatura em Celsius: "))
F = (9 / 5 * C) + 32
print("A temperatura em Fahrenheit é:", F)

# 10. Juntando texto com números
# Solicite ao usuário seu nome.
# Solicite ao usuário sua idade.
# Mostre uma mensagem no seguinte formato:
# Olá, [nome]! Você tem [idade] anos.

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(f"Olá, {nome}! Você tem {idade} anos.")

