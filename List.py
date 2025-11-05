print("U have no idea about Lists")
# =========================================
# 🌟 PYTHON LISTS - COMPLETE GUIDE (with outputs)
# =========================================

# 1️⃣ Creating Lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [10, "hello", 3.14, True]

print("Fruits:", fruits)       # Fruits: ['apple', 'banana', 'cherry']
print("Numbers:", numbers)     # Numbers: [1, 2, 3, 4, 5]
print("Mixed:", mixed)         # Mixed: [10, 'hello', 3.14, True]
print()

# 2️⃣ Accessing List Elements (Indexing)
print("First fruit:", fruits[0])       # First fruit: apple
print("Last fruit:", fruits[-1])       # Last fruit: cherry
print()

# 3️⃣ Modifying Lists
fruits[1] = "blueberry"
print("Modified fruits:", fruits)      # Modified fruits: ['apple', 'blueberry', 'cherry']
print()

# 4️⃣ Adding Elements
fruits.append("mango")        # Add to end
fruits.insert(1, "orange")    # Insert at index 1
print("After adding:", fruits)   # After adding: ['apple', 'orange', 'blueberry', 'cherry', 'mango']
print()

# 5️⃣ Removing Elements
fruits.remove("orange")       # Remove by value
popped_item = fruits.pop()    # Removes last item ("mango")
print("After removing:", fruits)     # After removing: ['apple', 'blueberry', 'cherry']
print("Popped item:", popped_item)   # Popped item: mango
print()

# 6️⃣ List Slicing
numbers = [10, 20, 30, 40, 50, 60, 70]
print("Slice [1:4]:", numbers[1:4])      # Slice [1:4]: [20, 30, 40]
print("Slice [:3]:", numbers[:3])        # Slice [:3]: [10, 20, 30]
print("Slice [::2]:", numbers[::2])      # Slice [::2]: [10, 30, 50, 70]
print()

# 7️⃣ Looping Through Lists
for fruit in fruits:
    print("I like", fruit)
# Output:
# I like apple
# I like blueberry
# I like cherry
print()

# 8️⃣ Checking Membership
if "apple" in fruits:
    print("Apple is in the list!")   # Apple is in the list!
print()

# 9️⃣ Getting List Length
print("Length of fruits list:", len(fruits))   # Length of fruits list: 3
print()

# 🔟 Combining Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Combined list:", combined)     # Combined list: [1, 2, 3, 4, 5, 6]
print()

# 11️⃣ List Comprehensions
squares = [x**2 for x in range(1, 6)]
even_numbers = [x for x in range(10) if x % 2 == 0]
print("Squares:", squares)            # Squares: [1, 4, 9, 16, 25]
print("Even numbers:", even_numbers)  # Even numbers: [0, 2, 4, 6, 8]
print()

# 12️⃣ Built-in List Functions
nums = [5, 2, 9, 1, 5, 6]
print("Original nums:", nums)         # Original nums: [5, 2, 9, 1, 5, 6]
print("Max:", max(nums))              # Max: 9
print("Min:", min(nums))              # Min: 1
print("Sum:", sum(nums))              # Sum: 28
nums.sort()
print("Sorted:", nums)                # Sorted: [1, 2, 5, 5, 6, 9]
nums.reverse()
print("Reversed:", nums)              # Reversed: [9, 6, 5, 5, 2, 1]
print()

# 13️⃣ Copying Lists
a = [1, 2, 3]
b = a.copy()     # Creates a separate copy
b.append(4)
print("a:", a)   # a: [1, 2, 3]
print("b:", b)   # b: [1, 2, 3, 4]
print()

# 14️⃣ Nested Lists (Lists inside lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:", matrix)
# Matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Accessing element [1][2]:", matrix[1][2])  # Accessing element [1][2]: 6
print()

# 15️⃣ Clearing a List
numbers.clear()
print("Cleared list:", numbers)       # Cleared list: []
print()

# 🎯 Bonus: Using *list()* Constructor
new_list = list(("Python", "is", "fun"))
print("Created using list() constructor:", new_list)
# Created using list() constructor: ['Python', 'is', 'fun']
print()

# =========================================
# ✅ END OF LIST TUTORIAL
# =========================================
