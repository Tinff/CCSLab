fileName = 'new2.txt'

file = open(fileName, "r")
data = file.readlines() 
print(data)


for line in data:
    print(line)



file.close()