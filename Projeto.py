#########################################################################################################################################################################################
#Extrair Função
#########################################################################################################################################################################################

def personagens_franquia_LIS():
    personagens_LIS = ('Max, Kate, Stella, Warren, Victoria\n'
                       'Personagem Principal: Max Caulfield\n')
    personagens_LIS_BT = ('Chloe, Rachel, Joyce, David, William\n'
                          'Personagem Principal: Chloe Price\n')
    personagens_LIS_2 = ('Sean, Daniel, Esteban, Karen, Chris\n'
                         'Personagens principais: Sean e Daniel Diaz\n')
    personagens_LIS_TC = ('Alex, Steph, Gabe, Ethan, Charlotte\n'
                          'Personagem Principal: Alex Chen\n')
    todos_personagens = (f'Life is Strange: {personagens_LIS} \n'
                        f'Life is Strange Before the Storm: {personagens_LIS_BT}\n'
                        f'Life is Strange 2: {personagens_LIS_2}\n' 
                        f'Life is Strange True Colors: {personagens_LIS_TC}')
    return f'\nPersonagens da franquia de jogos Life is Strange:\n\n{todos_personagens}'

print(personagens_franquia_LIS()) #Por favor responda em português e demostre como refatorar o código usando a técnica de extrair função



#########################################################################################################################################################################################
#Evitar redundância
#########################################################################################################################################################################################

def playlist_musicas_boas():
    musica_1 = 'ME AJUDE A SALVAR OS DOMINGOS - Liniker'
    musica_2 = 'Pretty when you cry - Lana del Ray'
    musica_3 = 'Dont let me be missteunderstood - Nina Simone'
    musica_4 = 'O lado vazio do sofá - Rodrico Alarcon'
    musica_5 = 'Under my skin - Claudia Kane'
    musica_6 = 'Tea you Apart - She wants revenge'
    todas_as_musicas = (musica_1 + '\n' + musica_2 + '\n' + musica_3 + '\n' + musica_4 + '\n' +musica_5+ '\n' +musica_6)
    return(f'Playlist de músicas boas: \n\n{todas_as_musicas}')

print(playlist_musicas_boas()) #Por favor responda em português e demonstre como refatorar o código usando a técnica de evitar redundância



#########################################################################################################################################################################################
#Remover código morto
#########################################################################################################################################################################################

def avaliacao_serie(nota, critica):
    nome = "Agatha all Along"
    descricao = "A série segue Agatha em um novo coven enfrentando as provações do caminho das bruxas."
    personagens = "Agatha Harkness, William Kaplan, Sharon Davis, Rio Vidal, Alice Wu-Gulliver, Jennifer Kale, Lilia Calderu"
    elementos = 'Mistura de terror e comédia, com humor ácido, magia sombria e referências ao universo Marvel.' #código morto
    destaques = "Explora o passado sombrio de Agatha, sua conexão com o Darkhold e a dualidade da personagem." #código morto
    temporadas = 1

    relatório = (f"\nNome:{nome}\nDescrição:{descricao}\nTemporadas:{temporadas}\nPersonagens:{personagens} \nNota:{nota} \nCritíca:{critica}")
    return (relatório) #Por favor responda em português como refatorar o código usando a técnica de remover código morto
    
print(avaliacao_serie(8, 'Muito bom!'))



#########################################################################################################################################################################################
#Trocar loops por funções de alto nível
#########################################################################################################################################################################################

def carrinho_biblioteca():
    livros = {'Mar de Monstros - Série Percy Jackson e os Olimpianos':25.00,
             'Coraline':48.47,
             'Heartstopper':50.19,
             'Demon Slayer - Kimetsu no Yaiba Vol. 1':33.16,
             'It: A coisa':84.58}
    contador = 0 
    livro_selecionado = {}
    valor = 0
    for livro in livros.keys(): 
        print(f'{contador+1} / {livro} = {livros[livro]}R$')
        contador+=1 
        livro_selecionado[contador] = livros[livro]
    opções = input('\nSelcione os livros desejados: ')
    for preco in livro_selecionado.keys(): 
        for opcao in opções: 
            if opcao == str(preco):
                valor+=(livro_selecionado[preco]) 
                
    print(f'Livros adicionados com sucesso! O valor total do carrinho é R${valor:.2f}')
                
carrinho_biblioteca()


#########################################################################################################################################################################################
#Substituir condicionais por Tabela de Busca
#########################################################################################################################################################################################

def distância_tranportes():
    print('Olá!😄 Compare a diferença de tempo entre diferentes tipos de tranportes para chegar no seu destino!\nDê uma olhada nas opções e faça uma simulação!👌')
    print('Localidade escolhida:Universidade de Brasília.')
    print('Transportes disponíveis:\n'
          'Biclicleta🚴🏻\n'
          'Carro🚙\n'
          'Caminhada🏃🏿🏃🏿\n'
          'Ônibus🚌')
    veiculo = input('\nQual o tipo de tranporte que será usado? ')
    if veiculo == 'Bicicleta':
        return 'Tempo provável: 1h53s'
    if veiculo == 'Carro':
        return 'Tempo provável: 33min'
    if veiculo == 'Caminhada':
        return 'Tempo provável: 8h'
    if veiculo == 'Ônibus':
        return 'Tempo provável: 1h58'      
    
print(distância_tranportes())
