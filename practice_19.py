# continue 와 break - 반복문 내에서 쓸 수 있음


absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1, 11): # 1 ~ 10
    if student in absent:
        continue # 아래문장을 실행시키지 않고 다음 반복으로 진행해라
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와.".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))
