# 튜플 - 내용 변경이나 추가는 불가능하지만 속도가 리스트보다 빠름
# 변경되지 않는 목록을 이용할때 튜플 사용

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") 튜플은 add제공 x , 값 추가 불가하고 고정된 값만 사용가능

# name = "송우기"
# age = 24
# bobby = "작곡"
# print(name, age, hobby)

(name, age, hobby) = ("송우기", 24, "작곡")
print(name, age, hobby)