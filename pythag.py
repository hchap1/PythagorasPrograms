
import math, time

def isRightAngled(a,b,c):

    return c*c == a*a +b*b

def findMissingSide(s1,s2,missingSide,mode):

    if missingSide.lower() == "hypotenuse":

        if mode.lower() == "surd":

            return "Sqrt: " + str(s1*s1 + s2*s2)

        else:

            return math.sqrt(s1*s1 + s2*s2)

    else:

        if s1 > s2:

            if mode.lower() == "surd":

                return "Sqrt: " + str(s1*s1 - s2*s2)

            else:

                return math.sqrt(s1*s1 - s2*s2)

        else:

            if mode.lower() == "surd":

                return "Sqrt: " + str(s2*s2 - s1*s1)

            else:

                return math.sqrt(s2*s2 - s1*s1)

def clear(wait):

    time.sleep(wait)

    print("\n" * 40)

    print("\n" * 40)
