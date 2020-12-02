file = open("day2input.txt").read()
lines = file.split("\n")
valid = 0
valid2 = 0
for x in lines:
    l = x.split(" ")
    minval = int(l[0].split("-")[0])
    maxval = int(l[0].split("-")[1])
    char = l[1].replace(":", "")
    pw = l[2]
    count = pw.count(char)
    if count >= minval and count <= maxval:
        valid = valid + 1
    if (pw[minval-1] == char) ^ (pw[maxval-1] == char):
        valid2 = valid2 + 1
print("Part 1:")
print(valid)
print("Part 2:")
print(valid2)
