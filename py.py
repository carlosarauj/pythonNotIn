# nome = 'carlos'

# print(nome[4])

# print('z' in nome)
# print('a' in nome)

# print('z' not in nome)
# print('a' not in nome)

nome = input('Digite seu nome: ')
encontrar = input("Qual letra você quer?: ")

if encontrar in nome:
    print(f'Achamos sua letra {encontrar} em {nome}')
else:
    print(f'letra {encontrar} não encontrada em {nome}')

#python py.py
#ctrl ; para comentar