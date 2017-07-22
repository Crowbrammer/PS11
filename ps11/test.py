
def createNode(name):
    pass
with open("mit_map.txt") as f:
    for line in f:
        splitLine = line.split(" ")
        for each in splitLine:
            print(each)

# Use this idea for creating log decorators
