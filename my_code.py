def add(numbers):
    if numbers == "":
        return 0

    string_with_cleared_new_lines = numbers.replace('\n', ",")
    list_of_numbers_as_string = string_with_cleared_new_lines.split(',')
    list_of_numbers_as_numbers = map(int, list_of_numbers_as_string)
    sum_of_list = sum(list_of_numbers_as_numbers)
    return sum_of_list
