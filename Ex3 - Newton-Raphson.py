#Shmuel Malikov - 313530537

from math import cos
import sympy as sp
from sympy.utilities.lambdify import lambdify


Epsilon = 0.0000001


def Bisection_Method(func1, f1Tag, sPoint, ePoint, Epsilon):
    """
        This function finds the root between the starting point to the end point based the Bisection Method.
        :param func1: function
        :param f1Tag: flag
        :param sPoint: Start point
        :param ePoint: End point
        :param Epsilon: Epsilon point
        :return: result
    """

    #used to count the Iterations
    counter = 0

    range_list_f = find_range_f(func1, sPoint, ePoint)
    range_list_fT = find_range_fT(f1Tag, sPoint, ePoint)

    result = []

    if range_list_f and range_list_fT:
        for i in range(0, len(range_list_f), 2):

            #The loop will run until the difference between the points will be bigger than epsilon
            while (range_list_f[i + 1] - range_list_f[i]) > Epsilon:

                x_m = (range_list_f[i] + range_list_f[i + 1]) / 2

                counter += 1
                print("Iteration: ", counter)

                if func1(range_list_f[i]) * func1(x_m) > 0:
                    range_list_f[i] = x_m

                else:
                    range_list_f[i + 1] = x_m

            if round(x_m, 6) not in result:
                print("x: ", round(x_m, 6))
                result.append(round(x_m, 6))

        for i in range(0, len(range_list_fT), 2):

            #The loop will run until the difference between the points will be bigger than epsilon
            while (range_list_fT[i + 1] - range_list_fT[i]) > Epsilon:

                x_m = (range_list_fT[i] + range_list_fT[i + 1]) / 2

                counter += 1
                print("Iteration: ", counter)

                if func1(range_list_fT[i]) * func1(x_m) > 0:
                    range_list_fT[i] = x_m
                else:
                    range_list_fT[i + 1] = x_m

            if round(x_m, 4) not in result:
                print("x: ", round(x_m, 4))
                result.append(round(x_m, 4))

    n = len(result)
    i = 0
    while i < n and n != 0:
        if not -0.1 < func1(result[i]) < 0.1:
            del result[i]
            n -= 1
            i = 0
        else:
            i += 1

    return result


def Newton_Raphson(func2, f2Tag, sPoint, ePoint, Epsilon):
    """
        This function finds the root between the starting point to the end point based the Newton-Raphson Method.
        :param func2: function
        :param f2Tag: flag
        :param sPoint: Start point
        :param ePoint: End point
        :param Epsilon: Epsilon point
        :return: result
    """

    x_r = (ePoint + sPoint) / 2
    if func2(x_r) != 0:
        x_next = x_r - (func2(x_r) / f2Tag(x_r))
    else:
        print("Please wait trying  closer range")
        return None

    counter = 1

    if round(func2(sPoint), 5) == 0:
        print("x: ", round(sPoint, 4))
        return round(x_r, 5)

    elif round(func2(ePoint), 5) == 0:
        print("x: ", round(ePoint, 4))
        return ePoint


    if func2(sPoint) > 0 and func2(ePoint) < 0 or func2(sPoint) < 0 and func2(ePoint) > 0:
        #The loop will check when the range between two number is small then epsilon
        while x_next - x_r < Epsilon:
            # Do it if the condition is not met

            print("Iteration: ", counter)

            if round(func2(x_r), 5) == 0:
                print("x: ", round(x_r, 6))
                return round(x_r, 6)

            counter += 1
            x_r = x_next
            x_next = x_r - (func2(x_r) / f2Tag(x_r))
    else:
        print("Error! The function does not converge")


def Secant_Method(func3, sPoint, ePoint, Epsilon):
    """
        This function finds the root between the starting point to the end point based the Secant Method.
        :param func3: function
        :param sPoint: Start point
        :param ePoint: End point
        :param Epsilon: Epsilon point
        :return: result list
    """
    result_list = []
    counter = 1

    range_list = find_range_f(func3, sPoint, ePoint)

    for i in range(0, len(range_list), 2):
        x_r = range_list[i]
        x_next = range_list[i + 1]

        while abs(x_next - x_r) > Epsilon:

            print("Iteration: ", counter)
            if round(func3(x_r), 6) == 0:
                print("x: ", round(x_r, 6))
                result_list.append(round(x_r, 6))

            last_r = x_r
            x_r = x_next
            x_next = (last_r * func3(x_r) - x_r * func3(last_r)) / (func3(x_r) - func3(last_r))
            counter += 1
    return result_list

