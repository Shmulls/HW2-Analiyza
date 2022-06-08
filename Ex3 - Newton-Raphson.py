# Gad Nadjar - ID : 337744155
# Rudy Haddad - ID : 336351481
# Shmuel Malikov - ID : 313530537
import sympy as sp
import math
from math import e
from sympy import lambdify

epsilon = 10 ** (-10)


def Calculate_(f):
    f_prime = f.diff(x)
    return f_prime


x = sp.symbols('x')


def check_error(start_point, end_point):
    """this function """
    flag1 = epsilon / (end_point - start_point)
    flag2 = (-1) * math.log(flag1, math.e)
    return (flag2 // math.log(2, math.e)) + 1


def Bisection_Method(func, start_point, end_point):
    """The bisection method is used to find the roots of a polynomial equation.
     It separates the interval and subdivides the interval in which the root of
      the equation lies.
      The principle behind this method is the intermediate theorem for continuous functions.
      """

    a, b = start_point, end_point
    c = (a + b) / 2
    f = lambdify(x, func)
    counter = 0
    while abs(a - b) > epsilon:
        if counter > check_error(start_point, end_point):
            return "The function does not converge"
        if f(c) * f(a) > 0:
            a = c
        else:
            b = c
        c = (a + b) / 2
        counter += 1

    print("number of iteration {}".format(counter))
    return c


def Newton_Raphson(func, func_tag, start_point, end_point):
    """The Newton-Raphson method is a way to quickly find a good approximation
     for the root of a real-valued function f ( x ) = 0 f(x) = 0 f(x)=0.
     It uses the idea that a continuous and differentiable function can be
     approximated by a straight line tangent to it.
     """
    xr = (start_point + end_point) / 2
    f = lambdify(x, func)
    fn = lambdify(x, func_tag)
    xr_1 = xr - (f(xr) / fn(xr))
    counter = 1
    while abs(xr - xr_1) > epsilon:
        if counter > 100:
            return "The Function Not Converge"
        xr = xr_1
        xr_1 = xr - (f(xr) / fn(xr))
        counter += 1

    print("Number Of Iteration {}".format(counter))
    return xr_1


def secant_method(func, start_point, end_point):
    """
    In numerical analysis, the secant method is a root-finding
     algorithm that uses a succession of roots of secant lines
     to better approximate a root of a function f. The secant
     method can be thought of as a finite-difference approximation of Newton's method.
    :param func:
    :param start_point:
    :param end_point:
    :return:
    """
    xr_minus1 = start_point
    xr = end_point
    f = lambdify(x, func)
    xr_1 = (xr_minus1 * f(xr) - xr * f(xr_minus1)) / (f(xr) - f(xr_minus1))
    counter = 1
    while abs(xr - xr_1) > epsilon:
        if counter > 100:
            return "The function not converge"
        xr_minus1 = xr
        xr = xr_1
        xr_1 = (xr_minus1 * f(xr) - xr * f(xr_minus1)) / (f(xr) - f(xr_minus1))
        counter += 1

    print("num of iteration {}".format(counter))
    return xr_1


def transition(func, start_point, end_point, n):
    f = lambdify(x, func)
    func_tag = Calculate_(func)
    next_It = start_point + 0.1
    next_It = round(next_It, 2)
    while round(start_point, 2) < end_point:
        if f(start_point) * f(next_It) < 0:
            if n == 1:
                print("x = {}".format(round(Bisection_Method(func, start_point, next_It), 6)))
            if n == 2:
                print("x = {}".format(round(Newton_Raphson(func, func_tag, start_point, next_It), 6)))
            if n == 3:
                print("x = {}".format(round(secant_method(func, start_point, next_It), 6)))
        if f(start_point) == 0:
            print("x = {}".format(start_point))

        start_point += 0.1
        start_point = round(start_point, 2)
        next_It += 0.1
        next_It = round(next_It, 2)
    if f(end_point) == 0:
        print("x = {}".format(end_point))


def main():
    choice = input("\nchoose method for solve :\n1 - Bisection Method\n2 - Newton-Raphson method\n3 - Secant Method\n")

    f = math.sin(2*e**-2*x)/x**2+5*x+6
    start = -1
    end = 2

    if choice == "1":
        transition(f, start, end, int(choice))
        main()
    elif choice == "2":
        transition(f, start, end, int(choice))
        main()
    elif choice == "3":
        transition(f, start, end, int(choice))
        main()
    else:
        print("end program. goodbye")


# activation program

main()