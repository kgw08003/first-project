# 파일 입출력

# score_file = open("score.txt", "w", encoding="utf8") # "w"는 쓰기용도로 사용, 덮어쓰기
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # 기존 파일에 추가로 내용 쓸때 "a"업핸드 나타내는 a 이용
# score_file.write("과학 : 80") # 추가 할때는 줄바꿈이 없음으로 명시적으로 작성해야함
# score_file.write("\n코딩 : 100")

# score_file = open("score.txt", "r", encoding="utf8") 
# print(score_file.read()) # 파일에 있는 내용 전부 다 읽기
# score_file.close()


# score_file = open("score.txt", "r", encoding="utf8") # 파일 읽기 모드로 열기
# print(score_file.readline())# 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline(), end="") # 파일에서는 자동으로 줄바꿈 되니 줄바꿈 안하려면 end=""이용
# print(score_file.readline())
# score_file.close()

# # 파일이 총 몇줄인지 모를때 반복문을 통해서 파일을 가져옴
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="") # 줄바꿈 안하기 위해 end="" 정의함
# score_file.close()

# 리스트에 값을 다 넣어서 처리
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 모든 라인을 가져와 list형태로 저장
for line in lines:
    print(line, end="")
score_file.close()