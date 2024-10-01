import os
os.system("cls || clear")
from dataclasses import dataclass

lista_dados = []
lista_filhos = []
lista__salario = []
contador = 0
def limpando_terminal():
    os.system("cls || clear")

@dataclass
class Dados:
    salario: float
    numero_filho: int

while True:
        print("""
        Código | Descricão
        1    | Adicionar família  
        2    | Exibir resultados
        3    | Sair
        """)
        opcao = int(input("\nDigite a opção que deseja selecionar: "))
        match opcao:
            case 1:
                print("\n=== Solicitando dados das famílias ===")
                dados = Dados(
                salario = float(input("Digite o quanto de salário você ganha: ")),
                numero_filho = int(input("Digite o número de filhos na sua família: "))
                )
                lista_dados.append(dados)
                arquivo_familias = "pesquisa_prefeitura.txt"
                with open(arquivo_familias, "a") as arquivo_dados_familia:
                     for dados in lista_dados:
                          arquivo_dados_familia.write(f"{dados.salario}, {dados.numero_filho}\n")
                arquivo_dados_familia.close()
            case 2:
                for familia in lista_dados:
                    print("\n=== Exibindo dados da família ===")
                    print(f"Salário: {dados.salario}")
                    print(f"Número de filhos: {dados.numero_filho}")
                    with open(arquivo_familias, "r") as arquivo_dados_familia:
                        for linha in arquivo_dados_familia:
                            nome, idade = linha.strip().split(",")
                            lista_dados.append(Dados(salario=lista__salario, numero_filho=))
            case 3:
                break





lista__salario.append(dados.salario)
lista_filhos.append(dados.numero_filho)
