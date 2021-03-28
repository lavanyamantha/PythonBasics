#first open the file with open

file = open('test.txt')
#Read all the contents of the file
#print(file.read())
#Read n numeber of characters by passing parameter
#print(file.read(5))

#to read one single line at a time
#print(file.readline())
#print(file.readline())

#print line by line using readLine method
#line = file.readline()
#while line!= "":
 #   print(line)
  #  line = file.readline()

values = ["abc", "bell", "cvasdjf", "ddkdjl", "ekaljdlsdd", "fdfadfa"]
for values in file.readlines():
    print(values)



file.close()