# while 반복문 - 어떤 조건이 만족할때까지 반복

# customer = "송우기"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1 # 한번 부르면 한번씩 횟수를 줄여나감
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "김민니"
# index = 1
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1

customer = "조미현"
person = "Unknown"

while person != customer : # 이조건에 만족할때까지 계속 반복
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")


