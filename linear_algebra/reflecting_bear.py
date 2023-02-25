import numpy as np
from numpy.linalg import norm
from numpy import transpose

verySmallNumber = 1e-14  # That's 1×10⁻¹⁴ = 0.00000000000001


def gsBasis(A):
    B = np.array(
        A, dtype=np.float_
    )  # Make B as a copy of A, since we're going to alter it's values.
    # Loop over all vectors, starting with zero, label them with i
    for i in range(B.shape[1]):
        # Inside that loop, loop over all previous vectors, j, to subtract.
        for j in range(i):
            # Complete the code to subtract the overlap with previous vectors.
            # you'll need the current vector B[:, i] and a previous vector B[:, j]
            B[:, i] = B[:, i] - B[:, i] @ B[:, j] * B[:, j]
        # Next insert code to do the normalisation test for B[:, i]
        if norm(B[:, i]) > verySmallNumber:
            B[:, i] = B[:, i] / norm(B[:, i])
        else:
            B[:, i] = np.zeros_like(B[:, i])

    # Finally, we return the result:
    return B

def build_reflection_matrix(bearBasis) : # The parameter bearBasis is a 2×2 matrix that is passed to the function.
    # https://www.youtube.com/watch?v=rHonltF77zI

    # T = E @ Te @ E^-1
    
    # Use the gsBasis function on bearBasis to get the mirror's orthonormal basis.
    E = gsBasis(bearBasis)
    # Write a matrix in component form that performs the mirror's reflection in the mirror's basis.
    # Recall, the mirror operates by negating the last component of a vector.
    # Replace a,b,c,d with appropriate values
    TE = np.array([[1, 0],
                   [0, -1]]) @ transpose(E)
    # Combine the matrices E and TE to produce your transformation matrix.
    T = E @ TE
    # Finally, we return the result. There is no need to change this line.
    return T
