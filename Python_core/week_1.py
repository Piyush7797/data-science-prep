"""#Week 1: Basics – Variables, Data Types, Input/Output, Loops, Conditionals


#Write a Python program to swap two variables

a =  5
b = 10
print("Before swapping: a =", a, "b =", b)
# Swapping
print("After swapping: a =", b, "b =", a)

a ,b = b,a 
print("a = ", a, "b = ", b)

#Q2. Take user input and display it back to the user

num = int(input("Enter the number "))
name =  input("enter your name")

print("the number are ",num)
print("the name is ",name)

#Q3. Write a program to check if a number is even or odd
num =  int(input("enter the number "))

if num % 2 ==0 :
    print(num, " number is even")
else :
    print(num, "number is odd")

#Create a program that prints the multiplication table of a given number.
num = int(input("enterthe number"))
for i in range(1 , 11):
    print(num,"x",i,"=",num*i)"""

######################
"""#Q5. Write a program to find the largest of three numbers.
num1 = int(input("enter num1 :"))
num2 = int(input("enter num2 :"))
num3 = int(input("enter num3 :"))

if  num1 >= num2 and num1 >= num3:
    print(num1,  "is the largest number ")
elif num2 >= num1 and num2 >= num3:
    print(num2 , "is the largest number ")
else:
    print(num3 , "is the largest number")"""


#Q6. Convert temperature from Celsius to Fahrenheit
clesius = float(input("enter the temperature in celsius "))
fahrenheit = (clesius * 9/5) + 32
print(clesius, "degree celsius is equal to ", fahrenheit, "degree fahrenheit")