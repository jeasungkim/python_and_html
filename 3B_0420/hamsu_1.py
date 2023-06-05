def Hello():
    "함수의 실명을 적을 수 있음" 
    print("안녕하세요")
    print("파이썬 함수 연습입니다.")
c=0
def add(a,b):
    "두 개의 변수를 받아 더하는 함수"
    global c
    c = a + b
    print(c) #pass 패스를 쓰면 오류가 안남

def addr(a,b):
    return a+b #return으로 하면 편함 안하면 global + c=0 해야함

x = add(10,20)

print(c)
print("-------------")
y = addr(10,20)
print(y)
Hello()
help(Hello)