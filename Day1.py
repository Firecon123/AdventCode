

def counter(file):
    spelledValues = {"one": "1",
                     "two": "2",
                     "three": "3",
                     "four": "4",
                     "five": "5",
                     "six": "6",
                     "seven": "7",
                     "eight": "8",
                     "nine": "9"}
    totalValue = 0
    numberstring = ""
    lineValues = []
    with open(file) as f:
        for line in f:
            for char in line:
                if char.isnumeric():
                    lineValues.append(char)
                else:
                    numberstring += char.lower()
                    if numberstring in spelledValues:
                        justTheNumber = ""

                        for letter in numberstring:
                            justTheNumber += letter
                            if justTheNumber in spelledValues:                   
                                lineValues.append(spelledValues.get(justTheNumber))
                                numberstring = ""
                                justTheNumber = ""
            lineValuesLength = len(lineValues)
            totalValue += int(lineValues[0]) * 10
            totalValue += int(lineValues[lineValuesLength - 1])
            lineValues.clear()
            numberstring = ""
    return totalValue


# print(counter("Day1Data"))
print(counter("Test"))



#     file = open('Day1Data', 'r')
#     count = 0
#     lines = file.readlines()
#     for line in lines:
#         index1 = None
#         index2 = None
#         for i in range(len(line)):
#             if line[i].isdigit():
#                 index1 = i
#                 break
#         for y in range(len(line) - 1, -1, -1):
#             if line[y].isdigit():
#                 index2 = y
#                 break
#         premier_nombre = int(line[index1])
#         dernier_nombre = int(line[index2])
#         count += (premier_nombre * 10) + dernier_nombre
#         file.close()

# print(counter)

