from typing import Tuple, List
import bisect
import math

def initMatrix(sizeA, sizeB):
    result = sizeA * [None]
    for i in range(sizeA):
        result[i] = sizeB * [0]
    return result


def create_unit(matrix):

    identityMat = list(range(len(matrix)))
    for i in range(len(identityMat)):
        identityMat[i] = list(range(len(identityMat)))

    for i in range(len(identityMat)):
        for j in range(len(identityMat[i])):
            identityMat[i][j] = 0.0

    for i in range(len(identityMat)):
        identityMat[i][i] = 1.0
    return identityMat



def getNorm(matrix):
    size = len(matrix)
    s = []
    for i in range(size):
        for j in range(size):
            matrix[i][j] = abs(matrix[i][j])
        s.append(sum((matrix[i])))
    return max(s)

def elementarMatrix(n, index1, index2, number):
    IdentityMatrix = create_I(n)
    IdentityMatrix[index1][index2] = number
    return IdentityMatrix

def fixMatrix(matrix):


    size = len(matrix)

    for i in range(size - 1):
        max = abs(matrix[i][i])

        for j in range(i+1, size):
            if abs(matrix[j][i] > max):
                tmp = matrix[i]
                matrix[i] = matrix[j]
                matrix[j] = tmp

    return matrix

def elementaryMatrixUnique(n, index1, index2, number):
    elementary = create_I(len(n))
    if index1 == 0 and index2 == 2 or index1 == 2 and index2 == 0:
        temp = elementary[index1]
        temp1 = elementary[index2]
        elementary[index1] = temp1
        elementary[index2] = temp
        return elementary
    if index1 == 0 and index2 == 1 or index1 == 1 and index2 == 0:
        temp = elementary[index1]
        temp1 = elementary[index2]
        elementary[index1] = temp1
        elementary[index2] = temp
        return elementary
    if index1 == 1 and index2 == 2 or index1 == 2 and index2 == 1:
        temp = elementary[index1]
        temp1 = elementary[index2]
        elementary[index1] = temp1
        elementary[index2] = temp
        return elementary

def funcPrint(A):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                                  for row in A]))


def MultiplicationMatrixSolution(M1, M2):
    size1 = len(M1)
    size2 = (len(M1[0]))
    size3 = len(M2)
    size4 = 1
    if size2 != size3:
        return ArithmeticError("the size is not correct")
    result = initMatrix(size1, size4)
    for i in range(size1):
        for j in range(size4):
            for k in range(size2):
                result[i][j] += M1[i][k] * M2[k]

    return result

def Multiplication(M1, M2):
    size1 = len(M1)
    size2 = (len(M1[0]))
    size3 = len(M2)
    size4 = len(M2[0])
    if size2 != size3:
        return ArithmeticError("the size is not correct")
    result = initMatrix(size1, size4)
    for i in range(size1):
        for j in range(size4):
            for k in range(size2):
                result[i][j] += M1[i][k] * M2[k][j]


    return result



def matrix_multiply(matA, matB):
    rowsA = len(matA)
    colsA = len(matA[0])
    rowsB = len(matB)
    colsB = len(matB[0])
    if colsA != rowsB:
        print('The columns number of matrix-A must be equal to rows  number of matrix-B')
    resMat = []
    while len(resMat) < rowsA:
        resMat.append([])
        while len(resMat[-1]) < colsB:
            resMat[-1].append(0.0)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += matA[i][k] * matB[k][j]
            resMat[i][j] = total
    return resMat


