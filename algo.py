import random
def creaMatriz(n):
    """ Crea una matriz de n x n llena de x """

    m = []
    for row in range(n):
        cel = []
        m.append(cel)
        for col in range(n):
            cel.append(' ')
    return m

def imprimeMatriz(matriz):
    """ Imprime la matriz dada de manera ORDENADA """

    for fil in range(len(matriz)):
            print (matriz[fil])

def manhattan(p1, p2):
    """ Regresa la distancia Manhattan entre dos puntos """

    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    distance = abs(x1-x2) + abs(y1-y2)
    return distance


def checkGuard(p):
    """ Revisa si es guard """
    if p == 'G':
        result = 1
    else:
        result = 0
    return result

def validatePoint(j,i):
    """ Revisa si el punto es esquina, o extremo """
    global cells
    n, ne, e, se, s, sw, w, nw = 0, 0, 0, 0, 0, 0, 0, 0

    #Esquina superior izquierda
    if j == 0 and i == 0:
        e = checkGuard(matrix[j][i+1])
        se = checkGuard(matrix[j+1][i+1])
        s = checkGuard(matrix[j+1][i])
    #Borde superior
    elif j == 0 and i != 0 and i != cells-1:
        e = checkGuard(matrix[j][i+1])
        se = checkGuard(matrix[j+1][i+1])
        s = checkGuard(matrix[j+1][i])
        sw = checkGuard(matrix[j+1][i-1])
        w = checkGuard(matrix[j][i-1])
    #Esquina superior derecha
    elif j ==  0 and i == cells-1:
        s = checkGuard(matrix[j+1][i])
        sw = checkGuard(matrix[j+1][i-1])
        w = checkGuard(matrix[j][i-1])
    #Borde derecho
    elif j!= 0 and j!= cells-1 and i ==cells-1:
        n = checkGuard(matrix[j-1][i])
        s = checkGuard(matrix[j+1][i])
        sw = checkGuard(matrix[j+1][i-1])
        w = checkGuard(matrix[j][i-1])
        nw = checkGuard(matrix[j-1][i-1])
    #Esquina inferior derecha
    elif j == cells-1 and i == cells-1:
        n = checkGuard(matrix[j-1][i])
        w = checkGuard(matrix[j][i-1])
        nw = checkGuard(matrix[j-1][i-1])
    #Borde inferior
    elif j == cells-1 and i != 0 and i!= cells-1:
        n = checkGuard(matrix[j-1][i])
        ne = checkGuard(matrix[j-1][i+1])
        e = checkGuard(matrix[j][i+1])
        w = checkGuard(matrix[j][i-1])
        nw = checkGuard(matrix[j-1][i-1])
    #Esquina inferior izquierda
    elif j == cells-1 and i == 0:
        n = checkGuard(matrix[j-1][i])
        ne = checkGuard(matrix[j-1][i+1])
        e = checkGuard(matrix[j][i+1])
    #Borde izquierdo
    elif j != 0 and j != cells-1 and i == 0:
        n = checkGuard(matrix[j-1][i])
        ne = checkGuard(matrix[j-1][i+1])
        e = checkGuard(matrix[j][i+1])
        se = checkGuard(matrix[j+1][i+1])
        s = checkGuard(matrix[j+1][i])
    #Las demas casillas
    else:
        n = checkGuard(matrix[j-1][i])
        ne = checkGuard(matrix[j-1][i+1])
        e = checkGuard(matrix[j][i+1])
        se = checkGuard(matrix[j+1][i+1])
        s = checkGuard(matrix[j+1][i])
        sw = checkGuard(matrix[j+1][i-1])
        w = checkGuard(matrix[j][i-1])
        nw = checkGuard(matrix[j-1][i-1])

    total = n + ne + e + se + s + sw + w + nw

    return total

def run():
    """ Regresa el numero de guardias alrededor del punto """
    global cells

    global lulz
    risk = []
    positions = []
    distances = []
    decisions = []

    for j in range(cells):
        for i in range (cells):
            if(matrix[j][i] == 'A'):
                A = [j,i]

    for j in range(cells):
        for i in range(cells):
            if(matrix[j][i] == 'T'):
                print ("El target en " + str(j+1) + "," + str(i+1) + " tiene " + str(validatePoint(j,i)) + " guardianes cerca")
                risk.append(validatePoint(j,i))
                positions.append([j,i])
                print ("La distancia entre el Hitman y el target " + str(j+1) + "," + str(i+1) + " es de " + str(manhattan(A, [j,i])))
                distances.append(manhattan(A, [j,i]))

    for i in range(len(risk)):
        decisions.append(risk[i] + distances[i])

    chosen = decisions.index(min(decisions)) #Esto es un index

    print ("\n\nEl Hitman preferiría matar al target de " + str(positions[chosen][0]+1) + "," + str(positions[chosen][1]+1))

#-------------------------------------------------------------------------------
# Main~~
#-------------------------------------------------------------------------------
cells = 3
lulz = {}
matrix = creaMatriz(cells)
t1 = 'T'
t2 = 'T'
t3 = 'T'

g1 = 'G'
g2 = 'G'
g3 = 'G'
g4 = 'G'
g5 = 'G'
g6 = 'G'

a = 'A'

matrix[random.randrange(cells)][random.randrange(cells)] = t2
matrix[random.randrange(cells)][random.randrange(cells)] = g1
matrix[random.randrange(cells)][random.randrange(cells)] = g2
matrix[random.randrange(cells)][random.randrange(cells)] = g3
matrix[random.randrange(cells)][random.randrange(cells)] = t1
matrix[random.randrange(cells)][random.randrange(cells)] = g4
matrix[random.randrange(cells)][random.randrange(cells)] = g5
matrix[random.randrange(cells)][random.randrange(cells)] = g6
matrix[random.randrange(cells)][random.randrange(cells)] = t3
matrix[random.randrange(cells)][random.randrange(cells)] = a

imprimeMatriz(matrix)
print ("\n\n")
run()
