class Main:
    pass

print("Testando")

from Cliente import Cliente
from  Conta import  Conta


cliente1 = Cliente("Bruno", "13991742722")
conta = Conta(cliente1.get_nome(), 6565, 0)

#id
print(cliente1)
print(cliente1.get_nome(), "Telefone" , cliente1._telefone)

#printado conta e cliente
print(conta.get_titular(), "numero:", conta.get_numero(), "Seu saldo é de:", conta.saldo)

conta.deposita(100)
conta.saque(50)
conta.extrato()