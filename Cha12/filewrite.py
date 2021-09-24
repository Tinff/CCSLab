fileName = 'new2.txt'

file = open(fileName, "a+")
data = 'creating file\n'
file.write(data) 

d2 = ['1','2','3']
file.writelines(d2)

file.close()