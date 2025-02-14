""" Mudança no tipo de Variável """

faturamento = float(input('Insira o faturamento'))
custo = float(input('Insira o custo'))

print(type(faturamento))
print(type(custo))

lucro = faturamento - custo
print(f'O lucro da sua empresa foi de R${lucro}.')