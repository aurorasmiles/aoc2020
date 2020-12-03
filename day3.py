file = open("day3input.txt").read()
lines = file.split("\n")
row = 0
line = 0
trees1 = 0
for x in lines:
    row = (row + 3) % len(x)

    if (line+1) < len(lines):
        line = line + 1
        print(lines[line])
        if (lines[line])[row] == "#":
            trees1 = trees1 + 1
row = 0
line = 0
trees2 = 0
for x in lines:
    row = (row + 1) % len(x)

    if (line+1) < len(lines):
        line = line + 1
        print(lines[line])
        if (lines[line])[row] == "#":
            trees2 = trees2 + 1
row = 0
line = 0
trees3 = 0
for x in lines:
    row = (row + 5) % len(x)

    if (line+1) < len(lines):
        line = line + 1
        print(lines[line])
        if (lines[line])[row] == "#":
            trees3 = trees3 + 1
row = 0
line = 0
trees4 = 0
for x in lines:
    row = (row + 7) % len(x)

    if (line+1) < len(lines):
        line = line + 1
        print(lines[line])
        if (lines[line])[row] == "#":
            trees4 = trees4 + 1
row = 0
line = 0
trees5 = 0
for x in lines:
    row = (row + 1) % len(x)

    if (line+2) < len(lines):
        line = line + 2
        print(lines[line])
        if (lines[line])[row] == "#":
            trees5 = trees5 + 1
print(trees1)
print(trees2)
print(trees3)
print(trees4)
print(trees5)
print(trees1*trees2*trees3*trees4*trees5)
