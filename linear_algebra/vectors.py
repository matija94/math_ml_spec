import math

"""
when angle between vectors r and s is 90 degrees then their dot product is 0
cosine rule can be written as dot_product(r,s) = |r|*|s|*cos(angle)
because cos(90) = 0 then dot product of orthogonal/perpendicular vectors is 0
"""


def sum_vectors(a, b):
    if len(a) != len(b):
        raise ValueError("diff lenghts")
    res = [0 for _ in range(len(a))]
    for i in range(len(a)):
        res[i] = a[i] + b[i]
    return res


def subtract_vectors(a, b):
    minus_b = [-i for i in b]
    return sum_vectors(a, minus_b)


def multiply_vector(scalar, vec):
    return [scalar * i for i in vec]


def divide_vector(scalar, vec):
    return [i / scalar for i in vec]


def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("diff lengths")
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


def vector_size(v):
    """
    Based on Pythagora's theorem, lenght of V is sqrt(v[0]**2 + .... + v[n]**2)
    size/length of vector r, which written as |r|, is equal to sqrt(dot_product(r,r))

    |r| = sqrt(dot_product(r,r))
    |r| * |r| = sqrt(dot_product(r,r)) * |r|
    |r| * |r| = sqrt(dot_product(r,r)) * sqrt(dot_product(r,r))
    |r| * |r| = dot_product(r,r)
    """
    return math.sqrt(dot_product(v, v))


def scalar_projection(r, s):
    """
    Scalar projection in terms of r and s
    sp = dot_product(r, s) / |r|

    in terms of cos(theta)
    sp = |s| * cos(theta)
    """
    return dot_product(r, s) / vector_size(s)


def angle_between_vectors(r, s):
    return dot_product(r, s) / (vector_size(r) * vector_size(s))


def normalize_vector(v):
    """
    Vector is normalized when it's divided by it's length.
    """
    return divide_vector(vector_size(v), v)


def vector_projection_for_basis_change(r, s):
    return dot_product(r, s) / dot_product(s, s)


def change_basis_for_vector(v, *basis_vecs):
    return [dot_product(v, b) / dot_product(b, b) for b in basis_vecs]


def vector_projection(r, s):
    """
    Vector projection multiplies vector it's being projected on with scalar projection.


    r @ s |r| * s/|s| 

    In case vectors are orthogonal(unit length, of size 1)
    r @ s * s
    """
    return multiply_vector(scalar_projection(r, s), normalize_vector(s))
