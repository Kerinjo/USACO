fin = open("gift1.in", "r")

n = int(fin.readline())
friends = {}
for i in range(n):
    friends[(fin.readline()[:-1])] = 0

print(friends)

line = fin.readline()[:-1]
while line:
    who = line
    print(f"Who? {who}")

    how_much, how_many = fin.readline()[:-1].split(" ")
    how_much = int(how_much)
    how_many = int(how_many)
    print(f"How much? {how_much}. To how many? {how_many}")

    receivers = []
    for i in range(how_many):
        receivers.append(fin.readline()[:-1])

    print(f"To who? {receivers}")

    line = fin.readline()[:-1]
