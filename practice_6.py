# 문자열 처리함수

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) #파이썬 첫번째 값이 대문자이냐?
print(len(python)) #파이썬 전체가 몇자인지
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("Java")) # find는 원하는 값 없음 -1 출력함
# index = python.index("Java") - index는 원하는 값 없음 오류 

print(python.count("n")) # count는 원하는 값 몇번 출력되는지 알려줌
