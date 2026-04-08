# # # # # #Even Odd Checker
# # # # # 
# # # # # num = int(input("Please enter a num :"))
# # # # # print(f"\nChecking if {num} is even or odd\n")
# # # # # 
# # # # # if num%2==0:
# # # # #     print(f"The number {num} is a even number")
# # # # # else:
# # # # #     print(f"The number {num} is an odd number")
# # # # # 
# # # # # #Swap Two Numbers
# # # # # print("---------------------------------")    
# # # # # a = 20
# # # # # b = 90
# # # # # 
# # # # # print( a,b)
# # # # # 
# # # # # a =b
# # # # # b=a
# # # # # 
# # # # # print(f"\nSwapped Numbers : {a},{b}")
# # # # # 
# # # # # 
# # # # # #Largest of 3 numbers
# # # # # 
# # # # # 
# # # # a = int(input("Enter 1st Number :"))
# # # # b = int(input("Enter 2nd Number :"))
# # # # c = int(input("Enter 3rd Number :"))
# # # # 
# # # # print("\n Checking...........")
# # # # 
# # # # if a>b and c:
# # # #     print(f"Number {a} is greater than number {b} and {c}")
# # # #     
# # # # elif b>a and c:
# # # #     print(f"Number {b} is greater than number {a} and {c}")
# # # # else:
# # # #     print(f"Number {c} is greater than number {a} and {b}")
# # # 
# # # 
# # # # 
# # # #
# # # print("---------------------------------")    
# # # 
# # # #Simple Intrest Calculator
# # # 
# # # print("Simple Intrest Calculator")
# # # 
# # # pa = int(input("Enter principle amount :"))
# # # i = int(input("Enter rate of intrest(in %):"))
# # # t = int(input("Enter time given (in years) :"))
# # # 
# # # 
# # # res = pa*i*t/100
# # # 
# # # print(f"Your final intrest would be : {res}\n")
# # # 
# # # total = pa+res
# # # 
# # # print("Your final amount would be {total}")
# # 
# # # ------------tempraure converter ----------
# # 
# # temp = int(input("Enter tempreature :"))
# # print(f"\n In which unit you had entered {temp} ?")
# # print("""
# # 
# # 1. Celsius
# # 2. Fahrenheit""")
# # 
# # choose = int(input("Choose a option from 1 and 2 :"))
# # 
# # if choose ==1:
# #     print(f"Converting {temp}°C to Fahrenheit.......")
# #     final = temp*1.8+32
# #     print("Coverted Successfully")
# #     print(f"{temp}°C in Fahrenheit would be {final}°F")
# #     
# # elif choose==2:
# #     print(f"Converting {temp}°F to Celsius.......")
# #     
# #     fah = temp-32/1.8
# #     print("Coverted Successfully")
# #     print(f"{temp}°F in Celsius would be {fah}°C")
# #     
# # else:
# #     print("Please select only from 1 and 2")
# 
# 👉 Positive / Negative / Zero Checker
# # 
# #

num = int(input("Please Enter a num :"))
if num >0:
    print(f"Number {num} is positive")
elif num<0:
    print(f"Number {num} is negative")
    print("Final Number : -",num)
    
else:
    print("This number is zero")