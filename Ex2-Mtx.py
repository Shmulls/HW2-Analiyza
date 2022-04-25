#Shmuel Malikov - 313530537

def isDDM(m, n):
    # for each row
    for i in range(0, n):

        # for each column, finding
        # sum of each row.
        sum = 0
        for j in range(0, n):
            sum = sum + abs(m[i][j])

        # removing the
        # diagonal element.
        sum = sum - abs(m[i][i])

        # checking if diagonal
        # element is less than
        # sum of non-diagonal
        # element.
        if (abs(m[i][i]) < sum):
            return False

    return True

def Determinant(matrix, mul):
    # Function that calcilates the determinant of matrix that recived
    # Return : Determinant matrix
    width = len(matrix)
    # Stop Conditions
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        det = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            # Change the sign of the multiply number
            sign *= -1
            #  Recursive call for determinant calculation
            det = det + mul * Determinant(m, sign * matrix[0][i])
    return det


def PivotMtx(matrix, vector):
    # This function arranges the matrix so pivot going to be diagonal
    # The returned value will be the arranged matrix.
    for i in range(len(matrix)):
        max = matrix[i][i]
        flag = i
        for j in range(i, len(matrix)):
            if(matrix[i][j] > max):
                max = matrix[i][j]
                flag = j
        if(flag != i):
            matrix[i], matrix[j] = matrix[j], matrix[i]
            vector[i], vector[j] = vector[j], vector[i]

    return matrix, vector


def MakeIMatrix(cols, rows):
    # Initialize a identity matrix
    return [[1 if x == y else 0 for y in range(cols)] for x in range(rows)]


def findLDU(matrix):
    # This function will calculate L, D and U according to the format we received in the lecture
    # The returned value will be L, D and U.
    L, D, U = MakeIMatrix(len(matrix), len(matrix)), MakeIMatrix(len(matrix), len(matrix)), MakeIMatrix(len(matrix), len(matrix))

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i > j:
                L[i][j] = matrix[i][j]
            elif i == j:
                L[i][i], U[i][i], D[i][i] = 0, 0, matrix[i][i]
            else:
                U[i][j] = matrix[i][j]

    return L, D, U


def findGH(matrix, k):
    # This function will calculate G, H according to the formulas we received in lecture
    # The returned value will be G and H
    L, D, U = findLDU(matrix)
    H = getMatrixInverse(D)
    if k == "Jacobi":
        H = getMatrixInverse(D)
    else:
        H = getMatrixInverse(addmatrix(L, D))
    G = copy_matrix(H)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            G[i][j] = -G[i][j]
    if(k == "Jacobi"):
        G = matrix_multiply(G, addmatrix(L, U))
    else:
        G = matrix_multiply(G, U)

    return G, H

def addmatrix(A, B):
    # Function that receiving two parameters A, B
    # A - Matrix 1
    # B - Matrix 2
    # The function will return the sum of the two matrix
    return [[A[i][j] + B[i][j] for j in range
(len(A[0]))] for i in range(len(A))]


def copy_matrix(matrix):
    # function that recive exsit matrix and copy it, and return new one.
    rows = len(matrix)
    cols = len(matrix[0])

    MC = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]

    for i in range(rows):
        for j in range(cols):
            MC[i][j] = matrix[i][j]

    return MC

def matrix_multiply(matrixA, matrixB):
    matrixC = [[0.0] * len(matrixB[0]) for _ in range(len(matrixA))]

    # Multiply the two matrices and store the outcome in matrixC
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                matrixC[i][j] = matrixC[i][j] + matrixA[i][k] * matrixB[k][j]

    # Return the outcome matrix
    return matrixC


def transposeMatrix(m):
    # function that receiving matrix as a parameter and doin transpose
    # return the transpose matrix
    return list(map(list,zip(*m)))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixInverse(m):
    determinant = Determinant(m, 1)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * Determinant(minor, 1))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


def JacobiandGausseSeidel(matrix, vector, method):
    # Function that receiving matrix, vector and method which define the type of calc the user asking
    # method parameter - "Jacobi" will recive jacobi soultion
    # method parameter - "GausseSeidel" will recive gausseSeidel soultion
    # this method using G and H parameters, according to the method they received
    matrix, vector = PivotMtx(matrix, vector)
    count = -1
    numberofint = 1

    if isDDM(matrix, len(matrix)) == False:
        print("Its not diagonally dominant Matrix")
        count = 150
    if method == "Jacobi":
        G, H = findGH(matrix, "Jacobi")
    else:
        G, H = findGH(matrix, "GausseSeidel")
    tmp = [[0 for _ in range(1)] for _ in range(len(vector))]
    print("0." + str(tmp))
    while count != 0:
        new_vector = tmp
        tmp = addmatrix(matrix_multiply(G, tmp), matrix_multiply(H, vector))
        print(str(numberofint) + "." + str(tmp) + "\n")
        flag = 0
        for i in range(len(tmp)):
            if abs(new_vector[i][0] - tmp[i][0]) >= 0.00001:
                flag = 1
        if flag == 0:
            break
        count -= 1
        numberofint += 1
    return tmp


# Driver Code

matrixA = [[4,2,0],[2,10,4],[0,4,5]]
vectorB = [[2], [6], [5]]

while(True):
    print("Welcome to EX2 - Jaacobi/Gausse-Seidel")
    print("Please choose ")
    selection = input("[1] Jaacobi OR [2] Gausse-Seidel (By pressing other number the program will shutdown.): ")
    if selection == "1":
        JacobiandGausseSeidel(matrixA, vectorB, "Jacobi")
    elif selection == "2":
        JacobiandGausseSeidel(matrixA, vectorB, "GausseSeidel")
    else:
        break
