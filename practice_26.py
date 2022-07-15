# 지역변수(함수호출시 만들어졌다가, 함수호출 끝나면 사라짐)와 전역변수(모든공간, 프로그램 내에서 부를 수 있는 변수)

# 전역변수는 많이 사용하면 코드가 지저분해짐
gun = 10 # 전역 공간 

def checkpoint(soldiers): # 경계근무
    # gun = 20 # 지역 변수
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}",format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))