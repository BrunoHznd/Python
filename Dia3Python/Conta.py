class Conta:
    def __init__(self, titular, numero, saldo):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo



    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,valor):
        if(valor < 0):
            print("O saldo não pode ser negativo")
        else:
            self._saldo = valor

    def get_numero(self):
        return self._numero

    def set_numero(self, numero):
        self._numero = numero


    def get_titular(self):
        return self._titular

    def set_titular(self, titular):
        self._titular = titular


    #metodos
    def saque(self, valor):
        if(self.saldo>=valor):
            self.saldo-=valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo Insuficiente")


    #outro metodo
    def deposita(self,valor):
        self.saldo+=valor


    #outro metodo
    def extrato(self):
        print("Cliente: ", self._titular, " Saldo Atual: ", self._saldo)