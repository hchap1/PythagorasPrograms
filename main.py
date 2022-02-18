
import pythag, math

while True:
    try:        
        action = input("[T]hree Dimensional Pythagoras, [C]heck if a triangles is right-angled, [F]ind missing side of right angled-triangle, [D]ifference between length of hypotenuse and length of combined sides, [H]elp!\n = ")
        if action.lower()[0] == "c":
            a = float(input("Side A?\n = "))
            b = float(input("Side B?\n = "))
            c = float(input("Hypotenuse?\n = "))
            print(str(pythag.isRightAngled(a,b,c)))
        elif action.lower()[0] == "f":
            missingSide = input("[H]ypotenuse, or [S]maller side?\n = ").lower()[0]
            form = input("[S]urd form, or [N]ormal?\n = ")
            dp = int(input("How many DP?\n = "))
            if form.lower()[0] == "s":
                form = "surd"
            else:
                form = "normal"
            if missingSide == "h":
                sideOne = float(input("Small side one?\n = "))
                sideTwo = float(input("Small side two?\n = "))
                print("c^2 = a^2 + b^2\na = sqrt(c^2 - b^2)\nx = sqrt(%s^2 + %s^2)" % (str(sideOne), str(sideTwo)))
                print(str(round(pythag.findMissingSide(sideOne,sideTwo,"hypotenuse",form),dp)))
            else:
                hypotenuse = float(input("Enter the hypotenuse?\n = "))
                sideTwo = float(input("Enter the smaller side?\n = "))
                print("c^2 = a^2 + b^2\na = sqrt(c^2 - b^2)\nx = sqrt(%s^2 - %s^2)" % (str(sideOne), str(sideTwo)))
                print(str(round(pythag.findMissingSide(hypotenuse,sideTwo,"ss",form),dp)))
        elif action.lower()[0] == "d":
            a = float(input("Enter A\n = "))
            b = float(input("Enter B\n = "))
            dp = int(input("How many DP?\n = "))
            c = pythag.findMissingSide(a,b,"hypotenuse","normal")
            ans = round((a + b) - c, dp)
            print("With hypotenuse %s, sides a and b are %s units greater than c." % (round(c,dp), ans))
        elif action.lower()[0] == "h":
            print("\nTo start, choose whether you want to find the missing side of a right angled triangle (find), and enter the missing side (hypotenuse or short side), than enter the other two sides, normal or surd, meaning absolute value or normal value. If the output is the decimal than it is reccomended to use SURD, as it could lead to a progressive error if you round. Now, choose how many decimal places to round to, and hit enter to get the result. If you want to check if a triangle is right-angled given the three sides, enter (check), and enter the three sides. If you want to see how much longer the two sides combined are than the hypotenuse given A and B of a right-angled triangled, press (D).\n") 
        elif action.lower()[0] == "t":
            print("You had to choose the most painful option didn't you?\n")
            a = float(input("Width?\n = "))
            b = float(input("Length?\n = "))
            c = float(input("Height?\n = "))
            dp = int(input("DP?\n = "))
            d = pythag.findMissingSide(a,b,"hypotenuse","normal")
            e = pythag.findMissingSide(d,c,"hypotenuse","normal")
            print("x = %s" % round(e,dp))
        input("HIT ENTER TO CONTINUE!")
        pythag.clear(0)
    except:
        print("\nSomething went wrong. Try entering proper numbers, or a valid option.\n")
        pythag.clear(4)

            



