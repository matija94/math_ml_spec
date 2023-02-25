"""
Applying one matrics transformation onto another is called composition.

Mats are associative A1*(A2*A3) == (A1*A2)*A3
Mats are not commutative A1*A2 != A2*A1

A * r = r'
A * (n*r) = n*r'
A * (r+s) = A*r + A*s
A * (n*e1 + m*e2) = n*(A*e1) + m*(A*e2)
[ [2,3], [10,1] ] * [3,2] = [12,32]
[ [2,3], [10,1] ] * (3*[1, 0] + 2*[0,1]) = 3*([ [2,3], [10,1] ]*[1,0]) + 2*([ [2,3], [10,1] ]*[0,1]) = 3*[2,10] + 2*[3,1] = [12,32]

A*A^-1 = I

DET for 2x2 mats == a*d - b*c

Vectors are linearly independent if determinant of matrix composed of these vectors as columns is not zero.

Vector set is orthonormal if it's vectors are of unit lenght and otrhogonal to each other 
Vectors are orthogonal to each other when they are perpendicular to each other, (their dot product is 0)
To find out orthogonal vector set use gram-schmidt process
For a matrix composed of ortogonal vectors it's easy to find a inverse as it's inverse is actually a transpose.


Now in data science what we're really saying here is that wherever possible, 
we want to use an orthonormal basis vector set when we transform our data. 
That is, we want our transformation matrix to be an orthogonal matrix. 
That means the inverse is easy to compute. 
It means the transmission is reversible because it doesn't collapse space. 
It means that the projection is just the dot product. Lots of things are nice and pleasant, and easy.
When performing a transformation in the basis the is not familiar to us(i.e unit vectors are not [1 0][0 1])
Following formula is used T = E @ Te @ E^-1


If DET of matrix A is 0 then A's operational results would equal to 0.


Eigenvector formula is A*x = l * x

To findout the eigen values for the vector x use the formula (A - I*l)x = 0
l = lambda, scalar
x = vector
A = transformation matrix


Given matrix A [[a,b], [c,d]], eigenvalues are calculated by solving the characteristic polynomial 
l^2 - (a+d)l + (ad-bc)
Then use eigenvalues to discover eigenvectors of the matrix A 


Eigenbasis
In order to apply some Transformation matrix n times we want to be able to use T^n
rather than doing matrix multiplication n times
To be able to do T^n we have to find a diagonal matrix of T, one which have non zeroes on main diagonal and zeros elsewhere
Then T = eigenbasis C @ diagonal matrix D @ eigenbasis inverse
T @ T = C @ D @ C^-1 @ C @ D @ C^-1 == C @ D @ D @ C == C @ D^2 @ C^-1
T^n = C @ D^n @ C^-1
D = C^-1 @ T @ C
"""

IDENTITY_MAT = [[1, 0], [0, 1]]


def multiply_with_vector(m, vector):
    if len(m[0]) != len(vector):
        raise ValueError("len of columns diff from len of rows")
    res = [0 for _ in range(len(vector))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            res[i] += m[i][j] * vector[j]
    return res


def matrix_multiply(A, B):
    # Make sure the matrices can be multiplied (A is nxm, B is mxp)
    if len(A[0]) != len(B):
        return "Cannot multiply matrices"

    # Create the result matrix (nxp)
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Multiply the matrices element-wise
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

