# %% [markdown]
# """"
# Você foi contratado para desenvolver um sistema que irá auxiliá-los a escolher os produtos que irão
# receber desconto na próxima Black Friday.
#
# Para isso, você terá acesso a uma API que fornece alguns dados dos produtos: um ID (identificador único), o preço e a
# categoria do produto. Uma função pronta irá retornar para você o conjunto de dados já em formato adequado: uma lista de
# dicionários, onde cada dicionário representa um produto.
#
# Você deverá implementar as funções para listar todas as categorias, listar todos os produtos de uma categoria,
# identificar o produto mais barato e o mais caro de uma categoria e o top 10 de produtos mais baratos e mais caros de toda
# a base de dados.
#
# Você pode baixar a base de dados clicando aqui e o código pronto para auxiliá-lo clicando aqui. Renomeie a base de dados
# para dados.json.
#
# Leia atentamente os comentários no código fornecido. Não modifique a função já pronta e respeite os parâmetros e
# retorno solicitados nos comentários de cada função que você irá desenvolver.
#
# Atente-se ao prazo de entrega. Você pode entregar o seu exercício fazendo o upload do arquivo .py finalizado.
# """

# %%

import json
import os.path
import sys


def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um 
    produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados


# FUNCAO PARA LISTAR TODAS AS CATEGORIAS
    # O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    # Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    # Cuidado para não retornar categorias repetidas.

def listar_categorias(dados):
    {'''
        Funcao que recebe uma lista produtos e retorna uma lista contendo todas as categorias
    '''}

    lista_categorias = list({i['categoria'] for i in dados})
    return sorted(lista_categorias)

    ...


# LISTAR TODOS OS ITENS DE UMA CATEGORIA
    # O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    # O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    # Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.

def listar_por_categoria(dados, categoria):
    {'''
        Funcao que recebe uma lista de produtos e o nome da categoria e retorna somente
        os produtos dessa categoria. 
    '''}
    produtos_categoria = [i for i in dados if i['categoria'] == categoria]
    return produtos_categoria


# FUNCAO PARA RETORNAR O(S) PRODUTO(S) MAIS CARO DE UMA CATEGORIA
    # O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    # O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    # Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.

def produto_mais_caro(dados, categoria):
    '''
        Funcao que recebe uma lista de produtos e o nome da categoria e retorna uma lista contendo 
        o(s) produto(s) mais caros dessa categoria.
    '''

    itens_categoria = listar_por_categoria(dados, categoria)
    valor_maximo = max([float(i['preco'])for i in itens_categoria])
    mais_caro_categoria = [
        i for i in itens_categoria if float(i['preco']) == valor_maximo]

    return mais_caro_categoria
    ...


# FUNCAO PARA RETORNAR O(S) PRODUTO(S) MAIS BARATO DE UMA CATEGORIA
    #  O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    #  O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    #  Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.


def produto_mais_barato(dados, categoria):
    '''
        Funcao que recebe uma lista de produtos e o nome da categoria e retorna uma lista contendo 
        o(s) produto(s) mais baratos dessa categoria.
    '''
    itens_categoria = listar_por_categoria(dados, categoria)
    valor_minimo = min([float(i['preco'])for i in itens_categoria])
    mais_barato_categoria = [
        i for i in itens_categoria if float(i['preco']) == valor_minimo]

    return mais_barato_categoria
    ...


dados = obter_dados()
print(produto_mais_barato(dados, 'pc_gamer'))


# FUNCOES AUXILIARES PARAS AS FUNCOES top_10_caros E top_10_baratos

def dados_ordenados(dados, decrescente):
    '''
    Funcao recebe uma lista e um boleano e retorna a lista com os valores ordenados  
    '''
    valores_ordenados = sorted(
        set([float(i['preco']) for i in dados]), reverse=decrescente)
    return valores_ordenados


def retorna_lista_ordenada(valores, dados):
    '''
    #Recebe uma lista de valores e uma lista de produtos e retorna uma lista com todos os produtos que possuam 
    esses  valores
    '''
    lista_top_10 = []
    for valor in valores:
        for dado in dados:
            if(float(dado['preco']) == valor):
                lista_top_10.append(dado)

    return lista_top_10


# FUNCAO PARA ACHAR OS 10 PRODUTOS MAIS CAROS DA LISTA
    # O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    # Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.

def top_10_caros(dados):
    '''
        Funcao que recebe uma lista de produtos e retorna os 10 produtos mais caros dessa lista
    '''

    # SOLUCAO COM LAMBDA
    lista_top_10 = sorted(dados, key=lambda i: float(
        i['preco']), reverse=True)[0:10]

    # SOLUCAO SEM LAMBDA
    # Funcao que retorna os 10 maiores valores unicos
    maximo_10 = dados_ordenados(dados, True)[0:10]
    # Traz todos os produtos que tenham esses valores (pode ser mais de 10 em caso de empate)
    lista_top_10 = retorna_lista_ordenada(maximo_10, dados)
    return lista_top_10


# FUNCAO PARA ACHAR OS 10 PRODUTOS MAIS BARATOS DA LISTA


# O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
# Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.

