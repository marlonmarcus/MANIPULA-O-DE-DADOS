import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pet:
    nome: str
    idade: int
    raca: str

    def mostrar_dadospet(self):
        print(f"Nome: {pet.nome}")
        print(f"Idade: {pet.idade}")
        print(f"Raça: {pet.raca}")

lista_pet = []

for i in range(2):
    mais_pet = Pet(
        nome=input("DIgite o nome do pet: "),
        idade=input("Digite a idade do pet: "),
        raca=input("Digite a raça do pet: ")
    )
    lista_pet.append(mais_pet)
    mais_pet = input("Deseja cadastrar mais algum pet? (S/N): ").lower()
    if mais_pet == "n":
        break

for pet in lista_pet:
    pet.mostrar_dadospet()