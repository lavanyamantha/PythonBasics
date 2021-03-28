greeting = "Good Morning"
a = 4

#if greeting == "Good Morning":
if a > 2:
    print("condition matches")

else:
    print("condition do not match")

print("if else code condition is ended")

#for loop

obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)

#Sum of First Natural Number 1+2+3+4+5
#range(i,j) -> i to j-1
summation = 0
for j in range(1, 6): #for(i=0;i<5;i++)
    summation = summation + j
print(summation)

print("****************************************************")
# passing index
for k in range(1, 10, 5):
    print(k)
print("****Skipping first index***")
for m in range(10): # n = n-1
    print(m)




