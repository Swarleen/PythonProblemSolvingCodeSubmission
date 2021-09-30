# Program Solving with Python/Intro to Competitive Programming, Fall 2021
# Eternal University, Baru Sahib
# Cite: John Guttag. 6.00SC Introduction to Computer Science and Programming. Spring 2011. Massachusetts Institute of Technology: MIT OpenCourseWare, https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011. License: Creative Commons BY-NC-SA.
#
#
# Problem Set 2
# Successive Approximation
# Name: Swarleen Bhamra
# Time spent: 5-6 hr


def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print(evaluate_poly(poly, x))  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    # TO DO ...

#Initally taking value of poly = 0.
    val_of_poly = 0                
    for i in poly:
        #appending value in "val_of_poly" with the equation.
        val_of_poly += (poly[(poly.index(i))]) * (x ** (poly.index(i)))            
    return val_of_poly
poly=(0.0,0.0,5.0,9.3,7.0)
x = -13
print(evaluate_poly(poly,x))
Tuple=list(poly)
poly=tuple(Tuple)
print(Tuple)



def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print(compute_deriv(poly))        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    # TO DO ...

    Derivative = ()
    for i in poly:
       if (poly.index(i)) > 0:
        #Using formula to find derivative, for the conditions when the value of polly is greater than 0.
        Derivative = Derivative +(((poly.index(i)) * i),)
    return Derivative
poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
print(compute_deriv(poly))


def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print(compute_root(poly, x_0, epsilon))
    (0.806790753796352, 8)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    # TO DO ...
   
    val = x_0
    j = 1.0
    deriv = compute_deriv(poly)
    while abs(evaluate_poly(poly, val)) > epsilon:
        val = val - evaluate_poly(poly, val) / evaluate_poly(deriv, val)
        j += 1.0
    return val, j
#assigning values yo polly.
poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
epsilon= .0001
x_0 = 0.1
print(compute_root(poly,x_0,epsilon))

#Tested
        

