# 참 / 거짓
from collections import namedtuple


print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not(5>10))
#변수 애완동물을 소개해 주세요
# 변수는 값을 저장하는 공간
animal = "강아지"
name = "연탄이" #문자열 큰따옴표
age = 4 #정수형 따옴표 없이
hobby = "산책"
is_adult = age >= 3

print("우리집" + animal +"의 이름은 " + name +"예요")
print(name + "는" + str(age) +"살이며" + hobby +"을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))
#변수는 맨위에 선언할 수도 있지만 중간에도 선언할 수 있다
# +말고도 ,를 이용하여서도 문장을 합할 수 있다 컴마를 사용하면 정수형 문자를 str사용 안해도 출력은 가능하지만
# ,를 사용하면 한칸 띄어쓰기 화 된다 , 여러줄 주석처리 ctrl + 슬러쉬

# 퀴즈
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")

# 연산자
print(1+1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 2
print(10%3) # 1
print(5//3) # 몫 구하기 1
print(10//3) # 3

print(10 > 3) #True
print(4 >= 7) #False
print(10 < 3) #False
print(5 <= 5) #True

print(3 == 3) #True
print(4 == 2) #False
print(3 + 4 == 7) #True

print(1 != 3) # 같지않다 True
print(not(1 !=3)) #False

print((3 > 0) and (3 < 5)) #True
print((3 > 0) & (3 < 5) ) #True

print((3 > 0) or (3 > 5)) #True
print((3 > 0) | (3 > 5)) #True

print(5 > 4 > 3) #True
print(5 > 4 > 7) #False

print(2 + 3 * 4) # 14
print((2 + 3)* 4) #우선순위 연샨 20
number = 2 + 3 * 4
print(number)
number = number + 2 # 16
print(number)
number += 2 #18
print(number)
number *= 2 #36
print(number)
number /= 2 #18
print(number)
number -= 2 #16
print(number)

number %= 2 #0
print(number)
