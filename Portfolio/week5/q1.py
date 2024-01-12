#write a program to add two numbers calculation,process and print should be in
#diff function

def input_value():
    num1 = float(input("Enter the first num:"))
    num2 = float(input("Enter the second num:"))
    return num1, num2

def calculation(a,b):
    return a+ b

def output_value(result):

    print("The sum of two numbers is:",result )

number1,number2=input_value()
sum=calculation(number1,number2)
y= output_value(sum)







