#Week 1: Basics – Variables, Data Types, Input/Output, Loops, Conditionals


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
    print(num,"x",i,"=",num*i)