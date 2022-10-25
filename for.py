myList = [1,4,6,8,6,2,9,3]
myList.sort()
print("Original list = " + str(myList))\

for i in range(len(myList)):
    if myList[i] == myList[i+1]:
        print(myList[i])
        break

