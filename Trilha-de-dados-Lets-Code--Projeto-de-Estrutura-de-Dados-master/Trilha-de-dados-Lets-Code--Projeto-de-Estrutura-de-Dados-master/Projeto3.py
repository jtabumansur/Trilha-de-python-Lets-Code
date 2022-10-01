from matriz import *


class Calculadora:
    tamanho_rio = []

    def __init__(self, matriz):
        self._matriz = matriz
        self._coordenadas = self.lista_coordenadas(
            matriz)  # Lista com as coordenadas dos rios
        self._lista_rios = []  # Lista para armazenar os tamanhos dos rios encontrados
        self._visitados = []  # Lista para registrar quais coordenadas ja foram visitadas

        self.calcula_rios(self._coordenadas[0], True)
        self.__str__()

    # getter setter for matriz
    @property
    def matriz(self):
        return self._matriz

    @matriz.setter
    def nome(self, matriz):
        self._matriz = matriz

    # Metodo para impressao do resultado - Para matrizes mto grandes a impressao e omitida
    def __str__(self):

        mensagem = ''
        print(*self.matriz, sep='\n') if len(self.matriz) <= 30 else ''
        mensagem += f"\nEncontrados {len(self._lista_rios)} rio(s)."
        mensagem += f"O maior rio mede: {max(self._lista_rios)}. "
        mensagem += f"Os outros tamanhos sao:" + ','.join(str(i) for i in sorted(self._lista_rios)) if len(
            self._lista_rios) <= 200 else ""
        mensagem += '\n________________________________________________________________________\n'
        return print(mensagem)

    # Metodo para pegar as coordenadas dos rios
    def lista_coordenadas(self, matriz):
        lista = []
        for x, linha in enumerate(matriz):
            for y, elemento in enumerate(linha):
                if elemento == 1:
                    lista.append((x, y))

        return lista

    # Funcao para calcular se a coordenada possui vizinhos adjascentes

    def calcula_vizinhos(self, coordenada):
        lista_vizinhos = []
        lista_vizinhos.append((coordenada[0], coordenada[1] - 1))
        lista_vizinhos.append((coordenada[0], coordenada[1] + 1))
        lista_vizinhos.append((coordenada[0] - 1, coordenada[1]))
        lista_vizinhos.append((coordenada[0] + 1, coordenada[1]))

        for vizinho in lista_vizinhos:
            if vizinho in self._coordenadas and vizinho not in self._visitados:
                self.calcula_rios(vizinho, False)

    # Funcao para calcular o tamanho dos rios

    def calcula_rios(self, coordenada, inicio=True):
        # Inicio segue em ordem a lista de coordenadas, ignorando as coordenadas ja visitadas
        if inicio:
            for item in self._coordenadas:
                if item not in self._visitados:
                    self._visitados.append(item)
                    Calculadora.tamanho_rio.append(1)
                    self.calcula_vizinhos(item)

                self._lista_rios.append(sum(Calculadora.tamanho_rio))if sum(
                    Calculadora.tamanho_rio) > 0 else ""
                Calculadora.tamanho_rio = []
            return self._lista_rios

        # Quando a funcao e chamada a partir de um vizinho ela aumenta o tamanho do rio e procura por adjascentes
        else:
            self._visitados.append(coordenada)
            Calculadora.tamanho_rio.append(1)
            self.calcula_vizinhos(coordenada)
            return False


matriz10 = gera_matriz(10, 10)
Calculadora(matriz10)

matriz30 = gera_matriz(30, 30)
Calculadora(matriz30)

matriz100 = gera_matriz(100, 100)
Calculadora(matriz100)
