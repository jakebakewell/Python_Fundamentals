# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(list):
    for i in range(0, len(list), 1):
        if list[i] > 0:
            list[i] = "big"
    return list
print(biggie_size([-1, 3, 5, -5, 6]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
def count_positives(list):
    sum = 0
    for i in range(0, len(list), 1):
        if list[i] > 0:
            sum = sum + 1
    list[len(list) - 1] = sum
    return list
print(count_positives([-1, 1, 1, 1]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
def sum_total(list):
    sum = 0
    for i in range(0, len(list), 1):
        sum = sum + list[i]
    return sum
print(sum_total([1, 2, 3, 4]))

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5
def average(list):
    sum = 0
    for i in range(0, len(list), 1):
        sum = sum + list[i]
    return sum/len(list)
print(average([1, 2, 3, 4]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
def list_length(list):
    length_count = 0
    for i in range(0, len(list), 1):
        length_count = length_count + 1
    return length_count
print(list_length([37, 2, 1, -9, 10]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
def minimum(list):
    if len(list) > 0:
        min = list[0]
        for i in range(0, len(list), 1):
            if list[i] < min:
                min = list[i]
        return min
    else:
        return False

print(minimum([37, 2, 1, -9]))

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
def maximum(list):
    if len(list) > 0:
        max = list[0]
        for i in range(0, len(list), 1):
            if list[i] > max:
                max = list[i]
        return max
    else:
        return False

print(maximum([37, 2, 1, -9]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(list):
    list_stats_dict = {}
    sum_total = 0
    min = list[0]
    max = list[0]
    listLength = len(list)
    for i in range(0, len(list), 1):
        sum_total = sum_total + list[i]
        if list[i] < min:
            min = list[i]
        if list[i] > max:
            max = list[i]
    list_stats_dict['sumTotal'] = sum_total
    list_stats_dict['average'] = sum_total/len(list)
    list_stats_dict['minimum'] = min
    list_stats_dict['maximum'] = max
    list_stats_dict['length'] = len(list)
    return list_stats_dict
print(ultimate_analysis([37, 2, 1, -9]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
import math
def reverse_list(list):
    length = math.floor(len(list)/2)
    for i in range(0, length, 1):
        temp = list[i]
        list[i] = list[len(list) - 1 - i]
        list[len(list) - 1 - i] = temp
    return list
print(reverse_list([37, 2, 1, -9]))