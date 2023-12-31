# 파이썬 프로그래밍의 기초 자료형

# 문자열 자료형

# (1) 문자열에 작은따옴표 포함하기
print("(1)--------------------")
a = "He's favorite fruit is strawberry.\n"
b = 'He\'s favorite fruit is strawberry.' # 역슬래쉬 \
print(a,b)

# (2) 문자열 안에 큰따옴표 포함하기
print("(2)--------------------")
a = '"I love strawberry.", he says.\n'
b = "\"I love strawberry.\", he says."
print(a,b)

# (3) 줄 바꿈
print("(3)--------------------")
a = "I need a love.\nSo i'm try to get girlfriend." # 이스케이프 코드
b = """ 
I need a love.
So i'm try to get girlfriend.""" # 연속된 작은,큰 따옴표 3개
c = '''
I need a love.
So i'm try to get girlfriend.'''
print (a,b,c)

# (4) 문자열 연산
print("(4)--------------------")
a = "Fly me "
b = "to the moon\n"
print(a+b,a*2)

# (5) 문자열 길이 구하기
print("(5)--------------------")
a = "You can show me who you are"
print(len(a)) # 공백 문자도 포함

# (6) Indexing(가리킨다.) 와 Slicing(잘라 낸다.)
print("(6)--------------------")
a = "Time is gold"
print("Indexing :", a[0], a[-1]) # 0부터 숫자를 센다. -1은 맨 뒤에서 부터 센다.
print("Slicing :", a[0:4], a[8:]) # 끝 번호에 해당되는 문자는 포함하지 않음.
print(a[:8] + 'sliver') # 문자열 치환하는 방법

# (7) 문자열 포매팅
print("(7)--------------------")
a = 3
b = "one"
print("I have a %d icecream and ate %s " %(a, b))
# %s(문자열), %c(문자 1개), %d(정수), %f(부동소수)
# %o(8진수), %x(16진수), %%(문자 % 자체)

# (8) 정렬과 공백
print("(8)--------------------")
print(",%10s, %-20smeet you," % ("Hi", "Nice to"))

# (9) 소수점 표현하기
print("(9)--------------------")
print("%10.4f" %3.1415681717) # %0.3f의 0은 길이에 상관하지 않겠다는 뜻임.

# (10) format 함수를 사용한 포매팅
print("(10)--------------------")
print("I ate {0} breads and {1} glass of orange juice. So i'm {situation} now".format(6, 3, situation = "full"))
# {0}, {1}은 입력값의 순서임. name=value와 혼용 가능.
print(",{0:=>10},{1:^10},{2:!<10},".format("apple", "kiwi", "orange"))
# :>은 오른쪽, :^은 가운데 :<은 왼쪽 정렬임. 그리고 공백 채우기는 위와 같음.

# (11) f 문자열 포매팅
print("(11)--------------------")
number = 2.216873
print(f"{{number}}, {number:10.3f}") #소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤.
# {{}}으로 {} 표현함.
# f 접두사를 붙이면 f 문자열 포매팅 이용 가능.

# (12) 문자열 내장 함수
print("(12)--------------------")
a = "My favoite activity is baseball."
b = "   Thank you   "
# 문자 개수 세기, 위치 알려주기
print(a.count('i'), a.find('a'), a.find('d'))
# 문자열 삽입
print(",".join(a[:3]))
# 소문자 -> 대문자 변환, 대문자 -> 소문자 변환
print(a[:2].upper(), a[:2].lower())
# rstrip, lstrip, strip(양쪽 공백 지우기)
print(b.rstrip(), b.lstrip(), b.strip())
# 문자열 바꾸기
print(a.replace("baseball", "basketball"))
# 문자열 나누기 (리스트에 넣음)
print(a.split(), a.split("a"))