# 문자열 포멧

print("나는 %d살 입니다." % 20) #정수
print("나는 %s을 좋아해요." % "파이썬") #문자열
print("Apple 은 %c로 시작해요." % "A") # 문자
# %s
print("나는 %s살 입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# # 방법 2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
# print("나는 {age}살이며, {coler}색을 좋아해요.".format(age = 20, color="빨간"))
# print("나는 {age}살이며, {coler}색을 좋아해요.".format(color="빨간", age = 20))

# 원하는 범위 드래그 후 컨트롤 슬레쉬 하면 전체 주석처리 됨

#방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")