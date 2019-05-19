print("*************************")
print("***** JOGO DA FORCA *****")
print("*************************")

print('1) Fácil')
print('2) Médio')
print('3) Difícil')
nivel = int(input("Escolha seu nível de dificuldade: "))
if(nivel == 1):
	erros = 20
elif(nivel == 2):
	erros = 10
elif(nivel == 3):
	erros = 5

palavra = list(input("informe a palavra: "))
letras_certas = len(palavra)*['_']
erradas = []
print(letras_certas)
print("")
acertou = False
enforcou = False

while(not acertou and not enforcou):
	chute = input('Qual letra?: ')
	if(chute in palavra):
		posicao = 0
		for letra in palavra:
			if (chute.upper() == letra.upper()):
				letras_certas[posicao] = letra
			posicao = posicao + 1
	else:
		erros -= 1
		erradas.append(chute)
	print("")
	acertou = '_' not in letras_certas
	enforcou = erros == 0
	print(letras_certas)
	print("")
	print('Letras erradas: {}'.format(erradas))
	print('Tem mais {} tentativas'.format(erros))
	print("")

if(acertou):
	print('VOCÊ GANHOU!')
else:
	print('VOCÊ PERDEU')
print('GAME OVER')
