import keyword
import calendar
import datetime


#print(keyword.kwlist)
#print(calendar.month(2009,9))
today = datetime.date.today()
print(today.year)
print(today.month)
print(today.day)
now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now. minute, now.second)

#입출력 복습
'''
#비만도(BMI) 구하기 몸무게/(키의제곱) *10000

height = int(input('키를 입력하세요: '))
weight = int(input('몸무게를 입력하세요: '))
BMI = weight/(height**2) *10000
print(f'당신의 비만도는 {round(BMI)}입니다')


#반올림 round()
pi = 3.6451
print(round(pi, 1))
print(round(pi, 2))


#사칙연산 계산기 만들기
num1 = int(input('첫번째 숫자를 입력하시오:'))
num2 = int(input('두번째 숫자를 입력하시오:'))
add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2
print(f'덧셈 결과: {add_result}')
print(f'뺄셈 결과: {sub_result}')
print(f'곱셈 결과: {mul_result}')
print(f'나눗셈 결과: {round(div_result)}')
'''
#변수 P63



















