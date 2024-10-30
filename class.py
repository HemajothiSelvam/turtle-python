
my_list = [1, 2]
contains_nested_list = False

for item in my_list:
    if isinstance(item, list):
        contains_nested_list = True
        break

if contains_nested_list:
    print("The list contains a nested list")
else:
    print("The list does not contain a nested list")
