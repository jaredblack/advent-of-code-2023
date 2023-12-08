from collections import defaultdict


in_file = open('in/test.txt')
st = in_file.read()
in_file.close()

total = 0
starr = st.splitlines()

def in_bounds(i, j):
    return 0 <= i < len(starr) and 0 <= j < len(starr[0])

# part 1
for i, line in enumerate(starr):
    nstr = ''
    is_model_num = False
    for j, c in enumerate(line):
        if c.isnumeric():
            nstr += c
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if in_bounds(k,l) and not starr[k][l].isnumeric() and starr[k][l] != '.':
                        is_model_num = True
        else:
            if is_model_num and len(nstr) > 0:
                total += int(nstr)
            nstr = ''
            is_model_num = False
    if is_model_num and len(nstr) > 0:
        total += int(nstr)    
        
print(total)
        

# part 2
gears = defaultdict(list)
for i, line in enumerate(starr):
    nstr = ''
    gear_loc = None
    for j, c in enumerate(line):
        if c.isnumeric():
            nstr += c
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if in_bounds(k,l) and starr[k][l] == '*':
                        gear_loc = (k, l)
        else:
            if gear_loc is not None and len(nstr) > 0:
                gears[gear_loc].append(int(nstr))
            nstr = ''
            gear_loc = None
    if gear_loc is not None and len(nstr) > 0:
        gears[gear_loc].append(int(nstr))  
        
total = 0
for gear, nums in gears.items():
    if len(nums) == 2:
        total += nums[0] * nums[1]
print(total)