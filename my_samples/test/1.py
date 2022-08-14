FILENAME = "user.txt"
with open(FILENAME) as file:
    a = file.read()
    lines = a.split("\n")
print(lines)