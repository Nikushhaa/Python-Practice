#for i in range(200000):
 #   print("Yo wassup")



# strings 
#first_name = "Nika"
#last_name = "Idunno"
#email = "bro123@fake.com"
#print(first_name)
#print(last_name)
#print(f"your email is: {email}")


#-----
#integers
#age = 19
#print(f"your age is: {age}")
#quantity = 3
#print(f"you have {quantity} items in your cart")
#num_of_students = 30
#print(f"there are {num_of_students} students in the class")
#----

#floats
#price = 19.99
#gpa = 3.2
#print(f"the price of the item is: ${price}")
#print(f"your gpa is: {gpa}")
#distance = 5.5
#print(f"the distance to the destination is: {distance} kilometers")
#------


#booleans

#is_student = True
#print(f"are you a student?: {is_student}")
#if is_student:
#    print("you are a student")
#else:
#    print("you are not a student")

#for_sale = True
#if for_sale:
#    print("the item is for sale")
#else:
#    print("the item is not for sale")

#is_online = False
#if is_online:
#    print("the player is online")
#else:   
#    print("the player is offline")
#------

    #typecasting
   # name = "Nika"
    #age = 19
   # gpa = 3.2
    #is_student = True
    
    #gpa = int(gpa)
    #print(gpa)

    #age = float(age)
    #print(age)

    #age = str(age)
    #print(type(age))
#------

    #input() a function that allows you to get user input from the console
#name = input("what is your name? ")
#print(f"hello {name}, nice to meet you!")
#print("happy birthday to you!")
#age = input("what is your age? ")
#age = int(age)
#age = age + 1
#print(f"you are {age} years old")



#------
#Exercise 1 rectangle area calc
#length = input("what is the length of the rectangle? ")
#width = input("what is the width of the rectangle? ")
#area = float(length) * float(width)
#print(f"the area of the rectangle is: {area}cm")

#------
#Exercise 2: Shopping cart program

#item = input("what item would you like to buy? ")
#price = input(f"what is the price of {item}?")
#quantity = input(f"how many {item}s would you like to buy? ")
#total = float(price) * float(quantity)
#print(f"the total cost of {quantity} {item}s is: ${total}")
#print(f"you have bought {quantity} x {item}/s")
#print (f"the total cost is: ${total}")


#-------
#madlibs game
#word game where you create a story
#by filling in blanks with different types of words (nouns, verbs, adjectives, etc.)

#adjective1 = input("enter an adjective: (description) ")
#noun1 = input("enter a noun: (person, place, or thing) ")
#adjective2 = input("enter another adjective: (description) ")
#verb1 = input("enter a verb ending with 'ing' (action) ")
#adjective3 = input("enter a third adjective: (description) ")

#print(f"today i went to {adjective1} zoo.")
#print(f"In an exhibit, i saw a {noun1}")
#print(f"{noun1} was {adjective2} and {verb1}")
#print(f"I was {adjective3}!")
#------


#friends = 10
#friends = friends + 1 same is down below
#friends = friends -2
#friends += 1
#friends = friends * 3
# friends /= 2
#friends = friends / 2
#friends = friends ** 2
#friends **= 2
#remainder = friends % 3 


#print(remainder)


#x = 3.14
#y = -4
#z = 5
#result = round(x)
#result = abs(y) mteli an moduli
#result = pow(4,3) 4x4x4
#result = max(x,y,z)
#result = min(x,y,z)

#print(result)





#import math 

#x = 9

#print(math.pi)
#print(math.e)
#result = math.sqrt()
#result = math.ceil(x)
#result = math.floor(x)
#print(result)



#import math
#radius = float(input('Enter the radius of a circle'))

#circumference = 2 * math.pi * radius

#print(f"The circumference is: {round(circumference,2)}cm")


#import math

#radius = float(input("Enter the radius of a circle:"))

#area = math.pi  * pow(radius,2)

#print(f"The area of this circle is: {round(area, 2)}cm^2")


#import math 

#a = float(input("Enter side A:"))
#b = float(input("Enter side B:"))
#c = math.sqrt(pow(a,2)+ pow(b,2))
#print(f"Side C = {c}")


# if = Do some code only IF some conditions is true
# Else do something else
#---- age example

#age = int(input("Enter your age:  "))

#if age >= 100:
    #  print("You are too old to sign up!")   
#elif age < 0:
   # print("You haven't been born yet!?")
#elif age >= 18:
  # print("You are now signed up!")
#else: 
 #   print("You must be 18+ to sign up!")    
#-----

#--- 2rd food example
#response = input("Would you like food?: (Y/N):")

#if response == "Y":
  #  print("Have some food!")
#else:
 #   print("No food for you!")



#----3rd example
#name = input("Enter your name:")

#if name == "":
 #   print("You didn't type in your name!")
#else:
  #  print(f"hello {name}")


#----4rd

#online = True

#if online:
 #   print("The user is online")
#else:
 #   print("The user is offline")


#Python calculator

#operator = input("Enter an operator (+ - * / ): ")
#num1 = float(input("Enter the first number: "))  # aq sachiroa float
#num2 = float(input("Enter the second number: "))
#print(num1 + num2) That's the first printing 


#if operator == "+":
 #result = num1 + num2
 #print(round(result))   
#elif operator == "-":
#  result = num1 - num2
#  print(round(result))
#elif operator == "*":
#  result = num1 * num2
#  print(round(result))
#elif operator == "/":
#  result = num1 / num2
#  print(round(result))

#else:
 # print(f"{operator} is not a valid operator! ")



 
#Python weight converter program

#weight = float(input ("Enter your weight: "))
#unit = input ("kilograms or pounds? (K or L):  ")

#if unit == "K":
   # weight = weight * 2.205
  #  unit = "Lbs."
 #elif unit == "L":
    #weight = weight / 2.205
   # unit = "kgs"
  #  print(f"Your weight is: {round(weight, 1)} {unit}")
#else:
    #print(f"{unit} was not valid")
#-----
































