from colorama import Fore, Style
from colorama import init

init()

# Lista com os níveis do reservatório

niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]
# Função para definir a cor de cada nível 

def definir_cor(nivel):

    if nivel == 1 :
        return Fore.RED

    elif nivel == 2:
        return Fore.YELLOW

    elif nivel == 3 :
        return Fore.GREEN

    elif nivel == 4 :
        return Fore.CYAN

    elif nivel == 5 :
        return Fore.BLUE

    else :
        return Fore.WHITE

# Exibir os níveis do reservatório com suas respectivas cores

print("\nMONITORAMENTO DO RESERVATÓRIO DE ÁGUA")
print("--------------------------------------")

for numero, situacao in enumerate(niveis, start=1):

    cor = definir_cor(numero)

    print(cor + situacao + Style.RESET_ALL)