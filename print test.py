#입출력문 연습 - print() input()
#주석 - 번역 X - 환줄 주석
#여러줄 수석 ''' ''' ''''' '''''
'''
print('hello world')
print('남명진')
message = '안녕하세요. 저는 인평자동차 고등학교 AI1-2반 남명진입니다.'
print(message)
message2 = 'i really want to stay at your house'
print(message2)
'''
#변수와 자료형
'''
a = 4
b = 2.5
c = 'hello'
d = 5672
print('a변수에 입력된 값은 ' ,a, '입니다')
a = 54
print('a변수에 입력된 값은 ' ,a, '입니다')
print(type(a))
print(type(b))
print(type(c))
print(type(d))
'''

#입력문 - input()
'''
name = input('이름을 입력하세요: ')
print('입력한 이름은: ' ,name, '입니다')
age = input('나이를 입력하세요: ')
print('내이름은' ,name,'이고 나이는' ,age,'살 입니다.')
'''
# 두 수의 덧셈(키보드로부터 수를 입력받기)
#키보드로 부터 입력받으면 모두 문자로 취급
#형 변환 => 캐스트연산 cast
'''
a = 7
b = 52
c = a+b
'''
a = int(input('a를 입력하시오:')) #캐스트연산 (문자=>정수)
b = int(input('b를 입력하시오:')) #str =>int
c= a*b
print(c)











