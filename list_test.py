# 복습
# 이스케이프 코드
'''
food = 'Python\'s favorite food os perl'
print(food)
say = '\'Python is very easy.\' he says.'
print(say)

# food 변수의 값을 대문자로 출력 p74

print(food.upper())
# say 변수의 값을 소문자로 출력 p74
print(say.lower())

print(say.title))

#리스트 변수  c언어 배열
#1. 여러개의 값을 저장
#2. 값을 변경 가능

h = ['lee', 17, 172.5, Ture]
print(h)
print(h[1]
c = h[1] + h[2]
print(c)

h[1] = 25
print(h)


singer = ['카리나', '강혜린', '김채원', '우기', '안유진', '아이유']
print(singer)
#append remove 값으로 추가 제거
singer.append('지젤') #값을 추가 append()
singer.append('루미')
singer.append('리사')
#print(singer)
singer.remove('카리나') #값을 삭제 remove()
#print(singer)
singer.remove('우기')
#print(singer)

#번지수로 삽입 제거 insert pop
singer.insert(1'박명수') #insert 삽입 위치 지정 가능

singer.insert(3'카더가든')
print(singer)
singer.pop(1) # pop 번지수로 삭제
print(singer)

fruit = ['사과', '망고', '키위', '귤', '딸기', '용과']
print(type(fruit)) #자료형
fruit.append('두리안') # 1. 두리안을 마지막에 추가하세요
fruit.remove('망고') # 2. 망고를 삭제하세요
fruit.pop(5) # 3. 5번지에 있는 과일을 삭제하세요
fruit.insert(2,'포도') # 4. 2번지에 포도를 삽입하세요
print(fruit)
fruit.clear() #리스트 변수 값 모두 삭제
print(fruit)
'''
#리스트변수 인덱싱

sport = ['야구', '축구', '농구', '배구', '탁구']
print(sport)
print(sport[1]) # 1번지 값 축구 출력
print(sport[1:4]) # 1~3번지 값 축구 농구 배구 출력
print(sport[0:5:2]) # 야구 농구 탁구 0 2 4















