my_list = ['a', 'b', 'c', 'd', 'e']

# 양수 인덱싱(0부터 시작)
print(f"첫 번째 요소 : {my_list[0]}")
print(f"세 번째 요소 : {my_list[2]}")

# 음수 인덱싱(뒤에서부터 시작, -1이 마지막 요소)
print(f"마지막 요소 : {my_list[-1]}")
print(f"뒤에서 두 번째 요소 : {my_list[-2]}")

# 주의 : 인덱스 범위를 벗어나면 IndedError 발생
#print(my_list[5])