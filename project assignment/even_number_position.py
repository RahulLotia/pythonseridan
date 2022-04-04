def get_index(list):
    res = []
    for idx, ele in enumerate(list):
        if ele % 2 == 0:
            res.append(idx)
    print("The original list is : " + str(list)+ '\n')
    print("index of even numbers : " + str(res)+ '\n')