def find_range_f(f, sPoint, ePoint):
    """
        Finds the suspected points and intersecting a function on the axis
        :param f: function
        :param sPoint: Start point
        :param ePoint: End point
        :return:  Range list
    """
    # Run between the start point to the end point, with jumping 0.1 each time.
    range_list_function = []

    # As long as there is a certain range between the start point and the end point
    while ePoint >= sPoint:
        if f(sPoint) * f(sPoint + 0.1) < 0:
            range_list_function.append(round(sPoint, 3))
            range_list_function.append(round(sPoint + 0.1, 3))
        sPoint += 0.1

    # Returns two lists that contain values that change the functions
    return range_list_function


def find_range_fT(fTag, sPoint, ePoint):
    """
        Finds the suspected points and intersecting a function derivative on the axis.
        :param f: function
        :param sPoint: Start point
        :param ePoint: End point
        :return:  Range list
    """
    range_list_fT = []
    while ePoint >= sPoint:
        if fTag(sPoint) * fTag(sPoint + 0.1) < 0:
            range_list_fT.append(round(sPoint, 3))
            range_list_fT.append(round(sPoint + 0.1, 3))
        sPoint += 0.1

    # Returns two lists that contain values that change the functions
    return range_list_fT


def main():

    x = sp.symbols('x')

    sPoint = 0
    ePoint = 0

    while True:
        print("Please choose method to solve - \nPress [1]: Bisection Method\n"
        "Press [2]: Newton Raphson Method\nPress [3]: Secant Method\nAny other KEY will exit the program\n")
        method = input()

        if method == "1":
            print("\n#######################################")
            print("Bisection Method")
            f1 = x ** 4 + x ** 3 - 3 * x ** 2
            f1Tag = f1.diff(x)
            print('our function -->', f1)
            print('our function after derivative -->', f1Tag)
            f1 = lambdify(x, f1)
            f1Tag = lambdify(x, f1Tag)
            sPoint = -3.0
            ePoint = 2.0
            result_list = Bisection_Method(f1, f1Tag, sPoint, ePoint, Epsilon)
            if result_list:
                print("#######################################")
                print("The results of the function are: ", result_list)
            else:
                print("No result found!")

        elif method == "2":
            print("\n#######################################")
            print("Newton Raphson")
            f2 = x ** 3 - x - 1
            f2Tag = f2.diff(x)
            print('our function -->', f2)
            print('our function after derivative -->', f2Tag)
            f2 = lambdify(x, f2)
            f2Tag = lambdify(x, f2Tag)
            result_list = []
            sPoint = 1.0
            ePoint = 2.0

            range_list_f = find_range_f(f2, sPoint, ePoint)
            range_list_fT = find_range_fT(f2Tag, sPoint, ePoint)

            for i in range(0, len(range_list_f), 2):
                answer = Newton_Raphson(f2, f2Tag, range_list_f[i], range_list_f[i+1], Epsilon)
                if answer not in result_list and answer is not None:
                    result_list.append(answer)

            for i in range(0, len(range_list_fT), 2):
                answer = Newton_Raphson(f2, f2Tag, sPoint, ePoint, Epsilon)
                if answer not in result_list and answer is not None:
                    result_list.append(answer)

            if result_list:
                print("#######################################")
                print("The results of the function are: ", result_list)

            else:
                print("No result found!")

        elif method == "3":

            print("\n#######################################")
            print("Secant Method")
            y = sp.cos
            f3 = x ** 3 - y(x)
            print('our function: ', f3)
            f3 = lambdify(x, f3)
            sPoint = 0.0
            ePoint = 1.0

            result_list = Secant_Method(f3, sPoint, ePoint, Epsilon)
            if result_list:
                print("#######################################")
                print("The results of the function are: ", result_list)
            else:
                print("No result found!")
        else:
            print("THANK YOU!")
            break


main()