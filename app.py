from tools import *

selecao = {"Seleção": "Brasileira",
           "País": "Brasil",
           "Ano": 2026,
           "Jogadores": [
                { "nome": "Alisson", "posicao": "GOLEIRO", "clube": "Liverpool" },
                { "nome": "Ederson", "posicao": "GOLEIRO", "clube": "Manchester City" },
                { "nome": "Dani Alves", "posicao": "LATERAL", "clube": "UNAM Pumas" },
                { "nome": "Danilo", "posicao": "LATERAL", "clube": "Juventus" },
                { "nome": "Alex Sandro", "posicao": "LATERAL", "clube": "Juventus" },
                { "nome": "Thiago Silva", "posicao": "ZAGUEIRO", "clube": "Chelsea" },
                { "nome": "Marquinhos", "posicao": "ZAGUEIRO", "clube": "PSG" },
                { "nome": "Éder Militão", "posicao": "ZAGUEIRO", "clube": "Real Madrid" },
                { "nome": "Casemiro", "posicao": "MEIA", "clube": "Manchester United" },
                { "nome": "Fabinho", "posicao": "MEIA", "clube": "Liverpool" },
                { "nome": "Lucas Paquetá", "posicao": "MEIA", "clube": "West Ham" },
                { "nome": "Neymar", "posicao": "ATACANTE", "clube": "Al Hilal" },
                { "nome": "Richarlison", "posicao": "ATACANTE", "clube": "Tottenham" },
                { "nome": "Gabriel Jesus", "posicao": "ATACANTE", "clube": "Arsenal" }]
            }


# Menu

print("Bem vindo ao sistema de cadastramento de Seleções")

msg = "Digite 1 para cadastrar jogadores\n"
msg += "Digite 2 para listar todos os jogadores \n"
msg += "Digite 3 para listar todos os jogadores por posição\n"
msg += "Digite 0 para sair\n"

cmd = ""

while True:
    cmd = input(msg)
    if cmd == "1":
        nome = input("Digite o nome do Jogador: ")
        posicao = input("Digite a posição do Jogador (GOLEIRO, ZAGUEIRO, LATERAL, MEIA e ATACANTE): ").upper()
        clube = input("Digite o clube do Jogador: ")

        selecao = cadastrar_jogador(selecao, nome, posicao, clube)
    elif cmd == "2":
        listar_todos(selecao)
    elif cmd == "3":
        posicao = input("Digite a posição do Jogador (GOLEIRO, ZAGUEIRO, LATERAL, MEIA e ATACANTE): ").upper()
        listar_por_posicao(selecao, posicao)
    elif cmd == "0":
        print("Sistema encerrado!")
        break
    else:
        print("Comando inválido!")