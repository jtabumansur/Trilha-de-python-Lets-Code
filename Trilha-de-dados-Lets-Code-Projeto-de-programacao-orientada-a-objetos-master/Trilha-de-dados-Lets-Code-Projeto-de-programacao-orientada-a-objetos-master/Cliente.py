import datetime
from Loja import Loja
from HelperLogs import logs_cliente as log
from itertools import count


class Cliente(object):

    def __init__(self, nome):
        self.nome = nome
        self._nBikesAlugadas = 0
        self._nBikesDebito = 0
        self._dtLocacao = ''
        self._dtDevolucao = ''
        self._lojaLocacao = ''
        self._divida = False

    # getter/setter para o numero de bikes alugadas
    @property
    def nBikesAlugadas(self):
        return self._nBikesAlugadas

    @nBikesAlugadas.setter
    def nBikesAlugadas(self, qtdBikes):
        return self._nBikesAlugadas

    # getter/setter para o numero de bikes em debito
    @property
    def nBikesDebito(self):
        return self._nBikesDebito

    @nBikesDebito.setter
    def nBikesDebito(self, qtdBikes):
        return self._nBikesDebito

    # getter/setter para a data de locacao
    @property
    def dtLocacao(self):
        return self._dtLocacao

    @dtLocacao.setter
    def dtLocacao(self, data):
        return self._dtLocacao

    # getter/setter para a data de devolucao
    @property
    def dtDevolucao(self):
        return self._dtDevolucao

    @dtDevolucao.setter
    def dtDevolucao(self, data):
        return self._dtDevolucao

    # getter/setter para a loja de locacao
    @property
    def lojaLocacao(self):
        return self._lojaLocacao

    @lojaLocacao.setter
    def lojaLocacao(self, loja):
        return self._lojaLocacao

    @property
    def divida(self):
        return self._divida

    @divida.setter
    def divida(self, boleano):
        return self._divida

    # Metodo para adicionar locacao
    def alugar(self, qtdbikes, loja):
        self._dtLocacao = datetime.datetime.now()
        self._nBikesAlugadas = qtdbikes
        self._nBikesDebito = qtdbikes
        self._lojaLocacao = loja
        self._divida = True

    # Metodo para devolucao de bikes

    def devolucao(self):
        self._nBikesAlugadas = 0
        self._dtDevolucao = datetime.datetime.now()

    # Metodo para pagar divida

    def pagardivida(self):
        self._nBikesAlugadas = 0
        self._lojaLocacao = ''
        self._dtLocacao = ''
        self._dtDevolucao = ''
        self._nBikesDebito = 0
        self._divida = False

    # Metodo para visualizar as informacoes do cliente
    def __repr__(self) -> str:
        return(f"Cliente : {self.nome} \nNumero de bikes alugadas: {self.nBikesAlugadas} \
               \nData da locacao : {self.dtLocacao} \nData da Devolucao: {self.dtDevolucao}")

    def alugar_bike(self, loja, qtdBikes):
        try:
            if isinstance(loja, Loja):
                if isinstance(qtdBikes, int) and qtdBikes > 0:
                    respostaloja = loja.alugar_bike(qtdBikes, self)
                    if respostaloja == True:
                        self.alugar(qtdBikes, loja)
                        return 'Cliente ' + self.nome + ' alugou [' + str(qtdBikes)+'] na loja ' + loja.nome
                    else:
                        return respostaloja
                else:
                    return 'Quantidade invalida'
            else:
                return 'Loja invalida'
        except Exception as e:
            return e

    # Metodo para retornar as bikes em uma loja especifica
    #  validando antes se  a loja e valida e se o cliente possui alguma bike para devolucao
    def retornar_bike(self, loja):
        try:
            if self._nBikesAlugadas > 0:
                if isinstance(loja, Loja):
                    if self.lojaLocacao == loja:
                        respostaloja = loja.retornar_bike(self.nBikesAlugadas)
                        if respostaloja == True:
                            self.devolucao()
                            return 'Bike(s) retornada(s) com sucesso'
                        else:
                            return respostaloja
                    else:
                        if isinstance(self.lojaLocacao, Loja):
                            return 'A(s) bike(s) deve(m) ser devolvida(s) na loja ' + self.lojaLocacao.nome
                else:
                    return 'Loja invalida'
            else:
                return 'Cliente nao possui nenhuma bike para devolucao'
        except Exception as e:
            return e

    # Metodo para consultar a divida do cliente
    #  validando antes se o cliente possui alguma bike para devolucao
    def consultar_debito(self):
        try:
            if self.lojaLocacao != '':
                if isinstance(self.lojaLocacao, Loja):
                    respostaloja = self.lojaLocacao.consultar_debito(self)
                return respostaloja
            return 'O cliente nao possui dividas'
        except Exception as e:
            return e

    # Metodo para pagar a loja ##ASSUMINDO CLIENTE SUPER CONFIAVEL - SEM VALIDACAO
    def pagar_debito(self):
        try:
            if isinstance(self.lojaLocacao, Loja):
                pagamento = self.lojaLocacao.pagar_debito(self)
                if pagamento == True:
                    self.pagardivida()
                    return 'Divida paga com sucesso'
                else:
                    return pagamento
            else:
                return 'Loja invalida'

        except Exception as e:
            return e
