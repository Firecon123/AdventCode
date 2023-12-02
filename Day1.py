def counter(file):
    totalValue = 0
    lineValues =[]
    with open(file) as f:
        for line in f:
            for char in line:
                if(char.isnumeric):
                    lineValues.append(char)
            lineValuesLength = len(lineValues)
            totalValue += int(lineValues[0])
            totalValue += int(lineValues[lineValuesLength - 1])
            lineValues = []
    return totalValue


print(counter("Day1Data"))
print(20)