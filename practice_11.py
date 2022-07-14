# 사전

# cabinet = {3: "민니", 100: "우기"} # 키는 3 벨류 민니, 두번째 열괴 키 100 벨류 우기
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))

# print(cabinet[5]) # 대괄호를 이용하여 없는 키 사용시 오류발생시키고 바로끝냄
# print(cabinet.get(5)) # get 이용시 값이 없음 none이라 출력하고 아래 계속 출력함
# print(cabinet.get(5, "사용 가능")) # none이후 값이 없으면 사용 가능 이라고 출력, 5번 열쇠 사용 가능이라 할 수 있음
# print("hi")

# print(3 in cabinet) # True
# print(5 in cabinet) # False

cabinet = {"A-3":"우기", "B-100":"민니"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "미연"
cabinet["C-20"] = "슈화"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)