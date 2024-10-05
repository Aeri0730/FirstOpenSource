# 간단한 덧셈/뺄셈 프로그램

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a / b

def multiply(a,b):
    return a * b

def main():
    print("간단한 덧셈/뺄셈/곱셈/나눗셈 프로그램입니다.")
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    operation = input("연산을 선택하세요 (+, -, *, /): ")

    if operation == '+':
        result = add(num1, num2)
        print(f"결과: {num1} + {num2} = {result}")
    elif operation == '-':
        result = subtract(num1, num2)
        print(f"결과: {num1} - {num2} = {result}")
    elif operation == '/':
        result = divide(num1, num2)
        print(f"결과: {num1} / {num2} = {result}")

    elif operation == '*':
        result = multiply(num1, num2)
        print(f"결과 : {num1} * {num2} = {result}")
    else:
        print("잘못된 연산자입니다. +, -, *, / 중 하나를 입력하세요.")
 

if __name__ == "__main__":
    main()

