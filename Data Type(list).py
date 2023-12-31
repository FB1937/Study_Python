# 파이썬 프로그래밍의 기초 자료형

# 리스트 자료형(요솟값의 생성, 삭제 , 수정이 가능함.)

# (1) 리스트명 = [요소1, 요소2, 요소3, 요소4]
print("(1)--------------------")
a = []
b = [1,2, ['life', 'is']] # 리스트 안에는 어떤 자료형도 포함할 수 있다.
print(a, b)

# (2) 리스트의 인덱싱과 슬라이싱
print("(2)--------------------")
a = [1, 2, ['x', 'y', 'z']] 
print(a[-1], a[2][1]) # 인덱싱
print(a[0:2], a[2][1:3]) # 슬라이싱

# (3) 리스트의 연산
print("(3)--------------------")
a = [2,7]
b = ['I', 'am', 'nice']
print(a + b, a * 2, len(b)) # 더하기, 반복하기, 길이 구하기

# (4) 리스트의 수정과 삭제
print("(4)--------------------")
a = [1, 2, 3, 4] # 수정
print('Before = ', a)
a[1] = 10
del a[2:] # 삭제
print('after = ', a)

# (5) 리스트 관련 함수
print("(5)--------------------")
a = [2, 5, 1]
# 리스트의 맨 마지막에 추가함
a.append(0)
# 리스트의 요소를 순서대로 정렬함. 알파벳도 가능.
a.sort()
print(a)
# 현재의 리스트를 거꾸로 뒤집는다.
a.reverse()
# 3번째 위치에 D를 삽입한다.
a.insert(3, 'D')
# 리스트에 5가 있으면 위칫값을 리턴한다.
print(a, a.index(5))
# 리시트를 추가한다.
a.extend([3,1])
# 리스트에 포함된 1의 갯수를 센다.
print(a, a.count(1))