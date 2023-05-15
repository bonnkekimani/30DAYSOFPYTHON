

# ### Day 1: Python Basics
# Start by installing Python and a text editor. Learn the basics of Python, such as: 
#  variables, data types, Math Operators, Comments, Input() function, Print() function, The str(), int(), and float() Functions

# #### Exercise
# Simple Python Calculator Program: Write a simple program that does basic math operations including addition, subtraction, deletion, division, power, squareroot,etc,. 


def PythonCalculator():
    numOne= int(input("Please Enter number 1: "))
    numTwo= int(input("Please Enter number 2: "))

    operand = int(input("Enter the Operand '\n' 1:Add '\n' 2:Subtract '\n' 3:Multiply,'\n' 4:Divide: '\n' 5:Deletion,'\n' 6:Power,'\n' 7:SquareRoot,'\n' "))

    if operand ==1:
        return numOne + numTwo
    elif operand ==2:
        return numOne - numTwo
    elif operand ==3:
        return numOne * numTwo
    elif operand == 4:
        return numOne // numTwo
    elif operand ==5:
        return numOne * numTwo
    elif operand ==6:
        return numOne ** numTwo
    elif operand ==7:
        return (numOne or numTwo) ** 0.5
    else:
        return "You entered the wrong operand"

if __name__ == "__main__":
    result = PythonCalculator()
    print(result)



