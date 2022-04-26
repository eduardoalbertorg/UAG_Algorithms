"""
2. Usa programación dinámica para encontrar la parentización óptima de la sucesión de matrices multiplicándose p=[5, 10, 3, 12, 5, 50, 6].
Entrega el mínimo de multiplicaciones escalares con el que se puede ejecutar dicha operación y explicita la parentización usada.

"""
maxint=int(1e9+7)

def MatrixChainOrder(p, n):
    m = [[0 for x in range(n)] for x in range(n)]
 
    # m[i, j] = Minimum number of scalar
    # multiplications needed
    # to compute the matrix A[i]A[i + 1]...A[j] =
    # A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]
 
    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        m[i][i] = 0
 
    # L is chain length.
    for L in range(2, n):
        for i in range(1, n-L + 1):
            j = i + L-1
            m[i][j] = maxint
            for k in range(i, j):
 
                # q = cost / scalar multiplications
                q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
 
    return m[1][n-1]

arr = [1, 2, 3, 4]
arr = [5, 10, 3, 12, 5, 50, 6]
size = len(arr)
 
print("Minimum number of multiplications is " +
      str(MatrixChainOrder(arr, size)))