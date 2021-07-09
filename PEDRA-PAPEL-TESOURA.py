import random

def title():
    print('''\033[91m
    
     
 ░░░░░██╗░█████╗░░██████╗░░█████╗░  ░░░░░██╗░█████╗░░██████╗░██╗░░░██╗███████╗███╗░░░███╗██████╗░░█████╗░
 ░░░░░██║██╔══██╗██╔════╝░██╔══██╗  ░░░░░██║██╔══██╗██╔═══██╗██║░░░██║██╔════╝████╗░████║██╔══██╗██╔══██╗
 ░░░░░██║██║░░██║██║░░██╗░██║░░██║  ░░░░░██║██║░░██║██║██╗██║██║░░░██║█████╗░░██╔████╔██║██████╔╝██║░░██║
 ██╗░░██║██║░░██║██║░░╚██╗██║░░██║  ██╗░░██║██║░░██║╚██████╔╝██║░░░██║██╔══╝░░██║╚██╔╝██║██╔═══╝░██║░░██║
 ╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝  ╚█████╔╝╚█████╔╝░╚═██╔═╝░╚██████╔╝███████╗██║░╚═╝░██║██║░░░░░╚█████╔╝
 ░╚════╝░░╚════╝░░╚═════╝░░╚════╝░  ░╚════╝░░╚════╝░░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░░░░╚═╝╚═╝░░░░░░╚════╝░
    
 \033[0m''')
    print('''
    ESCOLHA UM NUMERO PARA A OPÇÃO:
    
    0- PEDRA
    1- PAPEL
    2- TESOURA

    ''')

def gerador():
    opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
    computador = random.choice(opcoes)
    return computador

def jogo():
    title()
    computador = gerador()
    jogador = int(input("Digite a sua jogada: "))

    if computador == "PEDRA":
        print("O computador escolheu: Pedra")
        if jogador == 0:
            print("----\033[91mEMPATE!\033[0m----")
        elif jogador == 1:
            print("----\033[92mAEEEE!!!!! VOCÊ GANHOUUUU!!!!\033[0m----")
        elif jogador == 2:
            print("----\033[91mVOCÊ PERDEU!\033[0m----")
        else:
            print("----\033[91mNÚMERO INVALIDO\033[0m----")
    
    elif computador == "PAPEL":
        print("O computador escolheu: Papel")
        if jogador == 0:
            print("----\033[91mVOCÊ PERDEU!\033[0m----")
        elif jogador == 1:
            print("----\033[91mEMPATE!\033[0m----")
        elif jogador == 2:
            print("----\033[92mAEEEE!!!!! VOCÊ GANHOUUUU!!!!\033[0m----")
        else:
            print("----\033[91mNÚMERO INVALIDO\033[0m----")
        
    elif computador == "TESOURA":
        print("O computador escolheu: Tesoura")
        if jogador == 0:
            print("----\033[92mAEEEE!!!!! VOCÊ GANHOUUUU!!!!\033[0m----")
        elif jogador == 1:
            print("----\033[91mVOCÊ PERDEU!\033[0m----")
        elif jogador == 2:
            print("----\033[91mEMPATE!\033[0m----")
        else:
            print("----\033[91mNÚMERO INVALIDO\033[0m----")
    else:
        print("----\033[91mNÚMERO INVALIDO\033[0m----")
    
    print('-----------------------------------------------')
    print('Você deseja jogar novamente? \n 1- SIM \n 2- NÃO')
    option = int(input('-==>'))
    if option == 1:
        jogo()
    else:
        exit()
 
if __name__ == '__main__':
    jogo()
else:
    exit()