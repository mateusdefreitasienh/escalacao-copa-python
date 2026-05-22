from tools import *

selecao = {"Seleção": "Brasileira",
           "País": "Brasil",
           "Ano": 2026,
           "Jogadores": [
                { "nome": "Alisson", "posicao": "GOLEIRO", "clube": "Liverpool" },
                { "nome": "Ederson", "posicao": "GOLEIRO", "clube": "Manchester City" },
                { "nome": "Weverton", "posicao": "GOLEIRO", "clube": "Palmeiras" },
                { "nome": "Dani Alves", "posicao": "LATERAL", "clube": "UNAM Pumas" },
                { "nome": "Danilo", "posicao": "LATERAL", "clube": "Juventus" },
                { "nome": "Alex Sandro", "posicao": "LATERAL", "clube": "Juventus" },
                { "nome": "Emerson", "posicao": "LATERAL", "clube": "Real Betis" },
                { "nome": "Thiago Silva", "posicao": "ZAGUEIRO", "clube": "Chelsea" },
                { "nome": "Marquinhos", "posicao": "ZAGUEIRO", "clube": "PSG" },
                { "nome": "Éder Militão", "posicao": "ZAGUEIRO", "clube": "Real Madrid" },
                { "nome": "Bremer", "posicao": "ZAGUEIRO", "clube": "Juventus" },
                { "nome": "Casemiro", "posicao": "MEIA", "clube": "Manchester United" },
                { "nome": "Fabinho", "posicao": "MEIA", "clube": "Liverpool" },
                { "nome": "Fred", "posicao": "MEIA", "clube": "Manchester United" },
                { "nome": "Bruno Guimarães", "posicao": "MEIA", "clube": "Newcastle" },
                { "nome": "Lucas Paquetá", "posicao": "MEIA", "clube": "West Ham" },
                { "nome": "Neymar", "posicao": "ATACANTE", "clube": "Al Hilal" },
                { "nome": "Richarlison", "posicao": "ATACANTE", "clube": "Tottenham" },
                { "nome": "Vinícius Júnior", "posicao": "ATACANTE", "clube": "Real Madrid" },
                { "nome": "Raphinha", "posicao": "ATACANTE", "clube": "Barcelona" },
                { "nome": "Rodrygo", "posicao": "ATACANTE", "clube": "Real Madrid" },
                { "nome": "Gabriel Jesus", "posicao": "ATACANTE", "clube": "Arsenal" }]
            }

nome = input("Digite o nome do Jogador: ")
posicao = input("Digite a posição do Jogador (GOLEIRO, ZAGUEIRO, LATERAL, MEIA e ATACANTE): ").upper()
clube = input("Digite o clube do Jogador: ")

selecao = cadastrar_jogador(selecao, nome, posicao, clube)


print(selecao)
listar_todos(selecao)
listar_por_posicao(selecao, posicao="ATACANTE")
