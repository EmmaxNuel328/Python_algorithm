def insertion_sorting(List):
    length = len(List)
    sorted_list = []
    sorted_list.append(List)
   
    for i in range(length):
        # print("i: ", i)
        for j in range(i + 1, length):
            # print("j: ", j)
            for k in range(j + 1, length):
                # print("k: ", k)
                if List[j][0] < List[i][0]:
                    sorted_list.append([List[j], List[i], List[k]])
                else:
                    sorted_list.append(List)
    if sorted_list[1][2][0] < sorted_list[1][1][0]:
        sorted_list.append([sorted_list[1][0], sorted_list[1][2], sorted_list[1][1]])
    # else:
    #     sorted_list.append(sorted_list[1])
    # print(sorted_list)
    return sorted_list

example = [(3, "apple"), (1, "banana"), (2, "cherry")]
result = insertion_sorting(example)
for list in result:
    print(list)