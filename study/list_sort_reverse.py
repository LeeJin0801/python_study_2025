# 1. 리스트 정렬(sort() vs sorted())
my_numbers = [3, 1, 4, 1,5, 9, 2]
my_numbers.sort() # 원본 리스트가 정렬됨
print(f"sort() 후 : {my_numbers}") # [1, 1, 2, 3, 4, 5, 9]

my_numbers.sort(reverse=True)
print(f"sort(revers=True) 후 : {my_numbers}") # [9, 5, 4, 3, 2, 1, 1]

original_numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(original_numbers)
print(f"sorted() 후 (새 리스트) : {sorted_numbers}") # [1, 1, 3, 4, 5]
print(f"sorted() 후 (원본) : {original_numbers}") # [3, 1, 4, 1, 5]

sorted_desc = sorted(original_numbers, reverse=True)
print(f"sorted(revers=True) 후 : {sorted_desc}") #[5, 4, 3, 1, 1]

my_list = [1, 2, 3, 4, 5]
my_list.reverse() # 리스트 자체를 역순으로 뒤집음
print(f"reverse 후 : {my_list}") # [5, 4, 3, 2, 1]