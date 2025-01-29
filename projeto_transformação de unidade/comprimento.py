class Comprimento:
    def __init__(self):
        self.unidades = {
            'mm': 0.001, 'cm': 0.01, 'dm': 0.1, 'm': 1, 'dam': 10, 'hm': 100, 'km': 1000
        }
        self.opcoes_unidades = {
            'mm': ['cm', 'dm', 'm', 'dam', 'hm', 'km'],
            'cm': ['mm', 'dm', 'm', 'dam', 'hm', 'km'],
            'dm': ['mm', 'cm', 'm', 'dam', 'hm', 'km'],
            'm': ['mm', 'cm', 'dm', 'dam', 'hm', 'km'],
            'dam': ['mm', 'cm', 'dm', 'm', 'hm', 'km'],
            'hm': ['mm', 'cm', 'dm', 'm', 'dam', 'km'],
            'km': ['mm', 'cm', 'dm', 'm', 'dam', 'hm']
        }
        self.unidades_iniciais = {
            '1': 'mm', '2': 'cm', '3': 'dm', '4': 'm', '5': 'dam', '6': 'hm', '7': 'km'
        }

    def converter(self, valor, unidade_inicial, unidade_final):
        valor_em_metros = valor * self.unidades[unidade_inicial]
        valor_final = valor_em_metros / self.unidades[unidade_final]
        return valor_final

    def exibir_opcoes_unidade_final(self, unidade_inicial):
        print("Escolha a unidade final:")
        for i, unidade in enumerate(self.opcoes_unidades[unidade_inicial], 1):
            print(f"{i}. {unidade}")

        escolha = input('Digite a sua escolha: ')
        return self.opcoes_unidades[unidade_inicial][int(escolha) - 1]

    def iniciar(self):
        while True:
            entrada = input('Escolha a unidade a ser transformada:\n1.Miliímetro(mm)\n2.Centímetro(cm)\n3.Decímetro(dm)\n4.Metro(m)\n5.Decâmetro(dam)\n6.Hectômetro(hm)\n7.Quilômetro(km)\n8.Sair\nDigite a sua escolha: ')

            if entrada == '8':
                print('Saindo.')
                break

            elif entrada in ['1', '2', '3', '4', '5', '6', '7']:
                unidade_inicial = self.unidades_iniciais[entrada]
                valor = float(input(f'Digite o valor em {unidade_inicial} que deseja converter: '))
                unidade_final = self.exibir_opcoes_unidade_final(unidade_inicial)

                valor_convertido = self.converter(valor, unidade_inicial, unidade_final)
                print(f'{valor} {unidade_inicial} é igual a {valor_convertido} {unidade_final}\n')
            else:
                print('Opção inválida. Tente novamente.')