def top_10_baratos(dados):
    '''
        Funcao que recebe uma lista de produtos e retorna os 10 produtos mais baratos dessa lista
    '''
    # SOLUCAO COM LAMBDA
    lista_bottom_10 = sorted(dados, key=lambda i: float(i['preco']))[0:10]

    # SOLUCAO SEM LAMBDA

    # Funcao que retorna os 10 menores valores
    minimo_10 = dados_ordenados(dados, False)[0:10]
    # Traz todos os produtos que tenham esses valores (pode ser mais de 10 em caso de empate)
    lista_bottom_10 = retorna_lista_ordenada(minimo_10, dados)
    return lista_bottom_10


# FUNCOES AUXILIARES DO MENU
linha = '___________________________________________________________________'

################################################


def chama_menu():
    '''
    Funcao para imprimir a lista de opcoes do menu
    '''
    os.system('cls')  # limpar a tela

    lista_opcoes = ['1. Listar categorias', '2. Listar produtos de uma categoria',
                    '3. Produto mais caro por categoria', '4. Produto mais barato por categoria',
                    '5. Top 10 produtos mais caros', '6. Top 10 produtos mais baratos', '0. Sair']
    print('MENU')
    print(linha)
    print(*lista_opcoes, sep='\n')
    opcao = input("Selecione o numero da opcao desejada: ")
    return opcao


def selecionar_categoria(dados):
    '''
    Funcao que imprime a lista de categorias e pede para o usuario selecionar uma
    '''
    verificador = imprime_lista_categorias(dados)
    print(linha)
    opcao = input('Selecione o numero da categoria desejada: ')
    while opcao not in [str(i) for i in range(1, verificador+1)]:
        print("Opcao invalida!")
        opcao = input('Selecione o numero da categoria desejada: ')
    os.system('cls')  # limpar a tela
    categoria = listar_categorias(dados)[int(opcao)-1]

    return(categoria)


def imprime_lista_categorias(dados):
    '''
    Funcao para imprimir a lista de categorias 
    '''
    os.system('cls')  # limpar a tela

    print(f"Lista de categorias: ")
    print(linha)
    # Cria uma lista com o numero da opcao
    lista = [str(i+1)+'-'+itens for i,
             itens in enumerate(listar_categorias(dados))]
    print(*lista, sep=" / ")

    # Return para fazer a verificao caso alguma categoria seja selecionada
    return(len(lista))


def imprime_lista_produtos_categoria(dados):
    '''
    Funcao que seleciona a categoria e imprime os dados
    '''
    # Escolhe a categoria
    categoria = selecionar_categoria(dados)

    # Cabecalho e impressao dos dados
    print(f"Produtos da categoria {categoria}")
    print(linha)
    print(*listar_por_categoria(dados, categoria), sep='\n')


def imprime_produto(dados, valor):
    '''
    Funcao para selecionar a categoria e imprimir o produto mais caro ou mais barato da categoria
    '''
    # Escolhe a categoria
    categoria = selecionar_categoria(dados)

    # Cabecalho e impressao dos dados
    print(f"Produto mais {valor} da categoria {categoria}")
    print(linha)
    if valor == 'caro':
        print(produto_mais_caro(dados, categoria))
    else:
        print(produto_mais_barato(dados, categoria))


def imprime_lista_10(dados, valor):
    '''
    Funcao para imprimir os 10 produtos mais caros ou mais baratos da lista
    '''
    os.system('cls')  # limpar a tela

    # Cabecalho e impressao dos dados
    print(f"Lista dos 10 produtos mais {valor}")
    print(linha)
    if valor == 'caros':
        print(*top_10_caros(dados), sep='\n')
    else:
        print(*top_10_baratos(dados), sep='\n')

# MENU
    # O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    # Essa função deverá, em loop, realizar as seguintes ações:
    #   - Exibir as seguintes opções:
    #       1. Listar categorias/2. Listar produtos de uma categoria/3. Produto mais caro por /4. Produto mais barato por categoria/
    #       5. Top 10 produtos mais caros/6. Top 10 produtos mais baratos/0. Sair
    #   - Ler a opção do usuário.
    #   - No caso de opção inválida, imprima uma mensagem de erro.
    #   - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    #   - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    #   - Imprimir o retorno salvo.
    # O loop encerra quando a opção do usuário for 0.


def menu(dados):
    # Imprime menue e seleciona a opcao
    opcao = chama_menu()

    # # Validacao dos dados para facilitar a comprensao do menu if,elif, else
    # lista_categorias, listar_produtos_categoria, produto_mais_caro_categoria, produto_mais_barato_categoria,\
    #     top_10_mais_caros, top_10_mais_baratos, continuar = validador_menu(
    #         opcao)

    while opcao != '0':
        if opcao == '1':  # lista_categorias
            imprime_lista_categorias(dados)

        elif opcao == '2':  # listar_produtos_categoria
            imprime_lista_produtos_categoria(dados)

        elif opcao == '3':  # produto_mais_caro_categoria
            imprime_produto(dados, 'caro')

        elif opcao == '4':  # produto_mais_barato_categoria
            imprime_produto(dados, 'barato')

        elif opcao == '5':  # top_10_mais_caros
            imprime_lista_10(dados, 'caros')

        elif opcao == '6':  # top_10_mais_baratos
            imprime_lista_10(dados, 'baratos')

        else:
            os.system('cls')  # limpar a tela
            print("Opcao invalida!")
            menu(dados)

        print(linha)
        input("Digite qualquer tecla para voltar para o menu:")
        menu(dados)


d = obter_dados()
menu(d)
