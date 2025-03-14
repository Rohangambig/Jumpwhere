tuples_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_tuples = sorted(tuples_list, key=lambda x: x[1])
print(sorted_tuples)

dict_list = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 22}, {'name': 'Bob', 'age': 30}]
sorted_dicts = sorted(dict_list, key=lambda x: x['age'])
print(sorted_dicts)
