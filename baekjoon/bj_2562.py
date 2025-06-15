a = []
# for i in range(9):
#   a.extend(input("").split(" "))
# extend로 했을 때는 틀렸다.. 왜?

for i in range(9):
    num = int(input())
    a.append(num)

print(max(a))
print(a.index(max(a)) + 1)