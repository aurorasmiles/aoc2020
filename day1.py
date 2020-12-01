file = open("day1input.txt").read()
numbers = file.split('\n')
print("First part:")
for x in numbers:
    for y in numbers:
        if int(x) + int(y) == 2020:
            print("First Number: " + x)
            print("Second Number: " + y)
            print(int(x) * int(y))
            break
            break

print("Second part:")
for x in numbers:
    for y in numbers:
        for z in numbers:
            if int(x) + int(y) + int(z) == 2020:
                print("First Number: " + x)
                print("Second Number: " + y)
                print("Third Number: " + z)
                print(int(x)*int(y)*int(z))
                break

