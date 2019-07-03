# AUXILIARES ###
def intpos(x):
    """
    Recebe: um argumento;
    Devolve: True se for um inteiro maior que zero e False em caso contrario.
    ## Funcao nao especificada no enunciado ##    
    """
    return isinstance(x,int) and x>0


def lista_especif_sol(especificacoes):
    """
    Recebe: um tuplo de tuplos com as especificacoes;
    Devolve: uma lista com as especificacoes solucao desse tabuleiro.
    ## Funcao nao especificada no enunciado ##
    """
    especif_lst = list(especificacoes)              # conversao especificacoes para lista
    for i in range(2):
        especif_lst[i] = list(especif_lst[i])
        for j in range(len(especif_lst[i])):
            especif_lst[i][j] = list(especif_lst[i][j])
    return especif_lst                              # especif_lst = [[specs linhas], [specs colunas]]


def tabuleiro_por_preencher(t):
    """
    Recebe: um elemento do tipo tabuleiro;
    Devolve: True se houverem celulas por preencher e False em caso contrario
    ## Funcao nao especificada no enunciado ##
    """
    dimensao = tabuleiro_dimensoes(t)[0]       # obter dimensoes do tabuleiro

    flag = False
    for i in range(dimensao):
        for j in range(dimensao):
            celula = tabuleiro_celula(t, cria_coordenada(i+1,j+1))
            if celula == 0:
                flag = True   # o valor de flag e alterado para True caso o tabuleiro esteja por preencher
    return flag


# TAD COORDENADA ############################################################
def cria_coordenada(l, c):
    """
    Recebe: dois inteiros, linha e coluna;
    Devolve: um elemento do tipo coordenada com a linha e coluna respetiva.
    """
    if not intpos(l) or not intpos(c):
        raise ValueError('cria_coordenada: argumentos invalidos')
    else:
        return (l,c)


def coordenada_linha(coordenada):
    """
    Recebe: uma coordenada;
    Devolve: a sua linha.
    """
    return coordenada[0]


def coordenada_coluna(coordenada):
    """
    Recebe: uma coordenada;
    Devolve: a sua coluna.
    """
    return coordenada[1]


def e_coordenada(arg):
    """
    Recebe: um argumento;
    Devolve: True se for uma coordenada e False no caso contrario.
    """
    return isinstance(arg, tuple) and len(arg)==2 and intpos(arg[0]) and intpos(arg[1])


def coordenadas_iguais(coordenada1, coordenada2):
    """
    Recebe: duas coordenadas;
    Devolve: True se forem iguais e False no caso contrario.
    """
    return coordenada1 == coordenada2


def coordenada_para_cadeia(coordenada):
    """
    Recebe: uma coordenada;
    Devolve: a sua representacao em cadeia de caracteres.
    """
    return  '(' + str(coordenada_linha(coordenada)) + ' ' + ':' + ' ' + str(coordenada_coluna(coordenada)) + ')'


# TAD TABULEIRO ###############################################################
def cria_tabuleiro(t):
    """
    Recebe: um tuplo com a especificacao do tabuleiro;
    Devolve: um elemento do tipo tabuleiro com o tabuleiro do jogo.
    """
    if not isinstance(t, tuple) or len(t) != 2 or len(t[0]) != len(t[1]):
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    for e in t:                   #percorrer valores individuais e verificar validade
        for j in e:
            for i in j:
                if not intpos(i) or i > len(t[0]):
                    raise ValueError('cria_tabuleiro: argumentos invalidos')
    
    lc = []
    for i in range(len(t[0])):    # criar linhas e colunas do tabuleiro
        lc.append(len(t[0])*[0])

    return (t[0], t[1], lc)       # tabuleiro = ((specs linhas), (specs colunas), [linhas e colunas])


def tabuleiro_dimensoes(t):
    """
    Recebe: um elemento do tipo tabuleiro;
    Devolve: um tuplo com dois elementos, o numero de linhas e o numero de colunas do tabuleiro.
    """
    return (len(t[0]),len(t[0]))


