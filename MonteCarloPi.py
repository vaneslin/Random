import random
#import math <--some versions of python need to import math; mine works without it but just in case


def estimate_pi(precision):
    #returns estimated value of pi to (precision) number of accurate decimal places using monte carlo method
    try:
        PI = "3.141592"  # used as a reference to check accuracy in estimated pi value

        if precision > 6 or precision < 0:
            print "Please enter in an integer representing precision between 0 and 6 inclusive."
            return -1

        else:
            # info on Monte Carlo simulation: https://brilliant.org/wiki/monte-carlo/
            areaCircle = areaSquare = 0
            maybePi = ""  # a string that is our estimation of pi
            numPoints = 0  # number of random points generated

            # while maybePi does not have adequate number of accurate decimal places (using string comparison)
            while maybePi[: precision + 2] != PI[: precision + 2]:
                x = random.random()
                y = random.random()

                if x ** 2 + y ** 2 < 1:
                    # if (x, y) is inside the circle
                    areaCircle = areaCircle + 1

                areaSquare = areaSquare + 1
                # convert to string bc while loop compares substring values for equality
                maybePi = str(4.0 * areaCircle / areaSquare)
                numPoints = numPoints + 1

        print "Estimated value is " + maybePi + " after " + str(numPoints) + " random points."
        #maybePi can sometimes be more accurate that precision argument due to randomness of generated points
        return float(maybePi)

    except TypeError:
        print "Encountered Type Error"
        return -1


#*** Testing Area ***
# estimate_pi("")
# estimate_pi(-3.4)
# estimate_pi("pyyyyyy")
# estimate_pi(12)
# estimate_pi(0)
# estimate_pi(1)
# estimate_pi(2)
# estimate_pi(3)
# estimate_pi(4)
# estimate_pi(5)
# estimate_pi(6)