quantidade_de_pessoas = int(input('Por quantas pessoas será feita a divisão? '))

participantes_gastos = {}


for pessoa in range(quantidade_de_pessoas):
    print(f'\n--- Cadastro da {pessoa + 1}ª pessoa ---')
    nome = input('Qual o nome: ')
    valor = float(input('Quanto esta pessoa gastou? '))

    participantes_gastos[nome] = valor

gastos_totais = 0

for valor in participantes_gastos.values():
    gastos_totais += valor

divisao = gastos_totais / quantidade_de_pessoas

print(f'\n Valor Total: {gastos_totais:.2f}\n')

for nome, valor in participantes_gastos.items():
    print(f'O saldo de {nome} é igual a R$ {valor - divisao:.2f}\n')

