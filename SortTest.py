newList = ["$4.50", "$900.00", "$8,000.00", "$2.65"]
newList2 = []
newList4 = []
newList3 = []

for i in range(len(newList)):
    i1 = newList.pop()
    i1 = i1.replace('$', '')
    newList2.append(i1)
    sortedList = sorted(newList2, key=len)

print(sortedList)
sortedList.reverse()


for i in range(len(sortedList)):
    i2 = sortedList.pop()
    newList3.append("$" + i2)

#sortedList = sorted(newList2, key=len)
print(newList)

print(newList3)