lista = []

def insere_carro(carro):
    lista.append(carro)
    print(lista)

def remove_carro(carro):

    try:
        lista.remove(f'{carro}')
        print(lista)
    except Exception as error:
        print(f'o veiculo {carro} nao foi encontrado')
        veiculo = input('digite o nome do veiculo: ')
        remove_carro(veiculo)


insere_carro('supra')
insere_carro('golf')

remove_carro('supra')
remove_carro('golf')

for veiculo in lista:
    print(veiculo)










