with open("day1.txt", "r") as f:
    data = f.readlines()

result = 0
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for item in data:
    p = list()
    p += [(item.find(f), numbers.index(f)) for f in numbers if f in item]
    p += [(item.find(str(i)), i) for i in range(0, 10) if str(i) in item]
    p += [(item.rfind(f), numbers.index(f)) for f in numbers if f in item]
    p += [(item.rfind(str(i)), i) for i in range(0, 10) if str(i) in item]
    found = sorted(p)
    result += found[0][1]*10 + found[-1][1]

print(result)