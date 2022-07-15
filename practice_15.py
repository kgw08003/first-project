# 퀴즈) 당신의 학교에서는 파이썬 코딩 대회를 주최한다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였다.
# 댓글 작성자들 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 된다.
# 추첨 프로그램을 작성하시오.

# 조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건 3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다--

# (활용 예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1)) # 랜덤으로 셔플 후 하나 뽑음

from random import *
users = range(1,21) # 1부터 20까지 숫자를 생성
# print(type(users)) # range는 리스트가 아니어서 리스트에서 쓰고자 하는 함수 사용 못함
users = list(users) # range 타입이던 users가 list로 변환되어 저장됨
# print(type(users)) # list로 저장 완료 - 큰수도 쉽게 뽑을 수 있음

print(users)
shuffle(users) # 셔플로 섞음
print(users)

winners = sample(users, 4) # 뽑은 4명 중에서 1명은 치킨, 3명은 커피

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0])) # winners 첫번째 치킨
print("커피 당첨자 : {0}".format(winners[1:])) # winners 첫번째 이후 3명 커피
print("-- 축하합니다--")
