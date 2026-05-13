def insertion_sorting(List):
    length = len(List)
    sorted_list = []
    
   
    for i in range(length):
        j = i - 1
        print("FIRST j: ", j)
        while j >= 0 and List[j][0] > List[j + 1][0]:
            List[j], List[j + 1] = List[j + 1], List[j]
        j -= 1
        print("SECOND j: ", j)
        sorted_list.append(List[:])
    return sorted_list

example = [(3, "apple"), (1, "banana"), (2, "cherry")]
result = insertion_sorting(example)
for list in result:
    print(list)