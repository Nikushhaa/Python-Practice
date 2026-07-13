# x1 = float(input("x1= "))
# y1 = float(input("y1= "))
# x2 = float(input("x2= "))
# y2 = float(input("y2= "))

# result = ((x2-x1)**2 + (y2-y1)**2) ** 0.5




def find_min(numbers):
    min_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[min_index]:
            min_index = i

    return min_index


array = [15, 8, 23, 4, 19]

index = find_min(array)

print("Index:", index)
print("Value:", array[index])



def find_max(numbers):
    max_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[max_index]:
            max_index = i

    return max_index


array = [15, 8, 23, 4, 19]

index = find_max(array)

print("Index:", index)
print("Value:", array[index])