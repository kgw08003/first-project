# 표준 입출력

# print("python", "Java", "JavaScript", sep=" vs ")

#  print("python", "Java", "JavaScript", sep=",", end="?") #end는 문장의 끝부분을 물음표로 바꾸어 달라(뒷문장이 연달아서 출려됨)
# print("무엇이 더 재밌을까요?")

# import sys
# print("python", "Java", file=sys.stdout) # 표준 출력으로 문장이 찍힘
# print("python", "Java", file=sys.stderr) # 표준 에러로 (필요시 따로 에러 처리함)

# 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subjuct, score in scores.items():
#     # print(subjuct, score)
#     print(subjuct.ljust(8), str(score).rjust(4), sep=":") # ljust(8): 8칸의 공간을 확보한 후 왼쪽정렬하라
# # rjust(8): 8칸의 공간을 확보한 후 왼쪽정렬하라

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) # zfill(3) 3크기 만큼 공간 확보하고 갚을 집어넣고 값이 없는 부분은 0으로 채워넣어라


# 표준 입력
# answer = input("아무 값이나 입력하세요 : ")
answer = 10  # 사용자 입력을 통해 입력을 받게 되면 항상 문자열 형태로 저장됨
print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")
