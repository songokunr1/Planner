def sum_numbers_from_string(string):
    numbers = []
    for each_character in string:
        if each_character.isdigit():
            numbers.append(int(each_character))
    total = 0
    for each_number in numbers:
        total=total+each_number

    return total