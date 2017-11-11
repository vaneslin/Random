def calculate(exp):

    #returns evaluated simple expression if exp is formatted correctly, else returns -1
    #a simple expression is a string that is either a non-negative integer i = "i" with no leading zeroes
    #or in the form "( exp1 op exp2 )" where exp1 and exp2 are valid simple expressions and op is either +, -, *, or /
    #i.e. valid = "42" "( 5 + 3 )" "( ( 728 - ( 10 + 2 ) ) * ( 10 - 6 ) )"
    #i.e. invalid = 42 "(5+3)" "003" "44.5" "-3" "( 40 / 0 )" "( 10 + 2 ) * 5"

    try:
        print ("Your input: " + exp)

        #case 1: exp is a single non-negative int
        if is_valid_integer(exp):
            print "Evaluated expression: " + exp
            return exp

        #case 2: exp is in the form ( ... ) with the basic valid expression being ( e1 op e2 ) + CORRECT SPACING
        elif exp[0] == "(" and exp[exp.__len__()-1] == ")":
            print "Evaluated expression: " + evaluate(exp)
            return evaluate(exp)

        #case 3: exp is a hot mess, i.e. "kjlksjdf" or "10 + 4)" or "(3+4)" <-- watch your spacing
        else:
            print "Invalid expression format, spacing, or syntax"
            return -1

    except TypeError:
        print "Encountered Type Error"
        return -1

    except IndexError:
        print "Encountered IndexError"
        return -1


def evaluate(exp):
    #the word of the day is STACK
    stack = []

    #splits expression into a list of characters - either (, ), an int, or an operand ( + - * / )
    charList = exp.split()

    #initialize stack with "("
    stack.append(charList[0])
    index = 1

    while stack[0] == "(" and index < charList.__len__():
        #push things to stack and evaluate expressions as parentheses open and close
        stack.append(charList[index])
        index += 1

        #once a ")" is reached, evaluate the basic expression
        if charList[index-1] == ")":
            possibleExpression = []
            #generate a basic expression ( e1 op e2 ) from stack
            for i in range(0, 5):
                possibleExpression.insert(0, stack.pop())

            if is_valid_expression(possibleExpression) and get_value(possibleExpression) != -1:
                #evaluate value of basic expression and push back to top of stack
                evaluatedVal = str(get_value(possibleExpression))
                stack.append(evaluatedVal)
            else:
                #invalid basic expression
                return -1

    return evaluatedVal;


def is_valid_integer(num):
    # luckily, isinstance(int(str(num)), int) == False if num is a float
    try:
        #checks if its a valid non-negative int
        if isinstance(int(str(num)), int) and int(str(num)) >= 0:
            if num[0] == '0' and int(str(num)) != 0:
                #contains leading zeroes
                return False
            else:
                #valid int
                return True
        else:
            #not a non-negative integer
            return False
    except ValueError:
        return False


def is_valid_expression(expList):
    #checks if format of basic simple expression ( e1 op e2 ) is correct
    if expList[0] == "(" and expList[4] == ")" and is_valid_integer(expList[1]) and is_valid_integer(expList[3]):
            if expList[2] == "+" or expList[2] == "-" or expList[2] == "*" or expList[2] == "/":
                return True;
    return False


def get_value(expList):
    #finds value of expList: ["(", "int1", "op", "int2", ")"]
    a = int(expList[1])
    b = int(expList[3])
    if expList[2] == "+":
        return a + b
    elif expList[2] == "-":
        return a - b
    elif expList[2] == "*":
        return a * b
    elif expList[2] == "/" and b != 0:
        #assuming you want integer division here...
        return int(a/b)
    else:
        print "Cannot divide by zero"
        return -1


#*** Testing Area ***
# calculate("")
# calculate("42")
# calculate("42.03")
# calculate("-34.2")
# calculate(44.5)
# calculate("( ( 728 - ( 10 + 2 ) ) * ( 10 - 6 ) )")
# calculate("( 40 / 0 )")
# calculate("( 10 + 2 ) *")
# calculate("10 / 2")
# calculate("( foo + 5 )")
# calculate("003")