# Author: Shmuel Malikov
# Machine Precision.


# Variables
ourEpsilon = 1
loopsNum = 0

# "Function" To Find Your Machine Precision
print("\n[Machine Precision Find]")
while 1.0 + (ourEpsilon / 2) > 1.0:
    print(f'({loopsNum}) {ourEpsilon} \\ 2 = {ourEpsilon / 2}')
    loopsNum = loopsNum + 1
    ourEpsilon = ourEpsilon / 2

# Your Own Machine Precision
print(f'Your Epsilon Is --> {ourEpsilon}\n')


# Example For Equation Which Give Wrong Output (Because Of Your Machine Precision)
print("[Wrong result given in the exercise]")
print("The Example Equation --> abs(3.0 * (4.0 / 3.0 - 1) - 1)")
print("The Example Solution --> " + str(abs(3.0 * (4.0 / 3.0 - 1) - 1)) + "\n")


# The Correct Solution For The Example
print("[Correct result for after fixing the equation]")
print("The Fixed Example Equation --> abs(3.0 * (4.0 /3.0 - 1) - 1) - ourEpsilon")
print("The Fixed Example Solution --> " + str(abs(3.0 * (4.0 / 3.0 - 1) - 1) - ourEpsilon))
