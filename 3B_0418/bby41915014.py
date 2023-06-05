
f = open("D:\\python\\b41915014\\c.txt", 'w')
f.write("동해물\n안녕하세요\nHello World!!")
f.close()

f = open("D:\\python\\b41915014\\c.txt", 'rt')
lines = f.readlines()
for line in lines:
  print(line, end='')
f.close()
