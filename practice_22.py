# 함수
def open_account(): # 함수는 정의만 하는 거지 실제로 호출하기 전까지는 실행되지 않는다
    print("새로운 계좌가 생성되었습니다.")

# open_account() # 함수 호출

# 전달값과 반환값
def deposit(balance, money): # 입금(잔액, 추가하는 금액)
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money # 리턴을통해 반환된 금액을 balance에 저장

def withdraw(balance, money): #출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금, 수수료 나옴
    commission = 100 # 수수료 100원
    return commission, balance - money - commission #콤마를 이용하여 여러개의 값 반환이 가능하다.

balance = 0 # 잔액
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))