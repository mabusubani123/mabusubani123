'''num = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
largest = 0
for i in num:
    if i > largest:
        largest = i
print("largest = ", largest)'''

'''a = int(intput("enter the num"))
b = int(input("enter the num"))
op = input("enter the operator")

if op =='+':
    print("sum",a+b)
if op == '_': 
    print("sub", a-b)

if op =="*":
    print("prod",a *b)
if op =='/':
 print("div", a/b)'''

'''def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n %i == 0:
            return False
        else:
         return False
num = int (input("enter the numb"))
if is_prime(num):
    
 print("prime")
else:
 print("not prime")''' 
 
'''# Create a list of numbers
numbers = [45, 12, 89, 3, 56, 23, 7]

# Find the minimum number using the built-in min() function
min_number = min(numbers)

# Display the results
print(f"The list of numbers is: {numbers}")
print(f"The minimum number is: {min_number}")'''

'''my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

count = 0
for item in my_list:
    count += 1

print(f"The total count of elements is: {count}")'''

'''my_list = [15, -8, 22, -4, 10, 5, -12, 30, -3, 7]

# Initialize sum to 0
total_sum = 0

# Loop through each element and add it to the total
for item in my_list:
    total_sum += item

print(f"The sum of the list is: {total_sum}")'''

'''# --- STACK OPERATIONS (LIFO: Last In, First Out) ---
stack = []

stack.append(10)  # Push 10
stack.append(20)  # Push 20
print("Stack after pushes:", stack)

popped_item = stack.pop()  # Removes the last element (20)
print("Popped from stack:", popped_item)


# --- QUEUE OPERATIONS (FIFO: First In, First Out) ---
queue = []

queue.append(10)  # Enqueue 10
queue.append(20)  # Enqueue 20
print("Queue after enqueues:", queue)

dequeued_item = queue.pop(0)  # Removes the first element (10)
print("Dequeued from queue:", dequeued_item)'''


'''numbers = [10, 25, 30, 15, 5, 35]
target = 40 
found = False
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"Match found: {numbers[i]} + {numbers[j]} = {target}")
            found = True
            break
    if found:
        break

if not found:
    print("No two numbers match the target sum.")'''
    
    
'''class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("Preorder:  ", end="")
preorder(root)   

print("\nInorder:   ", end="")
inorder(root)    

print("\nPostorder: ", end="")
postorder(root)'''

'''def is_palindrome(s):
    
    s = s.replace(" ", "").lower()
    return s == s[::-1]

word = "Madam"
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")'''
    
try:
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b)
    else:
        print("Invalid operator")

except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
   

