# 함수 기본값 설정 방법
# def profile(name, age, main_hobby):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#         .format(name, age, main_hobby)) #역슬러쉬 치고 엔터하면 하나의 문장으로 취급함

# profile("송우기", 24, "작곡")
# profile("김민니", 26, "댄스")

# 같은 학교 같은 학년 같은 반 같은 취미. - 기본값 사용

def profile(name, age=17, main_hobby="작곡"):
     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
         .format(name, age, main_hobby))

profile("송우기")
profile("김민니")
