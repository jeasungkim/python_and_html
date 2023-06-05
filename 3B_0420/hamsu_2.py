a = 20 #전역
def func():
    a = 10 #지역
    print(a)

func() # 10
print(a) #20