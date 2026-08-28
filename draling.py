'''def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []  


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))'''




'''stack = []

def push(item):
    stack.append(item)
    print(f"{item} pushed into stack.")

def pop():
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        item = stack.pop()
        print(f"{item} popped from stack.")

def peek():
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        print(f"Top element is: {stack[-1]}")



push(10)
push(20)
push(30)

peek()    

pop()     
peek()     

print("Stack:", stack)'''

'''def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if are_anagrams(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")'''
    
'''# Binary Tree Inorder Traversal
# Inorder: Left -> Root -> Right

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Creating the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Inorder traversal
print("Inorder Traversal:")
inorder(root)'''

'''# Custom Exception
class ThreeDivisionError(Exception):
    pass


try:
    num = int(input("Enter a number: "))

    if num % 3 == 0:
        raise ThreeDivisionError("The number is divisible by 3.")

    print("The number is not divisible by 3.")

except ThreeDivisionError as e:
    print("ThreeDivisionError:", e)'''
    
 
 # Check whether a year is a leap year

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year")
   

    





