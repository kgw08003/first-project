#if
# wather = "맑아요"
# wather = input("오늘 날씨는 어때요? ")
# # if 조건:
# #     실행 명령문
# if wather == "비" or wather == "눈":
#     print("우산을 챙기세요")
# elif wather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

temp = int(input("기온은 어때요? ")) #input은 항상 문자형태로 받으니 날씨는 숫자 임으로 int로 감싸 정수형태로 받는다.
if 30 <= temp:
    print("너무 더우니 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("따뜻한 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추우니 나가지 마세요")
