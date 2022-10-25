myList = [1,4,6,8,3,2,9,3]
myList.sort()
print("Original list = " + str(myList))

myNewList = set(myList)
myNewList = list(myNewList)
print("New list = " + str(myNewList))

for i in range(len(myNewList)):
    if myList[i] != myNewList[i]:
        print(myList[i])
        break