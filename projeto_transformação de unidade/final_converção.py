from comprimento import Comprimento
from temperatura import Temperatura
from volume import Volume

def menu_principal():
    while True:
        print("\n\033[1mConversor de Unidades\033[0m\n")
        print("1. Conversor de Comprimento")
        print("2. Conversor de Temperatura")
        print("3. Conversor de Volume")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")
        print('\n')
        if escolha == '1':
            conversor = Comprimento()
            conversor.iniciar()
        elif escolha == '2':
            conversor = Temperatura()
            conversor.executar()
        elif escolha == '3':
            conversor = Volume()
            conversor.executar()
        elif escolha == '4':
            print("Saindo.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_principal()

