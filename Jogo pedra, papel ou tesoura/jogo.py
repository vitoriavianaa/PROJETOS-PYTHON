import random

print('VAMOS JOGAR PEDRA, PAPEL, TESOURA?')

while True:
    escolha = input("Escolha o seu: ")

    lista = ['pedra', 'papel', 'tesoura']
    item_escolhido = random.choice(lista)

    if escolha == item_escolhido:
        print(f'Computador: {item_escolhido}!')
        print('Empate!')
    elif escolha == 'pedra' and item_escolhido == 'tesoura':
        print(f'Computador: {item_escolhido}!')
        print('Você VENCEU!')
    elif escolha == 'tesoura' and item_escolhido == 'papel':
        print(f'Computador: {item_escolhido}!')
        print('Você VENCEU!')
    elif escolha == 'papel' and item_escolhido == 'pedra':
        print(f'Computador: {item_escolhido}!')
        print('Você VENCEU!')
    else:
        print(f'Computador: {item_escolhido}!')
        print('Você PERDEU!')

    resposta = input('DE NOVO? (s/n): ')
    if resposta.lower() != 's':
        break

print('Fim do jogo!')
