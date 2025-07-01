
# Exercícios 13, 14 e 15
# Autor: Adalove (2025)
# Estes exercícios são de minha autoria.

# 11. É triângulo?
# Peça os três lados de um triângulo 
# e a altura também.
# Informe se os valores podem formar um triângulo.
# Calcule a área do triângulo.

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))
h = float(input("Altura relativa à base (A): "))


if a + b > c and a + c > b and b + c > a:
    print("É um triângulo!")
    area = (a * h) / 2
    print(f"Área do triângulo: {area:.2f}")
else:
    print("Não é um triângulo.")

# 12. Ano bissexto
# Peça o ano do usuário.
# Informe se o ano é bissexto ou não.

ano = int(input("Digite um ano: "))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print("Ano bissexto")
else:
    print("Não é bissexto")

# 13. Área da circunferência maior
# Peça os raios de duas circunferências.
# π = 3.14
# Mostre qual área é maior.
# Considere se forem iguais.

r1 = float(input("Raio da 1ª circunferência: "))
r2 = float(input("Raio da 2ª circunferência: "))
pi = 3.14

area1 = pi * r1 ** 2
area2 = pi * r2 ** 2

if area1 > area2:
    print("A 1ª circunferência tem área maior.")
elif area2 > area1:
    print("A 2ª circunferência tem área maior.")
else:
    print("As áreas são iguais.")

# 14. Posição relativa entre circunferência e reta
# Solicite a distância do centro da circunferência à reta. 
# Solicite o raio da circunferência.
# Classifique como:
# Reta externa à circunferência
# Reta tangente à circunferência
# Reta secante à circunferência

d = float(input("Distância do centro da circunferência à reta: "))

r = float(input("Raio da circunferência: "))

if d > r:
    print("Reta externa à circunferência.")
elif d == r:
    print("Reta tangente à circunferência.")
else:
    print("Reta secante à circunferência.")
 

# 15. Moda, Mediana e Média (difícil)
# Lista definida de números 
# [1, 2, 3, 4, 5, 2, 4, 3, 3]
# Defina a moda, mediana e média. 
# Mostre o resultado.

# Lista fixa
numeros = [1, 2, 3, 4, 5, 2, 4, 3, 3]

# --- MÉDIA ---
soma = 0
for n in numeros:
    soma += n
media = soma / len(numeros)

# --- MEDIANA ---
ordenada = sorted(numeros)
tamanho = len(ordenada)

if tamanho % 2 == 1:
    # quantidade ímpar → pega o número do meio
    mediana = ordenada[tamanho // 2]
else:
    # quantidade par → média dos dois do meio
    meio1 = ordenada[tamanho // 2 - 1]
    meio2 = ordenada[tamanho // 2]
    mediana = (meio1 + meio2) / 2

# --- MODA  ---
maior_contagem = 0
moda = None

for num in numeros:
    contagem = 0
    for outro in numeros:
        if outro == num:
            contagem += 1
    if contagem > maior_contagem:
        maior_contagem = contagem
        moda = num

# --- Resultado final ---
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")


