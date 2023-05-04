"""
ID: konmarc1
LANG: PYTHON3
TASK: ride
"""
# read from input
with open ('ride.in', 'r') as f:
    comet_name = f.readline()[:-1]
    group_name = f.readline()[:-1]

# convert letters to numbers, calculate product
comet_product = 1
for char in comet_name:
    comet_product *= ord(char) - 64

group_product = 1
for char in group_name:
    group_product *= ord(char) - 64

# calculate mod 47, compare & write to output
fout = open('ride.out', 'w')

if comet_product % 47 == group_product % 47:
    fout.write("GO\n")
else:
    fout.write("STAY\n")
