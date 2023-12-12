nomes = ("Julia", "Jefferson", "Anna", "Eduardo")
resultado = ''

while True:
    pesquisa = str(input('Qual o nome que deseja buscar?: ')).capitalize()
    for c,p in enumerate(nomes):
        if pesquisa in nomes:
            if pesquisa ==[p][0]:
                resultado = f'{p} encontrado na posição {c+1}!'
                print(resultado)
    if resultado == '':
        print('Não encontrei o nome informado.')
    continuar = str(input("Deseja pesquisar outro nome? [S/N]"))[0].upper()
    if continuar == 'N':
        break
    else:
        continue





