# 1. list in keyword
fruits = ["apple", "banana", "cherry"]
print(f"'apple'이 리스트에 있나요? {'apple' in fruits}") # True
print(f"'grape'가 리스트에 있나요? {'grape' in fruits}") # False

# 2. list.count(x)
data = [1, 2, 2, 3, 2, 4]
print(f"2의 개수 : {data.count(2)}") # 3
print(f"5의 개수 : {data.count(5)}") # 0

# 3. list.inded(x)
data = ['a', 'b', 'c','b', 'd', 'b']
print(f"'b'의 첫 번쨰 인덱스 : {data.index('b')}") # 1
# print(data.index('e')) ValueError : 'e' is not in list