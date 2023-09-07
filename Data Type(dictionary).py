# 파이썬 프로그래밍의 기초 자료형

# 딕셔너리 자료형

# (1) 딕셔너리명 = {'key1' : 'value1', 'key2' : 'value2'. 'key3' : 'value3'}
print("(1)--------------------")
game = {'name' : 'starcraft', 'price' : 3000, 'tribe' : ['terran', 'zerg', 'protosss' ]}
print(game)

# (2) 쌍 추가, 삭제하기
print("(2)--------------------")
dic = {1 : 'a'}
dic[2] = 'b'
print(dic)
del dic[1]
print(dic)

# (3) key로 value 얻기
print("(3)--------------------")
me = {'name' : 'Choi Daehoon', 'age' : '22', 'nationality': 'korea'}
print(me['nationality'])
# 주의점
# [1] key가 중복되었을 때, 1번째를 제외한 나머지는 무시됨.
# [2] key에 리스트는 쓸 수 없고, 튜플은 가능함.(변하지 않는 값만 가능)

# (4) 딕셔너리 관련 함수
print("(4)--------------------")
dic1 = {'a' : 1, 'b' : 2, 'c' : 3}
print(dic1.keys()) # key 리스트 만들기
print(dic1.values()) # value 리스트 만들기
print(dic1.items()) # key, value 쌍 얻기
print(dic1.get('d')) # key 로 value 얻기, key가 없을 때 none을 리턴함.
print('a' in dic1, 'd' in dic1) # 해당 key가 딕셔너리 안에 있는지 조사하기
print(dic1.clear()) # key, value 쌍 모두 지우기