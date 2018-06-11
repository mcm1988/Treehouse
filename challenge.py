items = ["apple", 5.2, "dog", 8]


def combiner(items):
    list_of_numbers = []
    combined_string = ""
    combined_numbers = 0
    for item in items:
        if isinstance(item, (int, float)):
            list_of_numbers.append(item)
        if isinstance(item, (str, list, dict)):
            combined_string += item
    for number in list_of_numbers:
        combined_numbers += number
    return combined_string + str(combined_numbers)


print(combiner(items))
