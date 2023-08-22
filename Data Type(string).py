# 문자열에 작은따옴표 포함하기
a = "He's favorite fruit is strawberry.\n"
b = 'He\'s favorite fruit is strawberry.' # 역슬래쉬 \
print(a,b)

# 문자열 안에 큰따옴표 포함하기
a = '"I love strawberry.", he says.\n'
b = "\"I love strawberry.\", he says."
print(a,b)

# 줄 바꿈
a = "I need a love.\nSo i'm try to get girlfriend." # 이스케이프 코드
b = """ 
I need a love.
So i'm try to get girlfriend.""" # 연속된 작은,큰 따옴표 3개
c = '''
I need a love.
So i'm try to get girlfriend.'''
print (a,b,c)

# 문자열 연산
a = "Fly me "
b = "to the moon\n"
print(a+b,a*2)

# 문자열 길이 구하기
a = "You can show me who you are"
print(len(a)) # 공백 문자도 포함

# Indexing(가리킨다.) 와 Slicing(잘라 낸다.)
a = "Time is gold"
print("Indexing :", a[0], a[-1]) # 0부터 숫자를 센다. -1은 맨 뒤에서 부터 센다.
print("Slicing :", a[0:4], a[8:]) # 끝 번호에 해당되는 문자는 포함하지 않음.