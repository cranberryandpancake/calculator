def calculator():
    print(" ⚊ ⚊ ⚊ ⚊ 계산기 ⚊ ⚊ ⚊ ⚊")
    print("⚊ ⚊ ⚊ ⚊ 연산 부호 ⚊ ⚊ ⚊ ⚊")
    print("      1) + 2) - 3) * 4) /")

    cal = int(input("어떤 연산을 원하시나요?"))
    num_01, num_02 = map(int, input("연산을 원하는 숫자 두 개를 입력하세요.").split())

    if cal == 1:
        result = "{} + {} = {}".format(num_01, num_02, num_01 + num_02)
    elif cal == 2:
        result = "{} - {} = {}".format(num_01, num_02, num_01 - num_02)
    elif cal == 3:
        result = "{} * {} = {}".format(num_01, num_02, num_01 * num_02)
    elif cal == 4:
        if num_02 != 0:
            result = "{} / {} = {}".format(num_01, num_02, num_01 / num_02)
        else:
            return "오류! 0으로 나눌 수 없습니다."
    else:
        return "오류! 잘못된 연산 부호입니다."

    return result

print(calculator())
