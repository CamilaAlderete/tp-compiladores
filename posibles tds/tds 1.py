# Este TDS recibe una lista de cadenas, donde las cadenas son cualquier combinacion de letras minusculas

# El match trata el espacio lo que permite continuar la ejecucion al procesar listas

# Problema: No se puede realizar los calculos requeridos por el enunciado porque el espacio es ignorado durante el match 
# y el TDS toma la lista como una sola cadena junta.
# Ejemplo: 'abc de' -> 'abcde' 
# Posible solucion: hacer globales las variables involucradas y modificarlas en el match al encontrar un espacio, pero esto no
# corresponde al match.

# cadena -> letraR
# R -> letraR | Ɛ
# letra -> a| ... | z 

entrada_inicial = input('Ingrese la lista de cadenas: ')
entrada = ' '.join(entrada_inicial.split())
i = 0
input = entrada[i]
salida = ' '


def S():

    global entrada, salida
    print(entrada)
    
    cadena()

    print(salida)

def cadena():

    letra()
    R()

def R():  

    global input
    if input == 'a' or input == 'b' or input == 'c' or input == 'd' or input == 'e' or input == 'f' or input == 'g' or input == 'h' or input == 'i' or input == 'j' or input == 'k' or input == 'l' or input == 'm' or input == 'n' or input == 'ñ' or input == 'o' or input == 'p' or input == 'q' or input == 'r' or input == 's' or input == 't' or input == 'u' or input == 'v' or input == 'w' or input == 'x' or input == 'y' or input == 'z':
        letra()
        R()
    else:
        return 0;

def letra():

    global input
    
    if input == 'a':
        match('a')
    elif input == 'b':
        match('b')
    elif input == 'c':
        match('c')
    elif input == 'd':
        match('d')
    elif input == 'e':
        match('e')
    elif input == 'f':
        match('f')
    elif input == 'g':
        match('g')
    elif input == 'h':
        match('h')
    elif input == 'i':
        match('i')
    elif input == 'j':
        match('j')
    elif input == 'k':
        match('k')
    elif input == 'l': 
        match('l')
    elif input == 'm':
        match('m')
    elif input == 'n':
        match('n')
    elif input == 'ñ':
        match('ñ')
    elif input == 'o':
        match('o')
    elif input == 'p':
        match('p')
    elif input == 'q':
        match('q')
    elif input == 'r':
        match('r')
    elif input == 's':
        match('s')
    elif input == 't':
        match('t')
    elif input == 'u': 
        match('u')
    elif input == 'v': 
        match('v')
    elif input == 'w':
        match('w')
    elif input == 'x': 
        match('x')
    elif input == 'y': 
        match('y')
    else:
        match('z')

def match(t):

    global input
    global entrada
    global i

    print(input)
    
    if t == input:

        i = i + 1

        if i < len(entrada): #todavia hay caracteres a procesar
            
            if entrada[i] != ' ': #caracter distinto a espacio, puede procesarse por el tds
                input = entrada[i]
            else: #espacio, ignorar y avanzar para procesar siguiente caracter
                i = i + 1
                input = entrada[i]

        else:
            input = '' #fin de cadena
    
    else:
        print('Error')
        exit()    



# def match__(t): #no reconoce ultimo carcter

#     global input
#     global entrada
#     global i
#     global salida
    

#     if i < len(entrada)-1 : #todavia hay caracteres a procesar
    
#         #otra opcion para atender caracteres extranhos

#         if pertenece_a_alfabeto(entrada[i]):
#             i = i + 1
#             input = entrada[i]
#             print(input)
#         else: #ignorar y avanzar para procesar siguiente caracter
#             while i < len(entrada)-1 and pertenece_a_alfabeto(entrada[i]) == False:
#                 i = i + 1
#                 input = entrada[i]

#                 if(pertenece_a_alfabeto(input) == False):
#                     print("warning")

#             if i == len(entrada):
#                 input = ''

#     else:
#         input = '' #fin de cadena


# def match(t): #modificar este

#     global input
#     global entrada
#     global i
#     global salida

#     if input == t:
#         print('match con '+input)
#         avanzar_input()
#     else:
#         print('warning, el caracter '+input+ ' no pertenece al alfabeto') 
#         manejo_errores()
    
    
    

# def avanzar_input():

#     global input
#     global entrada
#     global i
#     global salida

#     i = i + 1 #avanza indice

#     if i < len(entrada) : #todavia hay caracteres a procesar
    
#         if pertenece_a_alfabeto(entrada[i]):
#             input = entrada[i]
#         else:
#             manejo_errores()

#     else:
#         input = '' #fin de cadena

# def manejo_errores():

#     #ignora caracteres extranhos y avanza para procesar siguiente caracter
    
#     global input
#     global entrada
#     global i
#     global salida

#     while i < len(entrada)-1 and pertenece_a_alfabeto(entrada[i]) == False:
#         i = i + 1
#         input = entrada[i]

#         if(pertenece_a_alfabeto(input) == False):
            
#             print('warning, el caracter '+input+ ' no pertenece al alfabeto')

#             if i == len(entrada):
#                 input = ''

                 
# def pertenece_a_alfabeto(caracter):
    
#     if caracter == 'a' or caracter == 'b' or caracter == 'c' or caracter == 'd' or caracter == 'e' or caracter == 'f' or caracter == 'g' or caracter == 'h' or caracter == 'i' or caracter == 'j' or caracter == 'k' or caracter == 'l' or caracter == 'm' or caracter == 'n' or caracter == 'ñ' or caracter == 'o' or caracter == 'p' or caracter == 'q' or caracter == 'r' or caracter == 's' or caracter == 't' or caracter == 'u' or caracter == 'v' or caracter == 'w' or caracter == 'x' or caracter == 'y' or caracter == 'z':
#         return True
#     else:
#         return False
    

S()