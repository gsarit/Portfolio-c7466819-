#Write a program to calculate simple interest.
from decimal import Decimal
def input_value():
    principle=Decimal(input("Enter the value of principle:"))
    time=Decimal(input("Enter time:"))
    rate=Decimal(input("Enter the value of rate:"))
    return principle,time,rate
def calculation(a,b,c):
    return (a*b*c)/100
def output_value(interest):
    print("The value of simple interest is:",interest)

principle,time,rate=input_value()
result=calculation(principle,time,rate)
output_value(result)
    

