print("Welcome to the grocery store")
Milk=int(input("what is the price of milk"))
Bread=int(input("what is the price of Bread"))
Eggs=int(input("what is the price of Eggs"))
Butter=int(input("what is the price of Butter"))
Chocolate=int(input("what is the price of Chocolate"))
print(Milk+Bread+Eggs+Butter+Chocolate)
#Write a program to calculate the area of the following shapes individually: Triangle, rectangle and square. The length and breadth must be chose by the user.

base=float(input("what is the base of triangle? "))
height=float(input("what is the height of triangle? "))

# Calculate area
area = 0.5 * base * height
print("The area of the triangle is:", area)

# Calculate area of a rectangle

# Ask user for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate area
area = length * width

# Display result
print("The area of the rectangle is:", area)

# Calculate area of a square

# Ask user for the side length
side = float(input("Enter the side length of the square: "))

# Calculate area
area = side * side

# Display result
print("The area of the square is:", area)


