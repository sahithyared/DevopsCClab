# Simple Python program to calculate the area of a rectangle

# Function to calculate the area
def calculate_area(length, width):
    return length * width

# Ask the user for the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area using the function
area = calculate_area(length, width)

# Print the area of the rectangle
print(f"The area of the rectangle with length {length} and width {width} is {area}.")
