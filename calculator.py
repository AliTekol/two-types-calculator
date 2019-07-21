from ops import *

print("SIMPLE CALCULATOR\n")
print("--------------------")
print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")
print("--------------------")
print("Press 5 for SCIENTIFIC CALCULATOR")
print("--------------------")
print("Type 'exit' to exit the program")

ans = 0

while True:   
    x = input("\nEnter a choice = ")

    if x == 'exit':
        exit()

    try:
        val = int(x)

        if val < 5:          
            k = input("Enter first number = ")
            l = input("Enter second number = ")

            if k == 'ans':
                k = float(ans)
                
            elif l == 'ans':
                l = float(ans)

            else:
                pass

            if val == 1:
                print("The result is ",addition(k,l))
                ans = addition(k,l)

            elif val == 2:
                print("The result is ",subtraction(k,l))
                ans = subtraction(k,l)

            elif val == 3:
                print("The result is ",multiplier(k,l))
                ans = multiplier(k,l)

            elif val == 4:

                try:
                    print("The result is ",division(k,l))
                    ans = division(k,l)

                except ZeroDivisionError:
                    print("Zero Division Error !") 

        elif val == 5:
            print("\nTHE SCIENTIFIC CALCULATOR")
            print("--------------------")
            print("Press 6 for square root function")
            print("Press 7 for power function")
            print("Press 8 for sine function")
            print("Press 9 for cosine function")
            print("Press 10 for tangent  function")
            print("Press 11 for cotangent function")
            print("Press 12 for factorial  function")
            print("Press 13 for logarithm function")
            print("--------------------")
            print("Type 'exit' to exit the program")

            if x == 'exit':
                exit()

            val = int(x)

        elif val == 6:
            k = input("Enter the number = ")

            if k == 'ans':
                k = float(ans)

            else:
                pass

            k = float(k)
            print("The result is ",square_root(k))
            ans = square_root(k)

        elif val == 7:
            m = input("Enter the base = ")
            n = input("Enter the power = ")

            if m == 'ans':
                m = float(ans)

            elif n == 'ans':
                n = float(ans) 

            else:
                pass

            m = float(m)
            n = float(n)
            print("The result is ",power(m,n))
            ans = power(m,n)

        elif val == 8:
            k = input("Enter the number = ")

            if k == 'ans':
                k = float(ans)

            else:
                pass

            k = float(k)
            print("The result is ",sine(k))
            ans = sine(k)

        elif val == 9:
            k = input("Enter the number = ")

            if k == 'ans':
                k = float(ans)

            else:
                pass

            k = float(k)
            print("The result is ",cosine(k))
            ans = cosine(k)

        elif val == 10:
            k = input("Enter the number = ")

            if k== 'ans':
                k = float(ans)

            else:
                pass

            k = float(k)
            print("The result is ",tangent(k))
            ans = tangent(k)

        elif val == 11:
            k = input("Enter the number = ")

            if k == 'ans':
                k = float(ans)

            else:
                pass

            k = float(k)
            print("The result is ",cotangent(k))
            ans = cotangent(k)

        elif val == 12:
            k = input("Enter the number = ")

            if k == 'ans':
                k = float(ans)

            else:
                pass

            k = float(k)
            print("The result is ",factorial(k))
            ans = factorial(k)

        elif val == 13:
            try:
                m = input("Enter the base = ")
                n = input("Enter the log number = ")

                if m == 'ans':
                    m = float(ans)

                elif n == 'ans':
                    n = float(ans) 

                else:
                    pass

                m = float(m)
                n = float(n)
                print("The result is ",logarithm(m,n))
                ans = logarithm(m,n)
                
            except ZeroDivisionError:
                 print("Zero Division Error !") 

        else:
            print("Please enter correct choice")

    except ValueError:
        print("The input is not a number !")