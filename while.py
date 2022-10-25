myList = [1,4,6,8,9,2,9,3]
myList.sort()
print("Original list = " + str(myList))

count=0

while True:
    if myList[count] == myList[count+1]:
        print(myList[count])
        break
    else: 
        count = count+1