my_list = [1, 2, 3]

my_list.append(4)
print(f"append 후 : {my_list}")

my_list.insert(1, 1.5)
print(f"insert 후 : {my_list}")

another_list = [5, 6]
my_list.extend(another_list)
print(f"extend 후 : {my_list}")

# '+'연산자로 리스트 합치기 (새로운 리스트 생성)
list1 = [1, 2]
list2 = [3, 4]
combined_list = list1 + list2
print(f"'+'연산자로 합친 후 : {combined_list}")