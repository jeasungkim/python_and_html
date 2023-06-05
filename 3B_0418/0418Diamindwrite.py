# diamond
y = int(input("숫자를 입력하세요:"))
x = int(y/2)+1

for i in range(1, 2*x):
    if(i <= x):
        for j in range(x-i):
            print(" ", end='')
        
        for j in range(2*i-1):
            print("0", end='')
        print()
    
    else :
        for j in range(i-x):
            print(" ", end='')
        
        for j in range((2*x-i)*2-1):
            print("0", end='')
        print()    