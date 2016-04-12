def average_num(nums):
    totalnums = 0
    counter = float(len(nums))
    for num in nums:
        totalnums += num
    return totalnums/counter


integer_array = [80,19,20,22,100,14,19,22]
result = average_num(integer_array)
print "Counter: ", len(integer_array)
print "Average: ", result
