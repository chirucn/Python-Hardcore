#A-5: Max Number Finder in list
def max_in_list(lst):
    if len(lst)==0:
        return None
    max_num=lst[0]
    for i in range(len(lst)):
        if lst[i]>max_num:
            max_num=lst[i]
    return max_num
print(max_in_list([1,2,3,4,5]))