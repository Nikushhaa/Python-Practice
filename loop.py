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



import math

def solve_quadratic(a, b, c):
    # discriminanti
    d = b**2 - 4*a*c

    # shemowmeba
    if d > 0:
        # fesvebis gamotvla
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)

        print("Two solutions:")
        print("x1 =", x1)
        print("x2 =", x2)

    elif d == 0:
        # d s fesvis gamotvla
        x = -b / (2*a)

        print("One solution:")
        print("x =", x)

    else:
        # tu uaryofitia fesvebi ararsebobs
        print("No real solutions")


a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# gamodzaxeba
solve_quadratic(a, b, c)