def tabuleiro_especificacoes(t):
    """
    Recebe: um elemento do tipo tabuleiro;
    Devolve: um tuplo com as especificacoes do tabuleiro: ((linhas),(colunas)).
    """
    return (t[0],t[1])


def tabuleiro_celula(t, c):
    """
    Recebe: um elemento do tipo tabuleiro e um do tipo coordenada;
    Devolve: inteiro de 0 a 2 correspondente ao valor contido no 
    tabuleiro na posicao da coordenada.
    """
    d = tabuleiro_dimensoes(t)[0]                 # obter dimensoes do tabuleiro 
    if (not e_tabuleiro(t)) or (not e_coordenada(c)) or coordenada_linha(c) > d or coordenada_coluna(c) > d:
        raise ValueError('tabuleiro_celula: argumentos invalidos')
    else:
        linha = coordenada_linha(c)-1              # determinar o indice da linha que corresponde a coordenada dessa linha no tabuleiro
        coluna = coordenada_coluna(c)-1            # determinar o indice da coluna que corresponde a coordenada dessa coluna no tabuleiro
        return t[2][linha][coluna]


def tabuleiro_preenche_celula(t, c, n):
    """
    Recebe: um elemento do tipo tabuleiro, um do tipo coordenada e um inteiro entre 0 e 2 inclusive;
    Devolve: um elemento do tipo tabuleiro modificado na coordenada especificada com o valor inteiro dado.
    """
    d = tabuleiro_dimensoes(t)[0]
    if (not e_tabuleiro(t)) or (not e_coordenada(c)) or coordenada_linha(c) > d or coordenada_coluna(c) > d \
    or (not isinstance(n,int)) or n < 0 or n > 2:
        raise ValueError('tabuleiro_preenche_celula: argumentos invalidos')
    else:
        linha = coordenada_linha(c)-1
        coluna = coordenada_coluna(c)-1
        t[2][linha][coluna] = n
        return t


def e_tabuleiro(arg):
    """
    Recebe: um argumento universal;
    Devolve: True se for do tipo tabuleiro e False caso contrario.
    """
    # tabuleiro = ((specs linhas), (specs colunas), [linhas e colunas])
    if (not isinstance(arg, tuple)) or len(arg) != 3 or (not isinstance(arg[0], tuple)) or (not isinstance(arg[1], tuple)) \
    or (not isinstance(arg[2], list)) or not (len(arg[0]) == len(arg[1]) == len(arg[2])):
        return False
    #verificar os specs de linhas e colunas
    flag = True
    for a in range(2):
        for b in arg[a]:
            if not isinstance(b, tuple):                    # e um tuplo de tuplos?
                flag = False
            for c in b:
                if not intpos(c) or c > len(arg[0]):
                    flag = False
    
    #verificar a lista de linhas e colunas
    for d in arg[2]:
        if len(d) != len(arg[2]) or not isinstance(d, list):  # e uma lista de listas? nr colunas = nr linhas?
            flag = False
        for e in d:
            if not isinstance(e, int) or e < 0 or e > 2:      # os valores das celulas estao corretos?
                flag = False
    
    return flag


def tabuleiro_completo(t):
    """
    Recebe: um elemento do tipo tabuleiro;
    Devolve: True caso o tabuleiro esteja preenchido corretamente e False em caso contrario.
    """
    # tabuleiro = ((specs linhas), (specs colunas), [linhas e colunas])
    if tabuleiro_por_preencher(t):
        return False                            # se for encontrado um 0 no tabuleiro, sair logo da funcao

    especif_sol = tabuleiro_especificacoes(t)   # lista com as especificacoes solucao [[specs linhas], [specs colunas]]
    dimensao = tabuleiro_dimensoes(t)[0]        # dimensao do tabuleiro
    
    resultado = ()
    var_ctrl = 0                         # var_ctrl controla se estamos a percorrer linhas ou colunas
    for i in range(2):                   # gerar especificacoes 2 vezes, para linhas e colunas
        res_lc = ()                      # especificacoes das linhas ou das colunas
        for l in range(dimensao):
            especif, n = (), 0            #especif: ira conter a especif. de 1 linha/coluna
            for c in range(dimensao):
                if var_ctrl == 0:
                    celula = tabuleiro_celula(t, cria_coordenada(l+1,c+1)) # loop em que percorremos linhas
                else:
                    celula = tabuleiro_celula(t, cria_coordenada(c+1,l+1)) # loop em que percorremos colunas
                if celula == 2:
                    n += 1
                elif celula != 2 and n>0:
                    especif += (n,)
                    n = 0
                if c == dimensao-1 and n>0:
                    especif += (n,)
            res_lc += (especif,)
        var_ctrl = 1                    # proximo loop, percorrer colunas
        resultado += (res_lc,)

    return resultado == especif_sol   # True se as especificacoes solucao forem iguais as geradas


