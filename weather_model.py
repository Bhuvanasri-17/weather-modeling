import math

def quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        return f"Two Real Roots: {r1:.2f}, {r2:.2f}"
    elif d == 0:
        r = -b / (2*a)
        return f"One Real Root: {r:.2f}"
    else:
        return "No Real Roots"

# Stage 1: Hardcoded
print("Stage 1 - Hardcoded:")
print(quadratic(1, -5, 6))

# Stage 2: Keyboard input
print("\nStage 2 - User Input:")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
print(quadratic(a, b, c))

# Stage 3 & 4: Read from file
print("\nStage 3 & 4 - File Input:")
try:
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            a, b, c = map(float, line.strip().split())
            print(f"Line {i+1}: {quadratic(a, b, c)}")
except FileNotFoundError:
    print("input.txt file not found. Please create it in the same folder.")
