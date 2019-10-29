def min_max_difference(numbers_array):
    min=numbers_array[0]
    max=numbers_array[0]
    difference=0

    for num in numbers_array:
        if num<min:
            min=num
        if num>max:
            max=num

    difference = max-min
    return difference