def tabuleiros_iguais(t1, t2):
    """
    Recebe: dois elementos do tipo tabuleiro;
    Devolve: True caso sejam iguais e False em caso contrario.
    """
    return t1 == t2


def escreve_tabuleiro(t):
    """
    Recebe: um elemento do tipo tabuleiro;
    Devolve: a representacao externa do tabuleiro escrita no ecra.
    """
    if not e_tabuleiro(t):
        raise ValueError('escreve_tabuleiro: argumento invalido')
    else:
        # obter lista com as especificacoes,
        # possibilitando remocao de elementos ja escritos
        especif_sol = lista_especif_sol(tabuleiro_especificacoes(t))    # conversao especificacoes para lista
        especif_linh = especif_sol[0]                                   # linhas especificacoes
        especif_col = especif_sol[1]                                    # colunas especificacoes
        dimensao = tabuleiro_dimensoes(t)[0]                            # dimensao do tabuleiro
        
        especif_col_vazia = []
        for i in especif_col:             # obter lista vazia das especif. das colunas para verificacao
            especif_col_vazia.append([])  # da escrita de todos os elementos das colunas
        
        # loop das especificacoes das colunas
        while especif_col != especif_col_vazia:
            indices_len_max, n_max = [], 1
            for i in range(dimensao):           # sao guardadas as colunas com o maior nr de elem,
                len_atual = len(especif_col[i]) # pois serao escritas primeiro - (indices_len_max)
                if len_atual == n_max:
                    indices_len_max.append(i)
                elif len_atual > n_max:
                    n_max = len_atual
                    indices_len_max = []
                    indices_len_max.append(i)

            for i in range(dimensao):                                 # loop de escrita das especif. das colunas
                if i in indices_len_max and i == len(especif_col)-1:  # escrita de um nr da especif. da coluna
                    print(' ', especif_col[i][0], '   ')
                    especif_col[i] = especif_col[i][1:]               # elemento ja escrito, apagar
                elif i in indices_len_max:
                    print(' ', especif_col[i][0], ' ', end='')
                    especif_col[i] = especif_col[i][1:]
                elif i == len(especif_col)-1:                         # escrita de espacos
                    print('       ')
                else:
                    print('     ', end='')
        
        nr_max = 0
        for i in especif_linh:    # obter o numero de especificacoes maximo das linhas,
            if len(i) > nr_max:   # de modo a controlar o nr de espacos a escrever
                nr_max = len(i)

        # loop das linhas e suas especificacoes
        for i in range(dimensao):
            count = nr_max
            for j in range(dimensao):         # loop escreve tabuleiro
                celula = tabuleiro_celula(t, cria_coordenada(i+1, j+1))
                if celula == 2:
                    print('[ x ]', end= '')
                elif celula == 1:
                    print('[ . ]', end = '')
                else:
                    print('[ ? ]', end = '')
            
            for j in especif_linh[i]:          # loop escreve especificacoes das linhas
                print('',j, end = '')
                count += - 1
            for j in range(count):             # escreve os espacos em falta, tendo em conta
                print('  ', end = '')          # o nr_max e os numeros que ja foram escritos
            print('|')
        print('')