def InverseMatrice(A, B):
    trueelementary = A
    lst = []
    lst2 = []
    lst3 = []
    bMatrix = B
    counter = 1
    determinant = getMatrixDeternminant(trueelementary)
    if determinant == 0:
        raise "There's is no inverse"
    else:
        counter1 = 0
        counter2 = -1
        for i in range(len(trueelementary)):
            temp = trueelementary[i][i]
            counter2 = i
            counter1 = 0
            for j in range(len(trueelementary[i])):
                if j >= i:
                    if abs(trueelementary[j][i]) > abs(temp):
                        counter1 += 1 + i
                        temp = trueelementary[j][i]
            if counter1 == 0:
                pass
            else:
                if i == 0:
                    if counter1 == 1:
                        elementary = elementaryMatrixUnique(trueelementary, counter1 + 1, counter2, 1)
                        lst2.append(elementary)
                        print("Elementary : {}".format(counter))
                        funcprintt(elementary)
                        print("\n")
                        print("Matrix A :")
                        funcprintt(trueelementary)
                        print("\n")
                        trueelementary = Multiplication(elementary, trueelementary)
                        print("Elementary {} multiply by the Matrix X : ".format(counter))
                        funcprintt(trueelementary)
                        print("\n")
                        print(
                            "==========================================================================================")
                        print("\n")
                    else:
                        elementary = elementaryMatrixUnique(trueelementary, counter1, counter2, 1)
                        lst2.append(elementary)
                        print("Elementary : {}".format(counter))
                        funcprintt(elementary)
                        print("\n")
                        print("Matrix A :")
                        funcprintt(trueelementary)
                        print("\n")
                        trueelementary = Multiplication(elementary, trueelementary)
                        print("Elementary {} multiply by the Matrix X : ".format(counter))
                        counter += 1
                        funcprintt(trueelementary)
                        print("\n")
                        print(
                            "==========================================================================================")
                        print("\n")
                else:
                    elementary = elementaryMatrixUnique(trueelementary, counter1, counter2, 1)
                    lst2.append(elementary)
                    print("Elementary : {}".format(counter))
                    funcprintt(elementary)
                    print("\n")
                    print("Matrix A :")
                    funcprintt(trueelementary)
                    print("\n")
                    trueelementary = Multiplication(elementary, trueelementary)
                    print("Elementary {} multiply by the Matrix X : ".format(counter))
                    counter += 1
                    funcprintt(trueelementary)
                    print("\n")
                    print("==========================================================================================")
                    print("\n")



        for i in range(len(trueelementary)):
            if trueelementary[i][i] != float(1) and i < len(trueelementary) or trueelementary[i][i] != int(
                    1) and i < len(trueelementary):
                b = 1 / trueelementary[i][i]
                elementary = elementarMatrix(len(trueelementary), i, i, b)
                print("Elementary : {}".format(counter))
                funcprintt(elementary)
                print("\n")
                print("Matrix A :")
                funcprintt(trueelementary)
                print("\n")
                trueelementary = Multiplication(elementary, trueelementary)
                print("Elementary {} multiply by the Matrix X : ".format(counter))
                counter += 1
                funcprintt(trueelementary)
                print("\n")
                print("==========================================================================================")
                print("\n")
                lst.append(trueelementary)
                lst2.append(elementary)
            for j in range(len(trueelementary[i])):
                if j != i and trueelementary[j][i] != int(0) and j > i or j != i and trueelementary[j][i] != float(
                        0) and j > i:
                    d = (trueelementary[j][i] / trueelementary[i][i]) * -1
                    elementary = elementarMatrix(len(trueelementary), j, i, d)
                    print("Elementary : {}".format(counter))
                    funcprintt(elementary)
                    print("\n")
                    print("Matrix A :")
                    funcprintt(trueelementary)
                    print("\n")
                    trueelementary = Multiplication(elementary, trueelementary)
                    print("Elementary {} multiply by the Matrix X : ".format(counter))
                    counter += 1
                    funcprintt(trueelementary)
                    print("\n")
                    print("==========================================================================================")
                    print("\n")
                    lst.append(trueelementary)
                    lst2.append(elementary)
        for i in range(len(trueelementary) - 1, -1, -1):
            for j in range(len(trueelementary[i]) - 1, -1, -1):
                if trueelementary[i][j] != int(0) and trueelementary[i][j] != float(0.0) and trueelementary[i][
                    j] != int(1) and trueelementary[i][j] != float(1.0) and trueelementary[i][j] and i != j:
                    d = (trueelementary[i][j] / trueelementary[i][i]) * -1
                    elementary = elementarMatrix(len(trueelementary), i, j, d)
                    print("Elementary : {}".format(counter))
                    funcprintt(elementary)
                    print("\n")
                    print("Matrix A :")
                    funcprintt(trueelementary)
                    print("\n")
                    trueelementary = Multiplication(elementary, trueelementary)
                    print("Elementary {} multiply by the Matrix X : ".format(counter))
                    counter += 1
                    funcprintt(trueelementary)
                    print("\n")
                    print("==========================================================================================")
                    print("\n")
                    lst.append(trueelementary)
                    lst2.append(elementary)
        temp = lst2[0]
        for i in range(1, len(lst2), 1):
            temp2 = lst2[i]
            temp = Multiplication(temp2, temp)
        print("Inverse Matrix :")
        funcprintt(temp)
        print("\n")
        print("==========================================================================================")
        print("\n")
        print("Vector X : ")
        print(MultiplicationMatrixSolution(temp, bMatrix))

