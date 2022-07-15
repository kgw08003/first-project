# for - 반복문

# print("대기번호: 1")
# print("대기번호: 2")
# print("대기번호: 3")
# print("대기번호: 4")

# for waiting_no in [0, 1, 2, 3, 4]: # 특별한 값을 넣을때 사용

#randrange
# for waiting_no in range(6): # 0 ~ 5
#     print("대기번호 : {0}".format(waiting_no))

starbuks = ["송우기", "김민니", "예슈화", "전소연","조미연"]
for customer in starbuks:
    print("{0}, 커피가 준비되었습니다.".format(customer))