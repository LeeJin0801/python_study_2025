data = [10, 20, 30, 40, 50]
print(f"data 리스트 : {data}")
print(f"30 출력 : {data[2]}")
print(f"슬라이싱 : {data[1:4]}")

print(f"append 전 : {data}")
data.append(60)
print(f"append 후 : {data}")

print(f"insert 전 : {data}")
data.insert(0, 5)
print(f"insert 후 : {data}")

popped_item = data.pop(-1)
print(f"제거된 요소 : {popped_item}")

print(f"20 제거하기 전 : {data}")
del data[2]
print(f"제거 후 : {data}")