def funcprintt(A):
    print('\n'.join(['             '.join(['{:4}'.format(item) for item in row])
                     for row in A]))

def getMatrixMinor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

def getMatrixDeternminant(m):
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * m[0][c] * getMatrixDeternminant(getMatrixMinor(m, 0, c))
    return determinant

def DominantDiagonal(matrix):

    size = len(matrix)
    normVector = getMax(matrix)

    for i in range(size):
        s = sum(matrix[i]) - normVector[i]

        if s > normVector[i]:
            return False

    return True

def getMax(matrix):

    size = len(matrix)
    normVector = []

    for i in range(size):
        for j in range(size):
            matrix[i][j] = abs(matrix[i][j])

        normVector.append(max(matrix[i]))

    return normVector

def getPivot(matrix):

    pivote = []
    size = len(matrix)

    for i in range(size):
        for j in range(size):
            if i == j:
                pivote.append(matrix[i][j])

    return pivote

def GaussSeidelMethod(matrixA, matrixB):


    x1 = [0, 0, 0]
    x2 = [0, 0, 0]
    pivote = getPivot(matrixA)
    count = 1
    print("X.{} --> {}".format(0, x2))

    while True:
        i = 0
        j = 0

        x2[i] = (matrixB[i] - matrixA[j][1] * x1[1] - matrixA[j][2] * x1[2]) / pivote[i]
        i += 1
        j += 1
        x2[i] = (matrixB[i] - matrixA[j][0] * x2[0] - matrixA[j][2] * x1[2]) / pivote[i]
        i += 1
        j += 1
        x2[i] = (matrixB[i] - matrixA[j][0] * x2[0] - matrixA[j][1] * x2[1]) / pivote[i]

        print("X.{} --> {}".format(count, x2))
        count += 1

        if abs(x2[0] - x1[0]) < 0.0000001:
            break

        if count == 151:
            print("The matrix is not convergent !")
            break

        x1 = [i for i in x2]

def JacobiMethod(matrixA, matrixB):

    x1 = [0, 0, 0]
    x2 = [0, 0, 0]
    pivote = getPivot(matrixA)
    count = 1
    print("X.{} --> {}".format(0, x2))

    while True:
        i = 0
        j = 0

        x2[i] = (matrixB[i] - matrixA[j][1] * x1[1] - matrixA[j][2] * x1[2]) / pivote[i]
        i += 1
        j += 1
        x2[i] = (matrixB[i] - matrixA[j][0] * x1[0] - matrixA[j][2] * x1[2]) / pivote[i]
        i += 1
        j += 1
        x2[i] = (matrixB[i] - matrixA[j][0] * x1[0] - matrixA[j][1] *x1[1]) / pivote[i]

        print("X.{} --> {}".format(count, x2))
        count += 1

        if abs(x2[0] - x1[0]) < 0.0000001:
            return True

        if count == 151:
            print("The matrix is not convergent !")
            break


        x1 = [i for i in x2]


def linear_interpolation(thePoints, findPoint):
    for row in range(len(thePoints) - 1):
        if (findPoint > thePoints[row][0]) and findPoint < thePoints[row + 1][0]:
            x1 = thePoints[row][0]
            x2 = thePoints[row + 1][0]
            y1 = thePoints[row][1]
            y2 = thePoints[row + 1][1]
            return (((y1 - y2) / (x1 - x2)) * findPoint) + ((y2 * x1 - y1 * x2) / (x1 - x2))




