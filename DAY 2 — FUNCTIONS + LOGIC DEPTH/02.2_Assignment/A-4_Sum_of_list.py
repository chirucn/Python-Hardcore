#A-4: Sum of list
def sum_list(lst):
    total_sum=0
    for i in range(len(lst)):
        total_sum+=lst[i]
    return total_sum
print(sum_list([1,2,3,4,5]))