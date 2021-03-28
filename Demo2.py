#For list start with square bracket[]
values = [1, 2, "LaksmiLavanya", 4, 5]

#List is a datatype that allows multiple values and can be different datatypes

print(values[0])
print(values[3])

#to get the last index of the list
print(values[-1])

#to get substring - starts from 1 to -1
print(values[1:3])

#to insert inbetween list
values.insert(3, "Mantha")
print(values)

#to append
values.append("End")
print(values)

#update the list values
values[3] = "mantha"
print(values)

#deleting the list values
del values[0]
print(values)

#List and Tuple both are same but Tuple is immutable which cannot be chande
#List is [] and Tuple is ()

val = (12, 3, "Saripella", 4.5)
print(val[0])

#val[2] = "saripella"
#print(val)

# Dictionary - key value pair

dic = {"a":2 , 4:"baaddf","3":"Mantha"}
print(dic[4])
print(dic["3"])

#how to create dictionary dynamically at run time

dict = {}

dict["firstname"] = "Lakshmi"
dict["Middlename"] = "Lavanya"
dict["Lastname"] = "Mantha"

print(dict)
print(dict["firstname"])