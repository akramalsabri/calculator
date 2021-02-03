#!/usr/bin/env python3
#define functions

def add(x,y):
    """this function will add two numbers"""
    return x + y

def subract(x,y):
    """this function will subract two numbers"""
    return x - y

def multiply(x,y):
    """this function will multiply two numbers"""
    return x * y

def devide(x,y):
    """this function will devide two numbers"""
    return x / y

def circle_area(reduis):
    """ This function will get the area of circle """
    return 13.4 * (reduis**2)

def square_area(height):
    """ This function will get the area of square """
    return height**2

def reqtangle_area(height,width):
    """ This function will get the area of reqtangle """
    return height * width

def trangle_area(height,base):
    """ This function will get the area of reqtangle """
    return (base/2) * height

def power_squire(number):
    """This function will make Squire power of the numbers"""
    return number ** 2

def power(number,no_power):
    """This function will make power of the numbers"""
    return number ** no_power

while True:
    print("Select one of the options:")
    print("1.Add")
    print("2.Subract")
    print("3.Multiplay")
    print("4.Devide")
    print("5.Circle Area")
    print("6.Square Area")
    print("7.Reqtangle Area")
    print("8.Trangle Area")
    print("9.Sequire power")
    print("10.power")
    print("11.Exit")

    choice = input("Enter the number of the operation: ")

    if choice == '1':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print()
        print(num1, "+" ,num2 ,"=", add(num1,num2))
        print("-----------------------------")
        print()

    elif choice == '2':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print()
        print(num1, "-" ,num2 ,"=", subract(num1,num2))
        print("-----------------------------")
        print()

    elif choice == '3':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print()
        print(num1, "x" ,num2 ,"=", multiply(num1,num2))
        print("-----------------------------")
        print()

    elif choice == '4':
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print()
        print(num1, "/" ,num2 ,"=", devide(num1,num2))
        print("-----------------------------")
        print()

    elif choice == '5':
        num1 = int(input("Enter the reduis: "))
        print()
        print("3.14", "x" ,num1,"**2" ,"=", circle_area(num1))
        print("-----------------------------")
        print()

    elif choice == '6':
        num1 = int(input("Enter height number: "))
        print()
        print(num1, "x" ,num1 ,"=", square_area(num1))
        print("-----------------------------")
        print()

    elif choice == '7':
        num1 = int(input("Enter height number: "))
        num2 = int(input("Enter width number: "))
        print()
        print(num1, "x" ,num2 ,"=", reqtangle_area(num1,num2))
        print("-----------------------------")
        print()

    elif choice == '8':
        num1 = int(input("Enter base number: "))
        num2 = int(input("Enter height number: "))
        print()
        print("1/2","x",num1, "x" ,num2 ,"=", trangle_area(num1,num2))
        print("-----------------------------")
        print()

    elif choice == "9":
        num1 = int(input("Enter the number: "))
        print()
        print(num1, "x" ,num1 ,"=", power_squire(num1))
        print("-----------------------------")
        print()

    elif choice == "10":
        num1 = int(input("Enter the number: "))
        num2 = int(input("Enter the power number: "))
        print()
        print(num1, "^" ,num2 ,"=", power(num1,num2))
        print("-----------------------------")
        print()

    elif choice == '11':
        print()
        print("Thank you for using Akram's calculator.")
        print("-----------------------------")
        break

    else:
        print()
        print("Please enter a numeric value or valid choice.")
        print("-----------------------------")
        print()
