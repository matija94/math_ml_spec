# GRADED FUNCTION
import numpy as np

# Our function will go through the matrix replacing each row in order turning it into echelon form.
# If at any point it fails because it can't put a 1 in the leading diagonal,
# we will return the value True, otherwise, we will return False.
# There is no need to edit this function.
def isSingular(A):
    B = np.array(
        A, dtype=np.float_
    )  # Make B as a copy of A, since we're going to alter it's values.
    try:
        print(B)
        fixRowZero(B)
        print(B)
        fixRowOne(B)
        print(B)
        fixRowTwo(B)
        print(B)
        fixRowThree(B)
        print(B)
    except MatrixIsSingular:
        return True
    return False


# This next line defines our error flag. For when things go wrong if the matrix is singular.
# There is no need to edit this line.
class MatrixIsSingular(Exception):
    pass


# For Row Zero, all we require is the first element is equal to 1.
# We'll divide the row by the value of A[0, 0].
# This will get us in trouble though if A[0, 0] equals 0, so first we'll test for that,
# and if this is true, we'll add one of the lower rows to the first one before the division.
# We'll repeat the test going down each lower row until we can do the division.
# There is no need to edit this function.
def fixRowZero(A):
    print("fix row zero")
    if A[0, 0] == 0:
        print("diagonal is 0 add row 1")
        A[0] = A[0] + A[1]
        print(A)
    if A[0, 0] == 0:
        print("diagonal is 0 add row 2")
        A[0] = A[0] + A[2]
        print(A)
    if A[0, 0] == 0:
        print("diagonal is 0 add row 3")
        A[0] = A[0] + A[3]
        print(A)
    if A[0, 0] == 0:
        raise MatrixIsSingular()
    print("divide row 0 by it's first element")
    A[0] = A[0] / A[0, 0]
    print(A)
    return A


# First we'll set the sub-diagonal elements to zero, i.e. A[1,0].
# Next we want the diagonal element to be equal to one.
# We'll divide the row by the value of A[1, 1].
# Again, we need to test if this is zero.
# If so, we'll add a lower row and repeat setting the sub-diagonal elements to zero.
# There is no need to edit this function.
def fixRowOne(A):
    print(f"fiw row one {A}")
    print(f"set sub-diagonal elemts to zero, subtract {A[1,0]} * {A[0]} from row one")
    A[1] = A[1] - A[1, 0] * A[0]
    print(A)
    if A[1, 1] == 0:
        print("Diagonal is zero, add row 2 to row 1")
        A[1] = A[1] + A[2]
        print(A)
        print(f"set sub-diagonal elemts to zero, subtract {A[1,0]} * {A[0]} from row one")
        A[1] = A[1] - A[1, 0] * A[0]
    if A[1, 1] == 0:
        print("Diagonal is zero, add row 2 to row 1")
        A[1] = A[1] + A[3]
        print(A)
        print(f"set sub-diagonal elemts to zero, subtract {A[1,0]} * {A[0]} from row one")
        A[1] = A[1] - A[1, 0] * A[0]
    if A[1, 1] == 0:
        raise MatrixIsSingular()
    print("divide row 1 by its 1st element")
    A[1] = A[1] / A[1, 1]
    print(A)
    return A


# This is the first function that you should complete.
# Follow the instructions inside the function at each comment.
def fixRowTwo(A): # Insert code below to set the sub-diagonal elements of row two to zero (there are two of them).
    print("fix row to")
    print(A)
    print(f"set sub-diagonal elemts to zero, subtract {A[2,0]} * {A[0]} from row two")
    A[2] = A[2] - A[2, 0] * A[0]
    print(A)
    print(f"set sub-diagonal elemts to zero, subtract {A[2,1]} * {A[1]} from row two")
    A[2] = A[2] - A[2, 1] * A[1]
    print(A)

    # Next we'll test that the diagonal element is not zero.
    if A[2, 2] == 0:
        # Insert code below that adds a lower row to row 2.
        print("Diagonal is zero, add row 3 to row 2")
        A[2] += A[3]
        print(A)
        # Now repeat your code which sets the sub-diagonal elements to zero.
        print(f"set sub-diagonal elemts to zero, subtract {A[2,0]} * {A[0]} from row two")
        A[2] = A[2] - A[2, 0] * A[0]
        print(A)
        
        print(f"set sub-diagonal elemts to zero, subtract {A[2,1]} * {A[1]} from row two")
        A[2] = A[2] - A[2, 1] * A[1]
        print(A)

    if A[2, 2] == 0:
        raise MatrixIsSingular()
    # Finally set the diagonal element to one by dividing the whole row by that element.
    print("divide row by its 2nd element")
    A[2] = A[2] / A[2, 2]
    print(A)
    return A


# You should also complete this function
# Follow the instructions inside the function at each comment.
def fixRowThree(A):
    # Insert code below to set the sub-diagonal elements of row three to zero.
    print(f"set sub-diagonal elemts to zero, subtract {A[3,0]} * {A[0]} from row two")
    A[3] -= A[3, 0] * A[0]
    print(A)
    print(f"set sub-diagonal elemts to zero, subtract {A[3,1]} * {A[1]} from row two")
    A[3] -= A[3, 1] * A[1]
    print(A)
    print(f"set sub-diagonal elemts to zero, subtract {A[3,2]} * {A[2]} from row two")
    A[3] -= A[3, 2] * A[2]
    print(A)

    # Complete the if statement to test if the diagonal element is zero.
    if A[3, 3] == 0:
        raise MatrixIsSingular()
    # Transform the row to set the diagonal element to one.
    print("Divide row by its 3'rd ele")
    A[3] = A[3] / A[3, 3]
    print(A)

    return A
