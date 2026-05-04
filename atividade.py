import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Cliente:
    nome: str
    idade: int
    altura: float
    peso: float

    def mostrar_dados(self):
        print(f"Nome: {cliente.nome}")
        print(f"Idade: {cliente.idade}")
        print(f"Altura: {cliente.altura}")
        print(f"Peso: {cliente.peso}kg")    

lista_cliente = []

print("--- Solicitando Dados do Cliente ---")

for i in range(2):
    novo_cliente = Cliente(
        nome=input("Digite seu nome: "),
        idade=input("Digite sua idade: "),
        altura=input("Digite sua altura: "),
        peso=input("Digite seu peso: ")
    )
    lista_cliente.append(novo_cliente)


for cliente in lista_cliente:
    cliente.mostrar_dados()