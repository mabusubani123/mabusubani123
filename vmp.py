'''numbers = [3, 10, 15, 54, 75, 25, 23]

found = False

for num in numbers:
    if num % 3 == 0 or num % 5 == 0 or num % 8 == 0:
        print(num)
        found = True

if not found:
    print("None")'''
    
    
'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

smallest = min(numbers)
largest = max(numbers)

small_index = numbers.index(smallest)
large_index = numbers.index(largest)

numbers[small_index], numbers[large_index] = numbers[large_index], numbers[small_index]

print("Smallest element:", smallest)
print("Largest element:", largest)
print("After swapping:", numbers)'''


'''numbers = [-1, 3, 34, -8, -9, 1]

for i in range(len(numbers)):
    if numbers[i] == -1:
        numbers[i] = 100

print(numbers)'''


'''list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

average1 = sum(list1) / len(list1)
average2 = sum(list2) / len(list2)

print("Average of list 1:", average1)
print("Average of list 2:", average2)'''


'''num = int(input("Enter a number: "))

if num % 3 == 0:
    num = num + 5

print("Result:", num)'''


'''numbers = [3, 10, 15, 54, 75, 25, 23]

for num in numbers:
    if num % 3 == 0 and num % 5 != 0:
        print(num)'''
        
'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

for num in numbers:
    if num > 20:
        print(num)'''
        
        
'''numbers = [-1, 3, 34, -8, -9, 1]

for num in numbers:
    if num < 0:
        print(num)'''
        
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = len(numbers)

print("Count of elements:", count)'''


'''num = int(input("Enter a number: "))

if num % 3 == 0:
    num = num * 5

print("Result:", num'''


'''num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2

if total % 5 == 0:
    print("The sum is divisible by 5")
else:
    print("The sum is not divisible by 5")'''
    
    
'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

for num in numbers:
    if num > 1:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print(num)'''
            
'''numbers = [-1, 3, 34, -8, -9, 1]

print("Original list:", numbers)

# Add an element
numbers.append(10)
print("After append:", numbers)

# Remove an element
numbers.remove(34)
print("After remove:", numbers)

# Sort the list
numbers.sort()
print("After sorting:", numbers)

# Reverse the list
numbers.reverse()
print("After reversing:", numbers)

# Find length
print("Length of list:", len(numbers))'''


'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

average = sum(numbers) / len(numbers)

print("Average:", average)'''

'''num = 1578693
divisors = []

for i in range(1, 11):
    if num % i == 0:
        divisors.append(i)

print("Divisors:", divisors)'''



'''num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 5 == 0:
    num1 = num1 ** 2

if num2 % 5 == 0:
    num2 = num2 ** 2

print("First number:", num1)
print("Second number:", num2)'''

'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

prime = []
even = []
odd = []

for num in numbers:

    # Check prime
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime.append(num)

    # Check even and odd
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Prime numbers:", prime)
print("Even numbers:", even)
print("Odd numbers:", odd)'''


'''numbers = [-1, 3, 34, -8, -9, 1]

result = []

for num in numbers:
    if num >= 0 and num % 3 != 0:
        result.append(num)

print("After removing:", result)'''

'''numbers = [-1, 2, 3, 4, 5, 6, 7, 8, 9]

total = sum(numbers)
count = len(numbers)
average = total / count

print("Sum:", total)
print("Count:", count)
print("Average:", average)'''


'''num = 1578693

for i in range(1, 11):
    if num % i == 0:
        num = num - 100
        print("Divisible by", i, "->", num)'''
        
'''word = "university"
vowels = "aeiou"

count = sum(1 for letter in word if letter in vowels)

print("Number of vowels:", count)'''

'''numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

# Print 89 using its index
print(numbers[12])

# Add 59 at the 9th index
numbers.insert(9, 59)

print(numbers)'''

'''numbers = [-1, 3, 34, -8, -9, 1]

squares = [x ** 2 for x in numbers]

print(squares)'''


'''num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 // num2

print("Floor division:", result)'''

numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89, 7, 8, 54, 621, 57, 24, 3, 5, 6, 4]

unique_values = list(set(numbers))

print("Unique values:", unique_values)                                        