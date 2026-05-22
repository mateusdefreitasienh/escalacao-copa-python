# Sistema de Gestão da Seleção Brasileira

Com a nova convocação da Seleção Brasileira liberada recentemente, a comissão técnica precisa de uma ferramenta automatizada para organizar os jogadores convocados. Você foi contratado para desenvolver o protótipo desse sistema em Python, utilizando os conceitos de Estruturas de Dados Básicas (Listas e Dicionários) e Funções.

O objetivo principal é criar um sistema capaz de cadastrar os atletas, validar suas respectivas posições e gerar listagens específicas por setores do campo (Goleiros, Zagueiros, Meias, etc.).

---

## Requisitos do sistema

### Estrutura de Dados do Jogador
Cada jogador deve ser representado por um **dicionário** contendo as seguintes chaves:
- `nome`: Nome do atleta (String)
- `posicao`: Posição em que atua (String)
- `clube`: Clube atual do jogador (String)

### Armazenamento Global
O elenco completo da seleção deve ser armazenado em uma **lista dentro de um dicionário global** (ex: `elenco_selecao`), que guardará os dicionários de cada jogador cadastrado e terá as seguintes chaves:
- `selecao`: Nome da seleção (String)
- `pais`: País de origem da seleção (String)
- `ano`: Ano da escalação (String)

### Regra de Negócio (Validação)
O sistema só deve aceitar o cadastro de jogadores nas seguintes posições oficializadas:  
**GOLEIRO, ZAGUEIRO, LATERAL, MEIA, ATACANTE**  

Qualquer outra posição inserida deve ser rejeitada com uma mensagem de erro na tela.

### Funções Obrigatórias
Você deve implementar as seguintes funções para gerenciar o sistema:

- `cadastrar_jogador(nome, posicao, clube)`  
  Recebe os dados do atleta, valida se a posição é permitida e, caso seja, cria o dicionário do jogador e o adiciona à lista do elenco.

- `formatar_jogador(jogador)`  
  Recebe o dicionário de um jogador e retorna uma string formatada e amigável para exibição  
  *(Ex: "Vini Jr. (Real Madrid) - ATACANTE")*.

- `listar_todos()`  
  Percorre a lista do elenco e exibe na tela todos os jogadores convocados até o momento utilizando a função de formatação.

- `listar_por_posicao(posicao)`  
  Filtra e exibe na tela apenas os jogadores que atuam na posição informada.

---

## Orientações de Implementação

- **Padronização de Texto:**  
  Para evitar erros de digitação (ex: o usuário digitar "goleiro", "Goleiro" ou "GOLEIRO"), utilize o método `.upper()` do Python para padronizar as strings das posições sempre em letras maiúsculas antes de fazer as validações.

- **Script de Teste:**  
  No final do arquivo, utilize o bloco:
  ```python
  if __name__ == "__main__":

## Desafio adicional
- Criar um menu, questionando o que o usuaário quer fazer
- Limitar o cadastro em 26 jogadores