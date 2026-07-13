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
temp = 25
is_raining = False

if temp > 35 or temp< 0 or is_raining:
    print("The outdoor event is canceled")
else:
    print("The outdoor event is still scheduled")
                