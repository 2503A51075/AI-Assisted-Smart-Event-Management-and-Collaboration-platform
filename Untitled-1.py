def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


repeated_values = remove_duplicates([1, 2, 1, 3, 2])
empty_input = remove_duplicates([])
no_duplicates = remove_duplicates([1, 2, 3])

print(f"Repeated values: {repeated_values}")
print(f"Empty input: {empty_input}")
print(f"No duplicates: {no_duplicates}")