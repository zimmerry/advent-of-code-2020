with open("input.txt") as f:
    input = [int(line.rstrip()) for line in f]

# part 1
for i in range(len(input)):
    for j in range(i, len(input)):
        if (input[i] + input[j] == 2020):
            print(input[i] * input[j])

# part 2

for i in range(len(input)):
    for j in range(i, len(input)):
        for k in range(j, len(input)):
            if (input[i] + input[j] + input[k] == 2020):
                print(input[i] * input[j] * input[k])