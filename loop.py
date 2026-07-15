# for (let i = 0;i < 100;i++) {
# }

# for i in range(10):
#     if i == 5:
#         break

#     print(f"i={i}")


# start = int(input("Start= "))
# end = int(input("End= "))
    
# for i in range(start,end):
#     if i % 2 == 0:
#         print(f"Luwi= {i}")
#     else:
#         print(f"Kenti= {i}")


# while True:
#     number = int(input("Number: "))
#     if  number % 15 == 0:
#         print(f"FizzBuzz")
#     elif number % 3 == 0:
#         print(f"Fizz")
#     elif  number % 5 == 0:
#             print(f"Buzz")
    
# import math  

# def prime(number):
#     if number <= 1:
#      #tu ricxvi aris 1 ze naklebi an toli arari prime

#         print(f"{number} is not prime")
       
#         return False      
#     for i in range(2, int(math.sqrt(number)) + 1):
#        #tu ricxvs erti gamyofi mainc aqvs is uechveli iqneba kvadratul fesvze patara an naklebi
#         if number % i == 0:
#         #tu ricxvs nashti 0 aqvs eseigi aqvs gamyofi da ar aris martivi
#             print(f"{number} is not prime")
        
#             return False
#             #vasrulebt funqcias
#     print(f"{number} is prime")
# #tu ricxvshi vercerti gamyofi ver moipoveba
#     return True
#     #tu ricxvi martivia
# number = int(input("Number: "))
# prime(number)


#----- prime numbers
# import math

# def unprime(number):
#     if number <= 1:
#         print(f"{number} is not prime")
#         return False

#     for i in range(2, int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             print(f"{number} is not prime")
#             return False

#     print(f"{number} is prime")
#     return True


# number = int(input("Random number = "))
# unprime(number)



# discriminant = lambda a, b, c: b*b - 4*a*c   # D 

# solve = lambda a, b, c: (

#   -b / (2*a) if discriminant(a, b, c) == 0      # 0 tolia anu 1
#     else ((-b - discriminant(a, b, c)**0.5) / (2*a), (-b + discriminant(a, b, c)**0.5) / (2*a))  # dadebiti anu 2 fesvi
# )

# a, b, c = float(input("a: ")), float(input("b: ")), float(input("c: "))   # koeficientebi
# print(solve(a, b, c))   
# import math

# def solve_cubic(a, b, c, d): # funqcia romelsac gadaecema 4 ricxvi
    
#     b, c, d = b/a, c/a, d/a  #koeficienti iyofa a ze

#     p = c - b**2 / 3#vitvlit P s 
#     q = 2*b**3 / 27 - b*c / 3 + d #vitvlit Q s
#     D = (q/2)**2 + (p/3)**3 #vitvlit D s

#     cbrt = lambda x: x**(1/3) if x >= 0 else -((-x)**(1/3)) #kuburi fesvis funqcia

#     if D > 0: #tu D dadebitia
#         x1 = cbrt(-q/2 + D**0.5) + cbrt(-q/2 - D**0.5) - b/3
#         return (round(x1, 6),)
#     elif D == 0: #tu D nulia
#         u = cbrt(-q/2) #vpoulobt kubur fesvs
#         return (round(2*u - b/3, 6), round(-u - b/3, 6))
#     else: #tu D araa dadebiti mashin 3 pasuxi gvaqvs
#         m = 2 * (-p/3)**0.5
#         t = math.acos(3*q / (p*m)) / 3 #acos gveubneba kutxes
#         return (
#             round(m * math.cos(t) - b/3, 6),
#             round(m * math.cos(t + 2*math.pi/3) - b/3, 6),
#             round(m * math.cos(t + 4*math.pi/3) - b/3, 6)
#         )

# print(solve_cubic(
#     float(input("a: ")),
#     float(input("b: ")),
#     float(input("c: ")),
#     float(input("d: "))
# ))
# D diskriminanti
# P gardaqmnili koeficienti
# Q aris meore koeficienti
# cbrt kuburi fesvi

# მომხმარებელი წერს a,b,c,d-ს

# ↓

# კოდი ამარტივებს კუბურ განტოლებას

# ↓

# ითვლის p, q და D-ს

# ↓

# D-ის მიხედვით არჩევს რომელი ფორმულა გამოიყენოს

# ↓

# ითვლის x პასუხებს

# numbers = [15, 8, 22, 4, 1]

# arraymax = numbers[0]

# for i in range(len(numbers)):
#     if numbers[i] > arraymax:
#         arraymax = numbers[i]

# print("Maximum number is: ", arraymax)



# numbers = [15, 8, 22, 4, 1]

# arrayminimum = numbers[0]

# for i in range(len(numbers)):
#     if numbers[i] < arrayminimum:
#         arrayminimum = numbers[i]

# print("Minimum number is:", arrayminimum)

# def find_max(numbers):
#     if len(numbers) == 0:
#         raise IndexError("Array's empty!")
#     arraymax = numbers[0]

#     for i in range(len(numbers)):
#         if numbers[i] > arraymax:
#             arraymax = numbers[i]

