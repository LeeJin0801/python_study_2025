scores = [85, 92, 78, 65, 99, 88]
scores_asc = sorted(scores)

# 원본 리스트를 훼손하지 않고 오름차순 정렬
print(f"original scores : {scores}")
print(f"ascending scores : {scores_asc}")

print(f"78의 개수 : {scores.count(78)}")
print(f"99 in scores : {99 in scores}")

# 80점 이상 점수 리스트
passed_scores = [score for score in scores if score >= 80]
print(f"passed_scores(>= 80) : {passed_scores}")