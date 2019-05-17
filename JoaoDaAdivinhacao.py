#valor = input("Login: \n")
#senha = input("Senha: \n")
#print(" Bem vindo {}, sua senha é {}".format(valor,senha))
print("*******************************")
print("***** JOGO DA ADIVINHAÇÃO *****")
print("*******************************")
print()
print("1) Fácil")
print("2) Médio")
print("3) Dífcil")
nivel = int(input("Escolha um nível de dificuldade: "))

if(nivel == 1):
  total_de_tentativas = 20  
elif(nivel == 2):
    total_de_tentativas = 10
elif(nivel == 3):
    total_de_tentativas = 5

pontos = 1000
from random import randint
numero_secreto = randint(0,100)

for rodada in range(1, total_de_tentativas):
    
    print("*******************************")
    print("***** JOGO DA ADIVINHAÇÃO *****")
    print("*******************************")
    numero = int(input("Digite um numero: \n"))
    print("")
    if numero == numero_secreto:
        print("ACERTOU")
        break
    elif(numero > numero_secreto):
        print("numero maior que o esperado")
        pontos = pontos - (numero - numero_secreto)
    elif(numero < numero_secreto):
        print("numero menor que o esperado")
        pontos = pontos - (numero_secreto - numero)

    print("tentativa {} de {}".format(rodada, total_de_tentativas))
    print("Pontos: {}".format(pontos))
    print("")
print("END GAME!")
print("Pontuação final: {}".format(pontos))
