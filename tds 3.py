#SOlUCION NRO 2 PARA EL ESPACIO
#EN ESTE CODIGO SE INGRESA EL ESPACIO COMO TERMINAL, DE MODO A QUE TODA LA LISTA SEA PROCESADA DE UNA POR EL TDS

entrada_inicial = input('Ingrese la lista de cadenas: ')
entrada = ' '.join(entrada_inicial.split())
i = 0
input = entrada[i]
salida = ''



def S():

    global entrada, salida

    print('Entrada: ' +entrada)

    v = 0
    c = 0
    p = 0
    max_v = 0
    
    v, c, p, max_v = cadena(v, c, p, max_v)

    print('Entrada procesada: '+salida)
    print('Palabras: '+  str(p))
    print('Cantidad maxima de vocales: '+ str(max_v))


def cadena(v, c, p, max_v):

    v, c, p, max_v = letra(v, c, p, max_v)
    v, c, p, max_v = R(v, c, p, max_v)

    return v, c, p, max_v

def R(v, c, p, max_v):  

    global input
    
    if input == 'a' or input == 'b' or input == 'c' or input == 'd' or input == 'e' or input == 'f' or input == 'g' or input == 'h' or input == 'i' or input == 'j' or input == 'k' or input == 'l' or input == 'm' or input == 'n' or input == 'ñ' or input == 'o' or input == 'p' or input == 'q' or input == 'r' or input == 's' or input == 't' or input == 'u' or input == 'v' or input == 'w' or input == 'x' or input == 'y' or input == 'z' or input == ' ':
        
        v, c, p, max_v = letra(v, c, p, max_v)
        v, c, p, max_v = R(v, c, p, max_v)

        return v, c, p, max_v

    else: #fin de entrada

        #SE REPITEEE

        # cantidad de palabras en que las vocales se encuentran en mayor o igual cantidad que las consonantes
        if v >= c and (v != 0 or c != 0): # si se proceso una cadena valida v o c no deben ser 0 al mismo tiempo. Ej cadena invalida: 23
            p = p + 1

            #mayor cantidad de vocales en una o mas palabras
        if v > max_v:
            max_v = v

        v = 0
        c = 0 
        
        return v, c, p, max_v

def letra(v, c, p, max_v):

    global input
    
    if input == 'a':
        match('a')
        v = v + 1
    elif input == 'b':
        match('b')
        c = c + 1
    elif input == 'c':
        match('c')
        c = c + 1
    elif input == 'd':
        match('d')
        c = c + 1
    elif input == 'e':
        match('e')
        v = v +1
    elif input == 'f':
        match('f')
        c = c + 1
    elif input == 'g':
        match('g')
        c = c + 1
    elif input == 'h':
        match('h')
        c = c + 1
    elif input == 'i':
        match('i')
        v = v + 1        
    elif input == 'j':
        match('j')
        c = c + 1
    elif input == 'k':
        match('k')
        c = c + 1
    elif input == 'l': 
        match('l')
        c = c + 1
    elif input == 'm':
        match('m')
        c = c + 1
    elif input == 'n':
        match('n')
        c = c + 1
    elif input == 'ñ':
        match('ñ')
        c = c + 1
    elif input == 'o':
        match('o')
        v = v + 1
    elif input == 'p':
        match('p')
        c = c + 1
    elif input == 'q':
        match('q')
        c = c + 1
    elif input == 'r':
        match('r')
        c = c + 1
    elif input == 's':
        match('s')
        c = c + 1
    elif input == 't':
        match('t')
        c = c + 1
    elif input == 'u': 
        match('u')
        v = v + 1
    elif input == 'v': 
        match('v')
        c = c + 1
    elif input == 'w':
        match('w')
        c = c + 1
    elif input == 'x': 
        match('x')
        c = c + 1
    elif input == 'y': 
        match('y')
        c = c + 1
    elif input == 'z': 
        match('z')
        c = c + 1        
    else: # fin una cadena

        anterior = input # en match el input se va actualizar y pierdo el valor anterior

        match(' ')

        if anterior == ' ': #fin de una cadena. El if porque cualquier caracter puede entrar aqui

            # cantidad de palabras en que las vocales se encuentran en mayor o igual cantidad que las consonantes
            if v >= c and (v != 0 or c != 0): # si se proceso una cadena valida v o c no deben ser 0 al mismo tiempo. Ej cadena invalida: 23
                p = p + 1

            #mayor cantidad de vocales en una o mas palabras
            if v > max_v:
                max_v = v

            v = 0
            c = 0 

    return v, c, p, max_v




def match(t):

    global input, salida
    
    if input == t:
        #print('match con '+input)
        salida = salida + input
        avanzar_input()
    else:
        print('warning, el caracter '+input+ ' no pertenece al alfabeto') 
        manejo_errores()
    
    
    

def avanzar_input():

    global input, entrada, i, salida

    i = i + 1 #avanza indice

    if i < len(entrada) : #todavia hay caracteres a procesar
    
        if pertenece_a_alfabeto(entrada[i]):
            input = entrada[i]
        else:
            manejo_errores()

    else:
        input = '' #fin de cadena

def manejo_errores():

    #ignora caracteres extranhos y avanza para procesar siguiente caracter
    
    global input
    global entrada
    global i
    global salida

    while i < len(entrada)-1 and pertenece_a_alfabeto(entrada[i]) == False:
        i = i + 1
        input = entrada[i]

        if(pertenece_a_alfabeto(input) == False):
            
            print('warning, el caracter '+input+ ' no pertenece al alfabeto')

            if i == len(entrada):
                input = ''

                 
def pertenece_a_alfabeto(caracter):
    
    if caracter == 'a' or caracter == 'b' or caracter == 'c' or caracter == 'd' or caracter == 'e' or caracter == 'f' or caracter == 'g' or caracter == 'h' or caracter == 'i' or caracter == 'j' or caracter == 'k' or caracter == 'l' or caracter == 'm' or caracter == 'n' or caracter == 'ñ' or caracter == 'o' or caracter == 'p' or caracter == 'q' or caracter == 'r' or caracter == 's' or caracter == 't' or caracter == 'u' or caracter == 'v' or caracter == 'w' or caracter == 'x' or caracter == 'y' or caracter == 'z' or caracter == ' ':
        return True
    else:
        return False
    

S()