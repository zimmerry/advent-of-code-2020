with open("input.txt") as f:
    input = [line.rstrip() for line in f]

valid = 0

for i in range(len(input)):
    check_char = ''
    occurrences = 0

    if(input[i][0].isdigit() and input[i][1].isdigit):
        min = input[i][0] + input[i][2]
    else
        min = input[i][0]

    for j in range(len(input[i])):
        if(input[i][j].isalpha()):
            check_char = input[i][j]
            for k in range(j + 1, len(input[i])):
                if(input[i][k] == check_char):
                    occurrences += 1
            continue
    if occurrences > 0:
        valid += 1

print(valid)