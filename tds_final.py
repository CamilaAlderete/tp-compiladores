#SOlUCION NRO 3 PARA EL ESPACIO
#EN ESTE CODIGO SE INGRESA EL ESPACIO COMO TERMINAL, DE MODO A QUE TODA LA LISTA SEA PROCESADA DE UNA POR EL TDS

# cadena -> letraR
# R -> letraR | ' 'letraR | Ɛ
# letra -> a| ... | z

# P(cadena) = {a, ..., z}               S(cadena)  = {$}
# P(R) = {a,...,z} u {' '} u {Ɛ}        S(R) = S(cadena) = {$}
# P(letra) = {a} u ... u {z}            S(letra) = P(R) u S(cadena)=  {a,...,z, ' ', $}

 

#SIN VENTANITA
#entrada_inicial = input('Ingrese la lista de cadenas: ')
#entrada = entrada_inicial
#i = 0
#input = entrada[i]
#salida = ''


#VENTANITA
entrada = ''
i = 0
input = ''
salida = ''
warning = ''

#VENTANITA
def inicio(lista):
    
    #prepara las variables necesarias para manejar la entrada 

    global input, salida, entrada, i, warning

    i = 0

    entrada = lista
    input = entrada[i]
    salida = ''
    warning = ''

    return S()


def S():

    global entrada, salida, warning

    print('\nEntrada: ' +entrada)

    v = 0
    c = 0
    p = 0
    max_v = 0
    
    p_sin, max_v_sin = cadena(v, c, p, max_v)

    #para la ventanita
    resultado = 'Entrada procesada: '+ salida + "\n"+\
                'Palabras: '+  str(p_sin) + "\n"+\
                'Cantidad maxima de vocales: '+ str(max_v_sin) + "\n"+\
                warning
    
    return resultado



def cadena(v, c, p, max_v):

    v_val, c_val = letra(v, c)
    p_sin, max_v_sin = R(v_val, c_val, p, max_v)

    return p_sin, max_v_sin

def R(v, c, p, max_v):  

    global input
    
    if input == 'a' or input == 'b' or input == 'c' or input == 'd' or input == 'e' or input == 'f' or input == 'g' or input == 'h' or input == 'i' or input == 'j' or input == 'k' or input == 'l' or input == 'm' or input == 'n' or input == 'ñ' or input == 'o' or input == 'p' or input == 'q' or input == 'r' or input == 's' or input == 't' or input == 'u' or input == 'v' or input == 'w' or input == 'x' or input == 'y' or input == 'z':
        
        v_val, c_val = letra(v, c)
        p_sin, max_v_sin = R(v_val, c_val, p, max_v)

        return p_sin, max_v_sin
    
    elif input == ' ': # fin de una cadena, inicia otra

        match(' ')

        # cantidad de palabras en que las vocales se encuentran en mayor o igual cantidad que las consonantes
        if v >= c and (v != 0 or c != 0): # si se proceso una cadena valida v o c no deben ser 0 al mismo tiempo. Ej cadena invalida: 23
            p = p + 1

        #mayor cantidad de vocales en una o mas palabras
        if v > max_v:
            max_v = v

        v = 0
        c = 0 

        v_val, c_val = letra(v, c)
        p_sin, max_v_sin = R(v_val, c_val, p, max_v)

        return p_sin, max_v_sin

    else: #fin de entrada


        # cantidad de palabras en que las vocales se encuentran en mayor o igual cantidad que las consonantes
        if v >= c and (v != 0 or c != 0): # si se proceso una cadena valida v o c no deben ser 0 al mismo tiempo. Ej cadena invalida: 23
            p = p + 1

            #mayor cantidad de vocales en una o mas palabras
        if v > max_v:
            max_v = v


        #para que concuerde con las reglas semanticas
        p_sin = p
        max_v_sin = max_v
        
        return p_sin, max_v_sin

def letra(v, c):

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
      
    else: 
        
        anterior = input # en match el input se va actualizar y pierdo el valor anterior
        
        match('z')

        # con gestion de errores la ejecucion continua y puede caer cualquier caracter aqui, por eso se coloca el if
        if anterior == 'z':
            c = c + 1

    return v, c




def match(t):

    global input, salida
    
    if input == t:
        #print('match con '+input)
        salida = salida + input
        avanzar_input()
    else:
        print_warning(input)
        manejo_errores()
    
    
    

def avanzar_input():

    global input, entrada, i, salida

    i = i + 1 #avanza indice

    if i < len(entrada) : #todavia hay caracteres a procesar
        
        input = entrada[i]
        
        if not pertenece_a_alfabeto(input):

            print_warning(input)
            manejo_errores()

    else:
        input = '' #fin de cadena

def manejo_errores():

    #ignora caracteres extranhos y avanza el input hasta encontrar uno que pertenezca al alfabeto
    
    global input
    global entrada
    global i
    global salida

    if i == len(entrada)-1: #ultima posicion, ya no se puede avanzar
        input = ''

    #mientras haya caracter a procesar y este no pertenezca al alfabeto
    while i < len(entrada)-1 and pertenece_a_alfabeto(entrada[i]) == False:    
        i = i + 1
        input = entrada[i]

        if(pertenece_a_alfabeto(input) == False):
            
            print_warning(input)

            if i == len(entrada):
                input = ''

                 
def pertenece_a_alfabeto(caracter):
    
    if caracter == 'a' or caracter == 'b' or caracter == 'c' or caracter == 'd' or caracter == 'e' or caracter == 'f' or caracter == 'g' or caracter == 'h' or caracter == 'i' or caracter == 'j' or caracter == 'k' or caracter == 'l' or caracter == 'm' or caracter == 'n' or caracter == 'ñ' or caracter == 'o' or caracter == 'p' or caracter == 'q' or caracter == 'r' or caracter == 's' or caracter == 't' or caracter == 'u' or caracter == 'v' or caracter == 'w' or caracter == 'x' or caracter == 'y' or caracter == 'z' or caracter == ' ':
        return True
    else:
        return False

def print_warning(caracter):

    global warning
    
    if caracter != '': #evita mostrar warning del final de cadena   
        
        print("warning: '"+ caracter + "'")  
        
        #concatenacion del resultado para ventanita
        warning = warning + "warning: '" + caracter + "'\n"

#SIN VENTANITA        
#S()