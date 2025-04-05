# Exercicios para condicoes em Python, O usuario tentara adivinhar o numero escolhido pela maquina 
import random

print("Vamos jogar um jogo?")
print("voce devera adivinhar o numero que eu estou pensando")
print(" ele e entre 0 e 5")
num = int(input("digite o seu palpite:"))
num_maquina = random.randint(0,5)

if num == num_maquina:
  print("parabens voce acertou")
else:
    print(f"que pena voce errou o numero e  {num_maquina}")
