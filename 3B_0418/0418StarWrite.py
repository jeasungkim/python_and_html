n = int(input("몇 줄짜리 별을 출력할까요? "))

for i in range(1, n+1):
    print("*" * i)
print(10)
for i in range(n, 0, -1):
    print("*" * i)

