import datetime
from datetime import datetime
import os
from Cliente import Cliente
from Loja import Loja

cliente1 = Cliente('Juliana')
cliente2 = Cliente('Brian')
cliente3 = Cliente('Camila')
cliente4 = Cliente('Ana')
cliente5 = Cliente('Joao')
loja1 = Loja('Bike legal', 10)
loja2 = Loja('Monster Bikes', 20)
loja3 = Loja('Bikes Bike', 5)


global cliente
clientes = [cliente1, cliente2, cliente3, cliente4, cliente5]
lojas = [loja1, loja2, loja3]

linha = '___________________________________________________________________'


def chamar_menu():
    os.system('cls')  # limpar a tela

    lista_opcoes = ['1. Consultar disponibilidade de bike', '2. Alugar bike(s)',
                    '3. Retornar bike(s)', '4. Consultar debito',
                    '5. Pagar debito', '6-Consultar sua locacao', '0. Sair']
    print('MENU')
    print(linha)
    print(*lista_opcoes, sep='\n')
    opcao = input("Selecione o numero da opcao desejada: ")
    return opcao


def imprimir_clientes():
    os.system('cls')  # limpar a tela
    print(f"Lista de clientes: ")
    # Cria uma lista com o numero da opcao
    lista_clientes = [str(i+1)+'-'+itens.nome for i,
                      itens, in enumerate(clientes)]
    print(*lista_clientes, sep=" / ")
    # Return para fazer a verificao caso alguma categoria seja selecionada
    return(len(lista_clientes))


def seleciona_cliente():
    verificador = imprimir_clientes()
    opcao = int(input('Selecione o numero do cliente desejado: '))
    while opcao not in [i for i in range(1, verificador+1)]:
        print("Opcao invalida!")
        opcao = int(input('Selecione o numero do cliente desejado: '))
    cliente = clientes[opcao-1]
    os.system('cls')  # limpar a tela
    return(cliente)


def imprimir_lojas():
    os.system('cls')  # limpar a tela
    print(f"Lista de lojas: ")
    print(linha)
    # Cria uma lista com o numero da opcao
    lista_lojas = [str(i+1)+'-'+itens.nome for i,
                   itens, in enumerate(lojas)]
    print(*lista_lojas, sep=" / ")
    # Return para fazer a verificao caso alguma categoria seja selecionada
    return(len(lista_lojas))


def seleciona_loja():
    verificador = imprimir_lojas()
    opcao = int(input('Selecione o numero da loja desejada: '))
    while opcao not in [i for i in range(1, verificador+1)]:
        print("Opcao invalida!")
        opcao = input('Selecione o numero da loja desejada: ')
    loja = lojas[opcao-1]
    os.system('cls')  # limpar a tela
    return(loja)


def seleciona_qtdBikes():
    qtdbikes = int(input('Digite a quantidade de bikes desejada: '))
    while not isinstance(qtdbikes, int) and qtdbikes <= 0:
        print("Quantidade invalida!")
        qtdbikes = int(input('Digite a quantidade de bikes desejada: '))
    return qtdbikes


def menu():
    # Imprime menue e seleciona a opcao
    opcao = chamar_menu()

    while opcao != '0':
        if opcao == '1':  # Consultar disponibilidade de bike
            loja = seleciona_loja()
            loja.consultar_bike()
        elif opcao == '2':  # Alugar bike(s)
            loja = seleciona_loja()
            qtdBikes = seleciona_qtdBikes()
            print(cliente.alugar_bike(loja, qtdBikes))
        elif opcao == '3':  # 3. Retornar bike(s)
            print(cliente.retornar_bike(cliente.lojaLocacao))
        elif opcao == '4':  # Consultar debito
            print(cliente.consultar_debito())
        elif opcao == '5':  # Pagar debito
            print(cliente.pagar_debito())
        elif opcao == '6':  # Consultar sua locacao
            print(cliente)
        else:
            os.system('cls')  # limpar a tela
            print("Opcao invalida!")
            menu()

        print(linha)
        input("Digite qualquer tecla para voltar para o menu:")
        menu()


cliente = seleciona_cliente()
menu()
# print(seleciona_cliente())
