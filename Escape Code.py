# 문자열 안에서 줄을 바꿀 때 사용
a =  "I am\nshy boy"
print(a)

#문자열 사이에 탭 간격을 줄 때 사용
a = "Iam\tshyboy"
print(a)

# \를 그대로 표현할 때 사용
a = "4\\3"
print(a)

# 작은 따옴표(')를 그대로 표현할 때 사용
a = 'I\'m shy boy'
print(a)

# 큰 따옴표(")를 그대로 표현할 때 사용
a = "\"I am shy boy\""
print(a)

# 캐리지 리턴(줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동)
a = """    Bad days make good stories
    \rBad days make good stories"""
print(a)