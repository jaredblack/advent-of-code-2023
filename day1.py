in_file = open('in/day1.txt')
st = in_file.read()
in_file.close()

# part 1
total = 0
for line in st.split('\n'):
    first_digit = None
    last_digit = None
    for c in line:
        if c.isnumeric():
            if first_digit is None:
                first_digit = c
            last_digit = c
    n = int(first_digit + last_digit)
    total += n

print(total)

# part 2
alphadigits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
total = 0
for line in st.split('\n'):
    first_digit = None
    last_digit = None
    for i, c in enumerate(line):
        if c.isnumeric():
            if first_digit is None:
                first_digit = c
            last_digit = c
        else:
            for j, digit in enumerate(alphadigits):
                if line[i:].startswith(digit):
                    if first_digit is None:
                        first_digit = str(j + 1)
                    last_digit = str(j + 1)
    n = int(first_digit + last_digit)
    total += n

print(total)