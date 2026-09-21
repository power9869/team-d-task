# chatGPT통해서 받은 문제 연습용으로 풀어보기

drink = input("음료를 선택하세요:")
count = int(input("몇 잔 주문하시겠어요?:"))
# 아메리카노 > americano로 변경
americano = "아메리카노"
latte = "라떼"

total = count * 3000 # 5000으로 바꿔줘요

if drink == americano:
    print("총 금액은", total, "원입니다.")
elif drink == latte:
    total = count * 4000
    print("총 금액은", total, "원입니다.")
else:
    print("주문 할 수 없는 메뉴입니다.")