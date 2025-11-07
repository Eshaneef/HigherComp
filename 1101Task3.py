items = []
names = []
marks = []
with open("1101Task3/pupils.txt") as readfile:
    line = readfile.readline().rstrip('\n')
    while line:
        items = line.split(",")
        names.append(items[0])
        marks.append(items[1])
        line = readfile.readline().rstrip('\n')
for i in range(len(names)):
    print(f"{names[i]} - {marks[i]}")