# TAD JOGADA #################################################################
def cria_jogada(c, n):
    """
    Recebe: um elemento do tipo coordenada e um inteiro com valor 1 ou 2;
    Devolve: um elemento do tipo jogada.
    """
    if n < 1 or n > 2 or not e_coordenada(c):
        raise ValueError('cria_jogada: argumentos invalidos')
    else:
        linha = coordenada_linha(c)
        coluna = coordenada_coluna(c)
        return ((linha,coluna),n)


def jogada_coordenada(j):
    """
    Recebe: um elemento do tipo jogada;
    Devolve: um elemento do tipo coordenada, da jogada recebida.
    """
    return cria_coordenada(j[0][0],j[0][1])


def jogada_valor(j):
    """
    Recebe: um elemento do tipo jogada;
    Devolve: um inteiro com valor 1 ou 2, da jogada recebida.
    """
    return j[1]


def e_jogada(j):
    """
    Recebe: um argumento universal;
    Devolve: True se for do tipo jogada e False em caso contrario.
    """
    return isinstance(j, tuple) and len(j) == 2 and isinstance(j[0], tuple) and len(j[0]) == 2 \
    and intpos(j[0][0]) and intpos(j[0][1]) and (j[1] == 1 or j[1] == 2)


def jogadas_iguais(j1, j2):
    """
    Recebe: dois elementos do tipo jogada;
    Devolve: True se forem iguais e False em caso contrario.
    """
    return j1 == j2


def jogada_para_cadeia(j):
    """
    Recebe: um elemento do tipo jogada;
    Devolve: a sua representacao em cadeia de carateres.
    """
    return coordenada_para_cadeia(jogada_coordenada(j)) + ' --> ' + str(jogada_valor(j))


# FUNCOES JOGO ###########################################################
def le_tabuleiro(f):
    """
    Recebe: uma cadeia de carateres do nome do ficheiro das especificacoes do jogo;
    Devolve: um tuplo de dois tuplos com as especificacoes do jogo.
    """
    f = open(f, 'r')
    especificacoes = eval(f.readline())
    f.close()
    return especificacoes


def pede_jogada(t):
    """
    Recebe: um elemento do tipo tabuleiro;
    Devolve: um elemento do tipo jogada, que o jogador introduziu
    """
    # obter dimensoes do tabuleiro n x n
    n = str(tabuleiro_dimensoes(t)[0])

    print('Introduza a jogada')

    # obter coordenada da jogada
    lc_str = input('- coordenada entre (1 : 1) e (' + n + ' : ' + n + ') >> ')
    lc_str = lc_str.replace(':', ',')
    lc = eval(lc_str)
    
    # obter valor da jogada
    valor = eval(input('- valor >> '))
    
    # verificar se valor e coordenada sao validos
    if lc_str == None or lc[0] > int(n) or lc[1] > int(n):
        return False

    # obter jogada e devolve-la
    jogada = cria_jogada(cria_coordenada(lc[0],lc[1]), valor)
    return jogada


def jogo_picross(f):
    """
    Recebe: uma cadeia de carateres com o nome do ficheiro com a especif. do tabuleiro;
    Devolve: True caso o tabuleiro resultante do jogo esteja completo, False caso contrario
    """
    especificacoes = le_tabuleiro(f)     # obter especificacoes do ficheiro
    tab = cria_tabuleiro(especificacoes) # criar tabuleiro de jogo
    print('JOGO PICROSS')

    escreve = True                       # flag usada para controlar a escrita quando foi encontrada uma jogada invalida
    while tabuleiro_por_preencher(tab):  # enquanto houverem celulas vazias...
        if escreve:
            escreve_tabuleiro(tab)

        jogada = pede_jogada(tab)        # obtem jogada ou obtem False se esta for invalida
        if jogada == False:
            print('Jogada invalida.')
            escreve = False
        else:
            tabuleiro_preenche_celula(tab, jogada_coordenada(jogada), jogada_valor(jogada)) # mudar celula com jogada
            escreve = True
    
    if tabuleiro_completo(tab):         # solucao encontrada
        escreve_tabuleiro(tab)
        print('JOGO: Parabens, encontrou a solucao!')
        return True
    else:                               # solucao nao encontrada
        escreve_tabuleiro(tab)
        print('JOGO: O tabuleiro nao esta correto!')
        return False
