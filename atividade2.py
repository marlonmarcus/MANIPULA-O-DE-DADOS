import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    email: str
    telefone: str

    def mostrar_dados_func(self):
        print(f"Nome: {funcionario.nome}")
        print(f"Email: {funcionario.email}")
        print(f"Telefone: {funcionario.telefone}")

lista_funcionario = []

for i in range(3):
    novo_funcionario = Funcionario(
        nome=input("Digite seu nome: "),
        email=input("Digite seu email: "),
        telefone=input("Digite seu telefone: ")
    )
    lista_funcionario.append(novo_funcionario)

for funcionario in lista_funcionario:
    funcionario.mostrar_dados_func()