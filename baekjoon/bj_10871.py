# 10871 : x보다 작은 수
# N : 리스트 요소 수, x : 조건 (x보다 작은 수)
N, x = map(int, input("").split())
a = []

a.extend(map(int, input("").split()))
del a[N:]
proccessed_a = [num for num in a if num < x]
# num for num in a if num < x 를 바로 출력하려 하니 작동하지 않았다.
print(*proccessed_a)
# Python 리스트에 * 를 사용하면 리스트 압축 해제를 할 수 있게 된다.