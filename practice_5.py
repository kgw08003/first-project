# 슬라이싱 , 필요한 정보만 잘라서 사용하는 것


jumin = "990120-1234567"

print("성별 :" + jumin[7])
print("년 :" + jumin[0:2]) #0 ~ 2 직전까지 (0,1)
print("월 :" + jumin[2:4])
print("일 :" + jumin[4:6])
print("성별 :" + jumin[0:6])
print("성별 :" + jumin[:6]) #위와 같은 의미
print("성별 :" + jumin[7:14])
print("성별 :" + jumin[7:]) #위와 같은 의미
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])
# 맨 뒤에서 7번째부터 끝까지
