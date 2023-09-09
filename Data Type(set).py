# 파이썬 프로그래밍의 기초 자료형

# 집합 자료형

# (1) 변수명 = set(요솟값)
print("(1)--------------------")
unordered = set("Hello, hi") 
print(unordered)
# 중복을 허용하지 않고, 순서가 없다. 그러므로 인덱싱을 지원하지 않음.

# (2) 인덱싱을 사용하고 싶을 때
print("(2)--------------------")
oreder = list(unordered)
print(oreder[3])
# 리스트 자료형 혹은 튜플 자료형으로 변환 후에 가능함.

# (3) 교집합, 합집합, 차집합 구하기
print("(3)--------------------")
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
# 교집합
print(s1 & s2, s1.intersection(s2))
# 합집합
print(s1 | s2, s1.union(s2))
# 차집합
print(s1 - s2, s2 - s1, s1.difference(s2), s2.difference(s1))

# (4) 집합 자료형 관련 함수
print("(4)--------------------")
s1 = set([1, 2])
# 값 1개 추가하기
s1.add(3)
print(s1)
# 값 여러개 추가하기
s1.update([3, 4, 5])
print(s1)
# 특정 값 제거하기
s1.remove(2)
print(s1)