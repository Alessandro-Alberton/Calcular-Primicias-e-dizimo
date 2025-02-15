#Crie um programa que calcule as primicias e dizimos
# Primeiro ele precisa pegar o valor total dividir por 30
# Segundo, ele pega o valor total menos o valor que foi dividido por 30 e multiplico por 10%
# importar o app, builder (GUI)
#Criar o aplicativo
# criar a função builder

from dataclasses import dataclass, replace
import os # Importa a biblioteca para limpar a tela

def inicio():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') #limpa o terminal
        try:
            valor_total = float(input("Digite o valor: "))

            primicias = (valor_total/30)
            print(f"Primicia: R${primicias:.2f}")


            dizimo = (valor_total - primicias) * 0.1
            print(f"Dizimo: R${dizimo:.2f}")


            resultado = float(input(f"Total: R${primicias + dizimo:.2f}"))

            input('\npressione enter para voltar ao inicio...') # Aguarda enter para reiniciar

            repetir = input("Deseja calcular novamente? (s/n): ")
            if repetir.lower() != "s":
                print("Encerrando...")
                break  # Sai do loop se o usuário não quiser repetir

        except ValueError:
         print("Erro! Digite um número válido.")
         input("\nPressione Enter para tentar novamente...")  # Aguarda Enter
         
        finally:
         print("Operação finalizada.")  # Sempre será executado
inicio()
