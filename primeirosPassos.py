""" Comando Print """
# O print() em Python é uma função usada para exibir informações no console.

print('Hello, World!')


""" Operações Básicas """

a = 5
b = 3

print(a + b)
print(a - b)
print(a / b) # Divisão com exibição float
print(a // b) # Divisão sem exibição de float
print(a * b)
print(2 ** 3)
print(3 % 2)

# Ordem das operações
print(1 + 2 * 5) # Sem ordem
print((1 + 2) * 5) # Com ordem


""" Concatenação """

print('Meu nome é Luan, ' + 'sou estudante de ciência e análise de dados')


""" IN (em) """

print('não está estudando' in 'Luan está estudando análise e ciência de dados')
print('não está estudando' in 'Luan não está estudando análise e ciência de dados')


""" Variáveis """

nome = 'Luan'
qtdeVendas = 1800

print(nome, qtdeVendas)


""" Input """

nome = input('Qual teu nome?')
sobrenome = input('Qual seu sobrenome?')

nomeCompleto = f'Seu nome completo: {nome} {sobrenome}.'