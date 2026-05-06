import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Carro:
    marca: str
    modelo: str
    ano: str

    def mostrar_dados_carro(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

lista_carro = []

while True:
    os.system("cls")

    print("""--- ESSA É UMA PESQUISA PRA DESCOBRIR SEUS CARROS PREFERIDOS ---""")

    novo_carro = Carro(
        marca=input("Digite a marca do carro: "),
        modelo=input("Digite o modelo do carro: "),
        ano=input("Digite o ano do carro: ")
    )
    lista_carro.append(novo_carro)
    
    with open("cadastro_carro.csv", "a", encoding="UTF-8") as arquivo:
        for carro in lista_carro:
            arquivo.write(f"{carro.marca}, {carro.modelo}, {carro.ano}\n")
        print("ARQUIVO SALVO COM SUCESSO!")

    outro_carro = input("Deseja cadastrar outro veículo? (S ou N): ").lower()
    if outro_carro == "s":
        continue
    else:
        break