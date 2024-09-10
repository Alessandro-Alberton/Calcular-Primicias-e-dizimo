#Crie um programa que calcule as primicias e dizimos
# Primeiro ele precisa pegar o valor total dividir por 30
# Segundo, ele pega o valor total menos o valor que foi dividido por 30 e multiplico por 10%
# importar o app, builder (GUI)
#Criar o aplicativo
# criar a função builder

from dataclasses import replace

valor_total = float(input("Digite o valor: "))

primicias = (valor_total/30)
print(f"Primicia: R${primicias:,.2f}")


dizimo = (valor_total - primicias) * 0.1
print(f"Dizimo: R${dizimo:,.2f}")


resultado  = int(input(f"Total: R${primicias + dizimo:,.2f}"))

