def entry_to_number(jog):
    if jog == "pedra":
        return 1;
    elif jog == "tesoura":
        return 2;
    elif jog == "papel":
        return 3;
    else:
        return 0;

def avalia_jogada(jog1, jog2):
    
    if jog1 == jog2:
        return -1;
    if jog1 == 1:
        if jog2 == 2:
            return 1;
        else:
            return 2;
    elif jog1 == 2:
        if jog2 == 1:
            return 2;
        else:
            return 1;
    elif jog1 == 3:
        if jog2 == 1:
            return 1;
        else:
            return 2; 

print("--- Pedra Papel Tesoura ---");

vit1 = 0;
vit2 = 0;

while True:

    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'

    while True:
        entrada = input("Entre com 1 para jogar e 0 para sair\n");
        if entrada == '0' or entrada == '1':
            break;
        else:
            print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE);
            print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE);
            print("Entrada invalida!");

    if entrada == '0': 
        print("Score final: 1: [" + str(vit1) + "] vs 2: [" + str(vit2) + "].");
        break;

    while True:
        entr1 = input("Primeiro jogador: ");
        jog1 = entry_to_number(entr1);
        
        if jog1 != 0:
            break;
        else:
            print("Entrada invalida, tente novamente! Entradas validas: pedra, papel, tesoura.");

    print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE);

    while True:
        entr2 = input("Segundo Jogador: ");
        jog2 = entry_to_number(entr2);

        if jog2 != 0:
            break;
        else: 
            print("Entrada invalida, tente novamente! Entradas validas: pedra, papel, tesoura.");

    print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE);
        
    if avalia_jogada(jog1, jog2) == -1:
        print("Partida Empatada");
    elif avalia_jogada(jog1, jog2) == 1:
        print("Vitoria do primeiro jogador! 1: [" + entr1 + "] vs 2: [" + entr2 + "].");
        vit1 += 1;
    elif avalia_jogada(jog1, jog2) == 2:
        print("Vitoria do segundo jogador! 1: [" + entr1 + "] vs 2: [" + entr2 + "]."); 
        vit2 += 1;

    print("Score: 1: [" + str(vit1) + "] vs 2: [" + str(vit2) + "].");