def create_I(matrix):  # A function that creates and returns the unit matrix
    I = list(range(len(matrix)))  # make it list
    for i in range(len(I)):
        I[i] = list(range(len(I)))

    for i in range(len(I)):
        for j in range(len(I[i])):
            I[i][j] = 0.0  # put the zero

    for i in range(len(I)):
        I[i][i] = 1.0  # put the pivot
    return I  # unit matrix


def inverse(matrix):  # A function that creates and returns the inverse matrix to matrix A
    new_matrix = create_I(matrix)  # Creating the unit matrix
    count = 0
    check = False  # flag
    while count <= len(matrix) and check == False:
        if matrix[count][0] != 0:  # if the val in place not 0
            check = True  # flag
        count = count + 1  # ++
    if not check:
        print("ERROR")
    else:
        temp = matrix[count - 1]
        matrix[count - 1] = matrix[0]  # put zero
        matrix[0] = temp
        temp = new_matrix[count - 1]
        new_matrix[count - 1] = new_matrix[0]
        new_matrix[0] = temp

        for x in range(len(matrix)):
            divider = matrix[x][x]  # find the div val
            if divider == 0:
                divider = 1
            for i in range(len(matrix)):
                matrix[x][i] = matrix[x][i] / divider  # find the new index
                new_matrix[x][i] = new_matrix[x][i] / divider
            for row in range(len(matrix)):
                if row != x:
                    divider = matrix[row][x]
                    for i in range(len(matrix)):
                        matrix[row][i] = matrix[row][i] - divider * matrix[x][i]
                        new_matrix[row][i] = new_matrix[row][i] - divider * new_matrix[x][i]
    return new_matrix  # Return of the inverse matrix






def Polynomial_interpolation(points, find_point):
    # creating a new matrix
    mat = list(range(len(points)))
    for i in range(len(mat)):
        mat[i] = list(range(len(mat)))
    for row in range(len(points)):
        mat[row][0] = 1
    for row in range(len(points)):
        for col in range(1, len(points)):
            mat[row][col] = pow(points[row][0], col)
    res_mat = list(range(len(points)))
    for i in range(len(res_mat)):
        res_mat[i] = list(range(1))
    for row in range(len(res_mat)):
        res_mat[row][0] = points[row][1]
    vector_a = matrix_multiply(inverse(mat), res_mat)
    sum = 0
    for i in range(len(vector_a)):
        if i == 0:
            sum = vector_a[i][0]
            print(sum)
        else:
            sum += vector_a[i][0] * find_point ** i
            print(sum)
    return sum


def lagrange_interpolation(thePoints, findPoint):
    sum_ = 0
    for i in range(len(thePoints)):
        mul = 1
        for j in range(len(thePoints)):
            if i == j:
                continue
            mul = mul * ((findPoint - thePoints[j][0]) / (thePoints[i][0] - thePoints[j][0]))
        sum_ = sum_ + mul * thePoints[i][1]
    return sum_


def P(m, n, thePoints, findPoint):
    if m == n:
        return thePoints[m][1]
    resP = ((findPoint - thePoints[m][0]) * P(m + 1, n, thePoints, findPoint) - (findPoint - thePoints[n][0]) *
            P(m, n - 1, thePoints, findPoint)) \
        / (thePoints[n][0] - thePoints[m][0])

    return resP


def neville_interpolation(thePoints, findPoint):
    resMat = list(range(len(thePoints)))
    for k in range(len(thePoints)):
        resMat[k] = list(range(len(thePoints)))

    for i in range(len(thePoints)):
        for j in range(i, len(thePoints)):
            resMat[i][j] = P(i, j, thePoints, findPoint)
            print(resMat[i][j])
    return resMat[0][len(thePoints) - 1]





def compute_changes(x: List[float]) -> List[float]:
    return [x[i + 1] - x[i] for i in range(len(x) - 1)]


def create_tridiagonalmatrix(n: int, h: List[float]) -> Tuple[List[float], List[float], List[float]]:
    A = [h[i] / (h[i] + h[i + 1]) for i in range(n - 2)] + [0]
    B = [2] * n
    C = [0] + [h[i + 1] / (h[i] + h[i + 1]) for i in range(n - 2)]
    return A, B, C


