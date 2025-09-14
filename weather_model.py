# Temperature Modeling Function
def Temperature_modeling(a, b, c, time):
    return a * time**2 + b * time + c

#  Version 1: Hardcoded
a, b, c, time = 1, 5, 3, 3
temp = Temperature_modeling(a, b, c, time)
print(f"[V1] Temp at time {time} = {temp}")

# Version 2: Keyboard Input
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
time = int(input("Enter time: "))
temp = Temperature_modeling(a, b, c, time)
print(f"[V2] Temp at time {time} = {temp}")

#  Version 3: Read from Single-Line File
with open("sheet_Single.txt", "w") as f:
    f.write("2.5 3.0 1.5 4")
with open("sheet_Single.txt", "r") as f:
    a, b, c, time = map(float, f.readline().split())
    time = int(time)
temp = Temperature_modeling(a, b, c, time)
print(f"[V3] Temp at time {time} = {temp}")

# Version 4: Read from Multi-Line File
with open("sheet_Multiple.txt", "w") as f:
    f.write("1 2 3 1\n2 3 1 2\n")
print("[V4] Temperatures from file:")
for line in open("sheet_Multiple.txt"):
    a, b, c, time = map(float, line.split())
    time = int(time)
    temp = Temperature_modeling(a, b, c, time)
    print(f"  Time {time} → Temp = {temp}")
