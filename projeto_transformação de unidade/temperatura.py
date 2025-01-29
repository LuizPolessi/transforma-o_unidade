class Temperatura:
    def __init__(self):
        self.opcoes = {
            '1': 'Grau Celsius',
            '2': 'Grau Fahrenheit',
            '3': 'Kelvin',
            '4': 'Sair'
        }

    def celsius_para_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def celsius_para_kelvin(self, celsius):
        return celsius + 273.15

    def fahrenheit_para_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    def fahrenheit_para_kelvin(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9 + 273.15

    def kelvin_para_celsius(self, kelvin):
        return kelvin - 273.15

    def kelvin_para_fahrenheit(self, kelvin):
        return (kelvin - 273.15) * 9 / 5 + 32

    def exibir_menu(self):
        for key, value in self.opcoes.items():
            print(f"{key}. {value}")

    def realizar_conversao(self, origem, destino, temperatura):
        if origem == '1': 
            if destino == '2':
                return f"\n{temperatura}°C é igual a {self.celsius_para_fahrenheit(temperatura):.2f}°F\n"
            elif destino == '3':
                return f"\n{temperatura}°C é igual a {self.celsius_para_kelvin(temperatura):.2f}K\n"

        elif origem == '2': 
            if destino == '1':
                return f"\n{temperatura}°F é igual a {self.fahrenheit_para_celsius(temperatura):.2f}°C\n"
            elif destino == '3':
                return f"\n{temperatura}°F é igual a {self.fahrenheit_para_kelvin(temperatura):.2f}K\n"

        elif origem == '3':  
            if destino == '1':
                return f"\n{temperatura}K é igual a {self.kelvin_para_celsius(temperatura):.2f}°C\n"
            elif destino == '2':
                return f"\n{temperatura}K é igual a {self.kelvin_para_fahrenheit(temperatura):.2f}°F\n"

        return "\nConversão inválida!"

    def executar(self):
        while True:
            self.exibir_menu()
            origem = input("Escolha a unidade a ser transformada: ")

            if origem == '4':
                print("Saindo")
                break

            if origem not in ['1', '2', '3']:
                print("Opção inválida! Tente novamente.")
                continue

            destino = input("Escolha a unidade final: ")
            if destino == '4':
                print("Saindo")
                break

            if destino not in ['1', '2', '3']:
                print("Opção inválida! Tente novamente.")
                continue

            try:
                temperatura = float(input("Digite a temperatura a ser convertida: "))
                resultado = self.realizar_conversao(origem, destino, temperatura)
                print(resultado)
            except ValueError:
                print("Por favor, insira um valor numérico válido.\n")


