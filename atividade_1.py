import os
os.system("cls || clear")
from dataclasses import dataclass

lista_dados = []
lista_filhos = []
lista__salario = []
contador = 0
def limpando_terminal():
    os.system("cls || clear")

def calculando_media(a):
     soma = sum(a)
     quantidade = len(a)
     media = soma / quantidade
     return media

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
                dados = Dados(
                salario = float(input("Digite o ganho salarial total de sua família: ")),
                numero_filho = int(input("Digite a quantidade de filhos em sua família: "))
                )
                lista__salario.append(dados.salario)
                lista_filhos.append(dados.numero_filho)
                lista_dados.append(dados)
                arquivo_familias = "pesquisa_prefeitura.txt"
                with open(arquivo_familias, "a") as arquivo_dados_familia:
                     for dados in lista_dados:
                          arquivo_dados_familia.write(f"{dados.salario}, {dados.numero_filho}\n")
                arquivo_dados_familia.close()
                limpando_terminal()

            case 2:

                contador_familia = 0
                media_salarial = calculando_media(lista__salario)
                media_filhos = calculando_media(lista_filhos)
                maior_salario = max(lista__salario)
                menor_salario = min(lista__salario)
                limpando_terminal()
                for familia in lista_dados:
                    contador_familia += 1
                print("\n=== Exibindo dados das famílias ===")
                print(f"Quantidade de famílias que responderam a pesquisa: {contador_familia}")
                print(f"Média de salarial: {media_salarial:.2f}")
                print(f"Média de número de filhos: {media_filhos:.2f}")
                print(f"Maior salário: {maior_salario}")
                print(f"Menor salário: {menor_salario}")

            case 3:
                print("\n Programa encerrado")
                break
            case _:
                  print("Opção inválida. Tente Novamente")





