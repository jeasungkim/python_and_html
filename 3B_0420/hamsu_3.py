a = 10
def func():
    b = 20 #지역
    print(b)
    return a + b

x = func() 
print(x) 