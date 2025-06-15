my_list = ['a', 'b', 'c', 'b', 'd']

my_list.remove('b')
print(f"remove 후 : {my_list}")

popped_item = my_list.pop(2)
print(f"pop 후 : {my_list}, 제거된 항목: {popped_item}")

del my_list[0]
print(f"del 후 : {my_list}")

my_list_2 = [1, 2, 3, 4, 5]
del my_list_2[1:4]
print (f"clear 후: {my_list_2}")

my_list_3 = [10, 20, 30]
my_list_3.clear()
print(f"clear 후 : {my_list_3}")