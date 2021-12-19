def loadInfodados(arquivo):
  arqdados = open(arquivo, 'r')
  dados_dos_carros = arqdados.readlines()
  arqdados.close()

  return dados_dos_carros


def constroiDados(dados_dos_carros):
  dados = {}
  
  for dado in dados_dos_carros:
    infodados = dado.strip().split(";")  #cria uma lista de string dividindo as no caracter ;
    chave_placa_do_carro = infodados [4]  #pega o quarto elemento (placa do carro) da lista de strings criada no comando anterior
    tipo_carro = infodados[0]

    marca = infodados[1]

    ano_fabricacao = infodados[2]

    cor = infodados[3]

    dados[chave_placa_do_carro] = [tipo_carro, marca, ano_fabricacao, cor]
    return dados


def buscardados(dados_dos_carros):
  placadoCarro = input('Pra obter informações sobre o carro informe sua placa: ')

  if (placadoCarro in dados_dos_carros.keys()):
    print('Placa do carro: ', placadoCarro)
    print('Tipo do carro: ', dados_dos_carros[placadoCarro][0])
    print('Marca: ', dados_dos_carros[placadoCarro][1])
    print('Ano de fabricação: ', dados_dos_carros[placadoCarro][2])
    print('Cor: ', dados_dos_carros[placadoCarro][3])

  else:
    print(f'A placa "{placadoCarro}" não foi encontrada nos dados da coleção de carros!')
    print('\n')

  return None

def listardados(dados_dos_carros):
  for placadoCarro in dados_dos_carros.keys():
    print('Placa do carro: ', placadoCarro)
    print('Tipo do carro: ', dados_dos_carros[placadoCarro][0])
    print('Marca: ', dados_dos_carros[placadoCarro][1])
    print('Ano de fabricação: ', dados_dos_carros[placadoCarro][2])
    print('Cor: ', dados_dos_carros[placadoCarro][3])
    print('\n')

  return None


def cadastrardados(dados_dos_carros):
  newplaca = input('Para cadastrar um modelo insira a placa do carro:')
  newtipo = input('Insira o tipo do carro:')
  newmarca = input('Insira a marca do carro:')
  newanodefabricacao = input('Insira o ano de fabricação do carro:')
  newcor = input('Insira a cor do carro:')

  print ('Em seguida, para armazenar as informações do carro adicionado aperte a tecla "5" no menu' )
  print('\n')



  if (newplaca in dados_dos_carros.keys()):
    print(f'A placa {newplaca} já está cadastrada nos dados da coleção de carros!')
    print('\n')
    print(f'Placa:{newplaca}')
    print(f'Tipo do carro: {dados_dos_carros[newplaca][0]}')
    print(f'Marca: {dados_dos_carros[newplaca][1]}')
    print(f'Ano de fabricação: {dados_dos_carros[newplaca][2]}')
    print(f'Cor: {dados_dos_carros[newplaca][3]}')
    print('\n')  

  else:
    dados_dos_carros[newplaca] = [newtipo, newmarca, newanodefabricacao, newcor]

  return None


def deletarplaca(dados_dos_carros):
  deletarplaca = input('Para deletar um carro informe sua placa:')
  if (deletarplaca in dados_dos_carros.keys()):
    print(f'Placa:{deletarplaca}')
    print(f'Tipo do carro: {dados_dos_carros[deletarplaca][0]}')
    print(f'Marca: {dados_dos_carros[deletarplaca][1]}')
    print(f'Ano de fabricação: {dados_dos_carros[deletarplaca][2]}')
    print(f'Cor: {dados_dos_carros[deletarplaca][3]}')
    print('\n')
    dados_dos_carros.pop(deletarplaca)
  else:
    print(f'A placa: {deletarplaca} não foi encontrada nos dados da coleção de carros!')
    print('\n')

  return None


def menu():
  print('1 - Buscar dados do carro')
  print('2 - Listar todos os dados da coleção de carros')
  print('3 - Cadastrar dados do carro')
  print('4 - Remover dados do carro')
  print('5 - Gravar dados do carro')
  print('0 - Sair dos dados da coleção de carros')
  print('\n')
  escolha = int(input(''))

  return escolha

def gravardados(dados_dos_carros, arquivo):
    arqdados = open(arquivo, 'w')
    registros = []

    for placadoCarro in dados_dos_carros.keys():
      registroDadoNoArquivo = placadoCarro + ";" + dados_dos_carros[placadoCarro][0] + ";" +dados_dos_carros[placadoCarro][1] + ";" + dados_dos_carros[placadoCarro][2] + ";" + dados_dos_carros[placadoCarro][3] + "\n"
      registros.append(registroDadoNoArquivo)

    arqdados.writelines(registros)
    arqdados.close()

    return None


def rodarDados(dados_dos_carros):
    opcao = 1
    while (opcao != 0):
      opcao = menu()
      if (opcao == 1):
        buscardados(dados_dos_carros)
      elif (opcao == 2):
        listardados(dados_dos_carros)
      elif (opcao == 3):
        cadastrardados(dados_dos_carros)
      elif (opcao == 4):
        deletarplaca(dados_dos_carros)
      elif (opcao == 5):
        gravardados(dados_dos_carros, 'dados da coleção de carros2.csv')

      input('Aperte uma tecla para continuar...')

    return None


conteudoDosDados = loadInfodados('dados da coleção de carros.csv')
Dadosdoscarros = constroiDados(conteudoDosDados)

rodarDados(Dadosdoscarros)

