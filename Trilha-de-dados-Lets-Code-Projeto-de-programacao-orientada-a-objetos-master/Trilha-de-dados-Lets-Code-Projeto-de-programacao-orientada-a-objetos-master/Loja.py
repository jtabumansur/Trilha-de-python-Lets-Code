import datetime
import math


from sqlalchemy import true
from HelperLogs import logs_loja as log


class Loja(object):
    def __init__(self, nome, nBiKes):
        self._nome = nome
        self._nBikes = nBiKes
        self._bikeAlugadas = 0

    # getter/setter para o nome da loja
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, qtdBikes):
        return self._nome

    # getter/setter para o numero de bikes da loja
    @property
    def nBikes(self):
        return self._nBikes

    @nBikes.setter
    def nBikes(self, qtdBikes):
        return self._nBikes

    # getter/setter para o numero de bikes alugadas da loja
    @property
    def bikeAlugadas(self):
        return self._bikeAlugadas

    @bikeAlugadas.setter
    def bikeAlugadas(self, qtdBikes):
        return self._bikeAlugadas

    # Funcao magica para imprimir as informacoes da loja
    def __repr__(self):
        return f"Loja [{self.nome}] - Possui[{self._nBikes}] bikes - [{self._nBikes - self._bikeAlugadas}] disponiveis para locacao"

   # Metodo para calcular o tempo de divida do cliente
    def calcular_tempo(self, cliente):
        bikeDevolvida = cliente.dtDevolucao != ''
        devolucao = cliente.dtDevolucao if bikeDevolvida else datetime.datetime.now()
        tempoLocacao = devolucao - cliente.dtLocacao
        dia = datetime.timedelta(days=1)
        semana = datetime.timedelta(days=7)
        if tempoLocacao >= semana:
            return 'semanas', math.ceil(tempoLocacao.days/7)
        elif tempoLocacao > dia:
            return ('dias', tempoLocacao.days)
        else:
            return ('horas', math.ceil(tempoLocacao.total_seconds()/3600))

    # Metodo para calcular o valor de divida do cliente
    def calcular_valor(self, cliente):
        nBikes = cliente.nBikesDebito
        unidade, tempo = self.calcular_tempo(cliente)
        if unidade == 'horas':
            valor = 5*tempo*nBikes
        elif unidade == 'dias':
            valor = 25*tempo*nBikes
        elif unidade == 'semanas':
            valor = 100*tempo*nBikes
        if nBikes >= 3:
            valor = valor*0.7
        print(
            f"Debito - [{nBikes}] bikes - Tempo de locacao: [{tempo} {unidade}(s)] - Saldo devedor R$ [{valor}]")
        return valor

    # Metodo para retornaro numero de bicletas disponivels em uma determinada loja para o cliente

    def consultar_bike(self):
        print(self)

    # Metodo para alugar bikes para um cliente
    # validando se a loja tem disponibilidade, se o cliente ja possui outrabike alugada ou alguma divida

    def alugar_bike(self, bikes_solicitadas, cliente):
        bikes_disponiveis = self._nBikes-self._bikeAlugadas
        try:
            if cliente.nBikesAlugadas == 0:
                if not cliente._divida:
                    if (bikes_solicitadas <= bikes_disponiveis):
                        self._bikeAlugadas += bikes_solicitadas
                        return True
                    else:
                        return 'A loja nao possui bikes o suficiente para esta locacao'
                else:
                    return 'Locacao nao efetuado porque o cliente possui dividas'
            else:
                loja = cliente.lojaLocacao
                return 'O cliente ja possui [' + str(cliente.nBikesAlugadas)+'] bikes alugadas na loja ' + loja.nome

        except Exception as e:
            return str(e)

    # Metodo para retornar a bike dos clientes
    # Validando se a devolucao e na loja correta
    def retornar_bike(self, qtdBike):
        try:
            self._bikeAlugadas -= qtdBike
            return True

        except Exception as e:
            return str(e)

    # Metodo para consultar o valor da divida do cliente
    def consultar_debito(self, cliente):
        try:
            if cliente.divida:
                if cliente.dtDevolucao != '':
                    valor = self.calcular_valor(cliente)
                    return('O valor da divida e R$' + str(valor))
                else:
                    valor = self.calcular_valor(cliente)
                    return('O valor da divida parcial e R$' + str(valor))
            else:
                return('O cliente nao possui dividas')
        except Exception as e:
            return str(e)

    # Metodo para aceitar pagamento da divida do cliente ##ASSUMINDO CLIENTE SUPER CONFIAVEL - SEM VALIDACAO
    def pagar_debito(self, cliente):
        try:
            if cliente.divida and cliente.dtDevolucao != '':
                return True
            elif cliente.divida and cliente.dtDevolucao == '':
                return 'O cliente precisa devolver a(s) bike(s) primeiro'
            else:
                return 'O cliente nao possui dividas'
        except Exception as e:
            return str(e)
