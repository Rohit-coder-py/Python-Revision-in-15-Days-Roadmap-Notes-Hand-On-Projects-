# -Day 1 Project --
# 
# Project Name : CLI Menu Based Calculator
# 
#

print("Welcome to the calculator")

#Lets design functions first

def sumnum(a,b):
    c = a+b
    print(f"The addition of number {a} and {b} is {c}")
    print(F"Result : {c}\n")
    
def subs(min1,min2):
    fin = min1-min2
    print(f"The subtraction of number {min1} and {min2} is {fin}")
    print(f"Result : {fin}")

def multi(mul1,mul2):
    final = mul1*mul2
    print(f"The multiplication of number {mul1} and {mul2} is {final}")
    print(f"Result : {final}")
    
def div(d1 , d2):
    fi = d1/d2
    print(f"The division of number {d1} and {d2} is {fi}")
    
    
    
def options():
    print('''\n
- - - - - - - - - - - - - - -

1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit

- - - - - - - - - - - - - - -
''')
    
try:
    while True:
        options()
        choose=int(input("Enter your choice:"))
        if choose==1:
            a=int(input("Please Enter 1st Number :"))
            b=int(input("Please enter second number :"))
            print(f"Calculating the sum of {a} and {b}........\n")
            sumnum(a,b)
        elif choose==2:
            min1=int(input("Enter first Number :"))
            min2=int(input("Enter second number :"))
            print(f"Calculating the difference between {min2} and {min1}........\n")
            subs(min1,min2)
        elif choose==3:
            mul1=int(input("Enter first  Number :"))
            mul2=int(input("Enter second number :"))
            print(f"Calculating the multiplication of  {mul1} and {mul2}........\n")
            multi(mul1,mul2)
        elif choose==4:
            try:
                d1=int(input("Enter first number :"))
                d2=int(input("Enter second number :"))
                div(d1,d2)
            except ZeroDivisionError:
                print("Sorry! Zero Division Not Supported")
                print("Please enter any another number ")
        elif choose==5:
            print("Exiting.....")
            print("Wish You A Good Day ")
            break
        else:
            print("Invalid Option Selected ! Please select from 1 to 5 ")
except ValueError:
    print("Please Enter any number from 1 to 5 only")