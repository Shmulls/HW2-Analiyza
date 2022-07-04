# SOR method - Research in a numerical analysis course.
# Gad Nadjar - 337744155
# Shmuel Malikov - 313530537
# Rudy Haddad - 337744155
#
def SOR(A, b, w=1.25, start_first=None, eps=1e-5, max_iter=100, pItr=0):
    """
    Solves Ax=b
    Parameters
    ----------
    A  : list of list of floats : A matrix
    b : list of list of floats : b vector
    w  : float : weight
    start_first : list of floats : initial guess/None
    eps: float : error size
    max_iter: int : max iteration to run
    pItr : int : print iterations

    Returns
    -------
    list of floats
        solution to the system of linear equation

    Raises
    ------
    ValueError
        Solution does not converge
    """
    for i in range(len(A)):
        A[i].append(b[i][0])
    m=A
    n = len(m)
    start_first = [0] * n if start_first == None else start_first
    x1 = start_first[:]
    itr=0
    for __ in range(max_iter):
        for i in range(n):
            s = sum(-m[i][j] * x1[j] for j in range(n) if i != j)
            x1[i] = w * (m[i][n] + s) / m[i][i] + (1 - w) * start_first[i]
            itr+=1
            if(pItr==1):
                print("X[",itr,"]=",x1)
        if all(abs(x1[i] - start_first[i]) < eps for i in range(n)):
            return x1
        start_first = x1[:]
    raise ValueError('Solution does not converge')



A = [[3, -1, 1], [-1, 3, -1], [1, -1, 3]]
b=[[-1],[7],[-7]]
#print without iterations of Xi
print("Vector x of Ax=b: ", SOR(A, b))
#print with iterations of Xi
print("Vector x of Ax=b: ", SOR(A, b, pItr=1))
