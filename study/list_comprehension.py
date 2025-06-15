# 예시 1) 1부터 5까지의 숫자로 리스트 만들기
# 일반적인 방법
squares = []
for i in range(1, 6):
  squares.append(i * i)
print(f"일반적인 방법 : {squares}")

# 리스트 컴프리헨션 사용
squares_comp = [i * i for i in range(1, 6)] 
print(f"컴프리헨션 사용 : {squares_comp}")

# 예시 2) 짝수만 골라내서 새로운 리스트 만들기
numbers = [i for i in range(1, 11)]
print(f"numbers : {numbers}")
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"짝수만 : {even_numbers}")

# 예시 3) 문자열 리스트에서 길이가 3 이상인 단어만 대문자로 바꾸기
words = ["apple", "cat", "banana", "dog", "ho"]
processed_words = [word.upper() for word in words if len(word) >= 3]
print(f"처리된 단어 : {processed_words}")

# 예시 4) 2차원 리스트 만들기 (중첩 for문)
# 3 x 3 크기의 0으로 채워진 2차원 리스트
matrix = [[0 for col in range(3)] for row in range(3)]
print(f"2차원 리스트 : {matrix}")