#     return arraymax


# numbers = [15, 8, 23, 4, 19]

# print("Maximum number is:", find_max(numbers))


# def find_min(numbers):
#     if len(numbers) == 0:
#         raise IndexError("Array's empty!")
#     arraymin = numbers[0]

#     for i in range(len(numbers)):
#         if numbers[i] < arraymin:
#             arraymin = numbers[i]

#     return arraymin


# numbers = [15, 8, 23, 4, 19]

# print("Minimum number is: ", find_min(numbers))

# from sosogay import find_min, find_max


# def selection_sort(numbers, order):

#     for i in range(len(numbers)):
#         if order == "ascending":
#             index = find_min(numbers[i:]) + i
#         elif order == "descending":
#             index = find_max(numbers[i:]) + i
#         numbers[i], numbers[index] = numbers[index], numbers[i]

#     return numbers


# array = [15, 8, 23, 4, 19]

# print(selection_sort(array, "ascending"))
# print(selection_sort(array, "descending"))


# logical operators = evaluate multiple conditions (or, and, not)
#                                  or = at least one condition must be true
#                                  and = both conditions must be true
#                                  not = inverts the condition (not false, not True)
# temp = 25
# is_raining = False

# if temp > 35 or temp< 0 or is_raining:
#     print("The outdoor event is canceled")
# else:
#     print("The outdoor event is still scheduled")



# temp = -5
# is_sunny = True
# if temp >= 28 and is_sunny:
#     print("It is hot outside!")
#     print("It is sunny outside!")
# elif temp <= 0 and is_sunny:
#     print("It is freezing outside!")
#     print("It is sunny outside!")
# elif temp < 28 and temp > 0 and is_sunny:
#     print("It is warm outside!")
#     print("It is sunny outside!")             
# 
# ---------- conditional expression = a one-line shortcut for the if-else statement (ternary-operator)
#               prunt or assign one of two values based on a condition
#               X if condition else Y

# num = 5
# a = 6
# b = 9
# # print("positive"  if num > 0 else "negative")
# # result = "EVEN" if num % 2 == 0 else "ODD"
# max_num= a if a > b else b
# max_min= a if a < b else b
# status = "Adult" if age >= 18 else "Minor"
# print(status)

#------- string methods
#name = input("Enter your name: ")
# phone_number = input("Enter your phone number: ")
# #result =len(name)  # length of the string
# #result =name.find("N") # find the index of the first occurrence of "N"
# # result = name.rfind("o")
# # name = name.capitalize()  # capitalize the first letter of the string
# #name = name.upper()  # convert the string to uppercase
# #name = name.lower()  # convert the string to lowercase
# # result = name.isdigit()  # check if the string contains only digits
# #result = name.isalpha()  # check if the string contains only alphabetic characters ( if it contains space it will be false any sort of digits too)
# phone_number.count("-", " ")  # count the number of occurrences of "-" in the string
# print(phone_number)

#-------validating user input exercise
#username = input("Enter your name: ")
#username.find(" ")
#username.isalpha()
# if len(username)>12:
#     print("Username is too long")
#elif not username.find(" ") == -1:
#     print("Username contains a space")
#elif not username.isalpha():
#     print("Username contains a number")
# else:
#     print(f"welcome {username}!")    




#--------------- indexing = accessing elements of a sequence using [] indexing operators

#                        [start:stop:step]  start = starting index, stop = stopping index, step = how many steps to move forward
#                        start and step are optional, stop is required
#  credit_number = "1234-5678-9012-3456"
# credit_number = credit_number[::-1]   #reversing the string using slicing
#print(credit_number)  # 6543-2109-8765-4321

#print(credit_number[0])  # 1
#print(credit_number[5])  # 5
# print(credit_number[0:4])  # 1234

# print(credit_number[5:9])
#print(credit_number[5:]) #printing everythingf from index 5 to the end
# using negative indexing will start stepping from the end of the string
#print(credit_number[::2])  #printing every second character in the string
#last_digits = credit_number[-4:] # printing the last 4 digits of the string
# print(f"XXXX-XXXX-XXXX-{last_digits}")  # printing the last 4 digits of the string with X's in front



# format specifiers = {value:flags} format value based on what flags are inserted



# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces for the value (minimum width)
# :< = left align the value within the allocated space
# :> = right align the value within the allocated space
# :^ = center align the value within the allocated space
# :+ = show a plus sign for positive numbers and a minus sign for negative numbers
# : = show a space for positive numbers and a minus sign for negative numbers
# :  = insert a space before positive numbers
# :, = use a comma as a thousands separator


price1 = 3.14159
price2 = -987.65
price3 =  12.34
print(f"price 1 is ${price1:.2f}")
print(f"price 2 is ${price2:.2f}")
print(f"price 3 is ${price3:.2f}")



# print(f"price 1 is ${price1:.1f}")
# print(f"price 2 is ${price2:.1f}")
# print(f"price 3 is ${price3:.1f}")

# print(f"price 1 is ${price1:10}")
# print(f"price 2 is ${price2:10}")
# print(f"price 3 is ${price3:10}")









