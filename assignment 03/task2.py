lst = [3, 6, 9, 3, 30, 15, 9, 45, 36, 12, 12]
dupItems = []
uniqItems = {}
for x in lst:
    if x not in uniqItems:
        uniqItems[x] = 1
else:
    if uniqItems[x] == 1:
        dupItems.append(x)
        uniqItems[x] += 1
print("Duplicates are: ",dupItems)
print("Uniques are: ", uniqItems)