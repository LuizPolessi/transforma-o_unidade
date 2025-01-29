class Volume:
    def __init__(self):
        self.unidades = {'kL': 1000000, 'hL': 100000, 'daL': 10000, 'L': 1000, 'dL': 100, 'cL': 10, 'mL': 1}
        self.opcoes = {
            'kL': ['hL', 'daL', 'L', 'dL', 'cL', 'mL'],
            'hL': ['kL', 'daL', 'L', 'dL', 'cL', 'mL'],
            'daL': ['kL', 'hL', 'L', 'dL', 'cL', 'mL'],
            'L': ['kL', 'hL', 'daL', 'dL', 'cL', 'mL'],
            'dL': ['kL', 'hL', 'daL', 'L', 'cL', 'mL'],
            'cL': ['kL', 'hL', 'daL', 'L', 'dL', 'mL'],
            'mL': ['kL', 'hL', 'daL', 'L', 'dL', 'cL']
        }
    
    def converter(self, valor, unidade_inicial, unidade_final):
        resultado = valor * self.unidades[unidade_inicial]
        return resultado / self.unidades[unidade_final]

    def exibir_opcoes_unidade_final(self, unidade_inicial):
        print("\nEscolha a unidade final:")
        for i, unidade in enumerate(self.opcoes[unidade_inicial], 1):
            print(f"{i}. {unidade}")
        escolha = input('Digite a sua escolha: ')
        return self.opcoes[unidade_inicial][int(escolha) - 1]

    def executar(self):
        while True:
            entrada = input('Escolha a unidade a ser transformada:\n1.Quilolitro(kL)\n2.Hectolitro(hL)\n3.Decalitro(daL)\n4.Litro(L)\n5.Decilitro(dL)\n6.Centilitro(cL)\n7.Mililitro(mL)\n8.Sair\nDigite a sua escolha: ')
            
            if entrada == '8':
                print('Saindo.')
                break
            
            unidades_iniciais = {'1': 'kL', '2': 'hL', '3': 'daL', '4': 'L', '5': 'dL', '6': 'cL', '7': 'mL'}
            
            if entrada in unidades_iniciais:
                unidade_inicial = unidades_iniciais[entrada]
                valor = float(input(f'\nDigite o valor que deseja converter: '))
                unidade_final = self.exibir_opcoes_unidade_final(unidade_inicial)
                valor_convertido = self.converter(valor, unidade_inicial, unidade_final)
                print(f'\n{valor} {unidade_inicial} é igual a {valor_convertido} {unidade_final}')
            else:
                print('Opção inválida. Tente novamente.')

