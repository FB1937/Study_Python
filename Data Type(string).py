# 문자열에 작은따옴표 포함하기
a = "He's favorite fruit is strawberry.\n"
b = 'He\'s favorite fruit is strawberry.' # 역슬래쉬 \
print(a,b)

# 문자열 안에 큰따옴표 포함하기
a = '"I love strawberry.", he says.\n'
b = "\"I love strawberry.\", he says."
print(a,b)

# 줄 바꿈
a = "I need a love.\nSo i'm try to get girlfriend."
b = """
I need a love.
So i'm try to get girlfriend."""
c = '''
I need a love.
So i'm try to get girlfriend.\a'''
print (a,b,c)