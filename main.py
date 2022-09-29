import requests

requisicao = requests.get('https://api.hgbrasil.com/finance?key=e3dda753')

cotacoesDolar = float(requisicao.json()['results']['currencies']['USD']['buy'])
cotacoesEuro = float(requisicao.json()['results']['currencies']['EUR']['buy'])

opcao = int(input('Digite a opção que deseja:\n 1-Dolar\n 2-Euro\n 3-Encerrar\n'))

while opcao != 3:
    if opcao == 1:
        valorReal = float(input('Informe um valor em real R$: '))
        valorDolarConvertido = valorReal/cotacoesDolar
        print(f'O valor em Dolar: US$ {valorDolarConvertido:.2f}\n')
        opcao = int(input('Digite a opção que deseja:\n 1-Dolar\n 2-Euro\n 3-Encerrar\n'))
    elif opcao == 2:
        valorReal = float(input('Informe um valor em real R$: '))
        valorEuroConvertido = valorReal/cotacoesEuro
        print(f'O valor em Euro: EU$ {valorEuroConvertido:.2f}\n')
        opcao = int(input('Digite a opção que deseja:\n 1-Dolar\n 2-Euro\n 3-Encerrar\n'))
    else:
        print('Opção invalida!')

print('Programa finalizado')