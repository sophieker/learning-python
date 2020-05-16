array = []
length = int(input('how long do you want your list to be? '))
for counter in range(0, length):
    hi = int(input('enter a number here: '))
    array.append(hi)
sordid = []
for counter in range(0, len(array)):
    mini = array[0]
    for counter in range(0,len(array)):
        if mini > array[counter]:
            mini = array[counter]

    array.remove(mini)
    sordid.append(mini)

print(array)
print(sordid)
