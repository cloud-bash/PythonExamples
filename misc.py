list1 = ["a", "b", "c", "d"]
list2 = ["1", "2", "3", "4"]
list3 = ["w", "x", "y", "z"]
d = {}


def addListsToDict(dictionary, lists):
    # for each value in each list, add the value at each index
    i = 0
    while i < len(lists[0]):
        valueList = []
        for list in lists:
            valueList.append(list[i])
        for value in valueList:
            dictionary[value] = valueList
        i += 1
    # for l in lists:
    #     valueList = []
    #     for element in l:
    #         valueList.append(element)
    #     for value in valueList:
    #         dictionary[str(value)] = valueList


addListsToDict(d, [list1, list2, list3])
print(d)
