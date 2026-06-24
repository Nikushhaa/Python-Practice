
a = abs(float(input("a= ")))
b = abs(float(input("b= ")))
c = abs(float(input("c= ")))

if a + b <= c or a + c <= b or b + c <= a:
    print("Error: This triangle doesn't exist")
else:
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**(0.5)

    print("Area:", s)