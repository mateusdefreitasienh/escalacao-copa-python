
def cadastrar_jogador(selecao: dict, nome: str, posicao: str, clube: str):
    posicoes = ["GOLEIRO", "ZAGUEIRO", "LATERAL", "MEIA", "ATACANTE"]

    if posicao in posicoes:
        jogador = {"nome": nome, "posicao": posicao, "clube": clube}
        selecao["Jogadores"].append(jogador)
        print("Jogador cadastrado com sucesso!")
    else:
        print("Jogador não cadastrado! Corrija a posição informada!")
    return selecao

def formatar_jogador(jogador):
    msg = f"O jogador {jogador['nome']} joga no clube {jogador['clube']}"
    msg += f" como {jogador['posicao']}."
    return msg

def listar_todos(selecao):
    print(f"\n ========= Lista de todos os jogadores da {selecao['Seleção']} ========= ")
    for jogador in selecao["Jogadores"]:
        print(formatar_jogador(jogador))

def listar_por_posicao(selecao, posicao):
    print(f"\n ========= Lista de todos os jogadores da posição {posicao} da seleção {selecao['Seleção']} ========= ")
    for jogador in selecao["Jogadores"]:
        if jogador["posicao"] == posicao:
            print(formatar_jogador(jogador))