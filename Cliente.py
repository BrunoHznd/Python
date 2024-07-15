class Cliente:
    #A palavra reservada representa o objeto em si, portanto, sempre que quisermos especificar atributos de objetos, devemos associá-lo à palavra reservada self.
    def __init__(self, nome, telefone):
        #adicionando underline encapsula o atributo
        self._nome = nome
        self._telefone = telefone
        #Para adicionar atributos a uma classe, basta definir o nome do atributo acompanhado da palavra reservada self, no método especial denominado _ _init_ _ do Método Construtor.



    #utilizamos a palavra reservada pass quando nenhuma estrutura sera definida no corpo da classe
    #pass



#GET = é utilizado para ler os valores internos do objetos e envia-los como valor de retorno da função

    def get_nome(self):
        return self._nome
#SET = recebem argumentos que serao atribuidos a membros internos do objeto

    def set_nome(self, nome):
        self._nome = nome




    def get_telefone(self):
        return self._telefone

    def set_nome(self, telefone):
        self._telefone = telefone
