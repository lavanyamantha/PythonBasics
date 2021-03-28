it = 10

#while loops are used to check the condition
#break keyword is used to halt the while loop abruptly
#continue keyword is to stop the current iteration and proceed to nex iteration
while it>1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1

print("while loop execution is done")