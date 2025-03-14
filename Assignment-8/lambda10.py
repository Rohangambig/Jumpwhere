mixed_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
sorted_list = sorted(mixed_list, key=lambda x: (isinstance(x, str), x))
print(sorted_list)