def create_target(n: int, h: List[float], y: List[float]):
    return [0] + [6 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1]) / (h[i] + h[i - 1]) for i in
                  range(1, n - 1)] + [0]


def solve_tridiagonalsystem(A: List[float], B: List[float], C: List[float], D: List[float]):
    c_p = C + [0]
    d_p = [0] * len(B)
    X = [0] * len(B)

    c_p[0] = C[0] / B[0]
    d_p[0] = D[0] / B[0]
    for i in range(1, len(B)):
        c_p[i] = c_p[i] / (B[i] - c_p[i - 1] * A[i - 1])
        d_p[i] = (D[i] - d_p[i - 1] * A[i - 1]) / (B[i] - c_p[i - 1] * A[i - 1])

    X[-1] = d_p[-1]
    for i in range(len(B) - 2, -1, -1):
        X[i] = d_p[i] - c_p[i] * X[i + 1]

    return X


def compute_spline(x: List[float], y: List[float], value):
    n = len(x)
    if n < 3:
        raise ValueError('Too short an array')
    if n != len(y):
        raise ValueError('Array lengths are different')

    h = compute_changes(x)
    if any(v < 0 for v in h):
        raise ValueError('X must be strictly increasing')

    A, B, C = create_tridiagonalmatrix(n, h)
    D = create_target(n, h, y)

    M = solve_tridiagonalsystem(A, B, C, D)
    xx = value
    for i in range(len(x)):
        if x[i] > xx:
            i = i - 1
            break
    coefficients = (pow(x[i + 1] - xx, 3) * M[i] + pow(xx - x[i], 3) * M[i + 1]) / (6 * h[i])
    coefficients += ((x[i + 1] - xx) * y[i] + (xx - x[i]) * y[i + 1]) / h[i]
    coefficients -= (((x[i + 1] - xx) * M[i] + (xx - x[i]) * M[i + 1]) * h[i]) / 6
    return coefficients



















def main():
    while True:
        user_choice = int((input("\nPlease choose one option:\n"
                                 "1. Linear Interpolation\n"
                                 "2. Polynomial Interpolation\n"
                                 "3. Lagrange Interpolation\n"
                                 "4. Neville Interpolation\n"
                                 "5. Spline Cubine\n"
                                 "6. Exit\n"
                                )))

        if user_choice == 6:
            print("Bye.")
            exit(1)

        given_points = [[1.2, 1.5095], [1.3, 1.6984], [1.4, 1.9043], [1.5, 2.1293], [1.6, 2.3756]]
        val_point = 1.47
        datax = [1, 1.3, 1.6, 1.9, 2.2]
        datay = [0.7651, 0.62, 0.4554, 0.2818, 0.1103]

        dataxx = [0, (math.pi / 6), (math.pi / 4), (math.pi / 2)]
        datayy = [0, 0.5, 0.7072, 1]
        valpoint = math.pi / 3

        print("________________________________________")
        print('The points are:', given_points)
        print('The point:', val_point)

        if user_choice == 1:
            print("Using the Linear Interpolation method:")
            print('The value of point is: ', "%.4f" % linear_interpolation(given_points, val_point))
            main()

        elif user_choice == 2:
            print("Polynomial Interpolation")
            print('The value of point is: ', "%.4f" % Polynomial_interpolation(given_points, val_point))
            main()

        elif user_choice == 3:
            print("Lagrange Interpolation")
            print('The value of point is: ', "%.4f" % lagrange_interpolation(given_points, val_point))
            main()

        elif user_choice == 4:
            print("Neville Interpolation")
            print('The value of point is: ', "%.4f" % neville_interpolation(given_points, val_point))
            main()

        elif user_choice == 5:
            print("Spline Cubine")
            solve = compute_spline(dataxx, datayy, valpoint)
            print('The value of point is: ', "%.4f" % solve)

        else:
            print("Please enter a number between 1-5 only.\nPress 5 to exit.")
            print("________________________________________\n\n")


main()



