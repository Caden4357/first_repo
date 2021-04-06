#1)Given a list, write a function that changes all positive numbers in the list to "big
def make_it_big(list):
    for i in range(len(list)):
        if list[i] >= 0:
            list[i] = "make it big"
    return(list)
print(make_it_big([5,4,0,-4,-3,-3,-66]))
#2)Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number)
def count_positives(list):
    total = 0
    new_list = []
    for i in range(len(list)):
        new_list.append(list[i])
        if list[i] > 0:
            total = total + 1
    new_list[len(new_list)-1] = total
    return new_list
print(count_positives([-2,-1,0,6,66,-5,7]))
#3)Create a function that takes a list and returns the sum of all the values in the array.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 
def sum_total(list):
    total = 0
    for i in range(len(list)):
        total = total + list[i]
    return total
print(sum_total([5,4,3,2,1]))
#4)Create a function that takes a list and returns the average of all the values.
#Example: average([1,2,3,4]) should return 2.5
def sum_average(list):
    total = 0
    for i in range(len(list)):
        total = total + list[i]
    return total / float(len(list))
print(sum_total([5,4,3,2,1,4]))
#5)Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0
def length(list):
    return len(list)
print(length([]))
#6)Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False
def minimum_value(list):
    minimum = None
    if len(list) == 0:
        return False
    for i in range(len(list)):
        if list[i] < minimum:
            minimum = list[i]
    return minimum
print(minimum_value([]))
#7)Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False
def maximum_value(list):
    maximum = None
    if len(list) == 0:
        return False
    for i in range(len(list)):
        if list[i] > maximum:
            maximum = list[i]
    return maximum
print(maximum_value([-9,-10,-12,-200,-2,-1]))
#Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(list):
    sum = sum_total(list)
    avg = sum_average(list)
    min = minimum_value(list)
    max = maximum_value(list)
    len = length(list)
    new_dict = {
        "sumTotal": sum,
        "average": avg,
        "minimum": min,
        "maximum": max,
        "length": len,
    }
    return new_dict
print(ultimate_analysis([37,2,1,-9]))
#Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(list):
    list.reverse()
    return list
print(reverse_list([5,4,3,6,77,5,4,8]))
