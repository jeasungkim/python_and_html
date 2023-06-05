
import sys

f = open("D:\\python\\b41915014\\c.txt",'w')
sys.stdout = f
for i in range(2,10):
  for j in range(1,10):
    print("{} x {} = {}".format(i,j,i*j))
  print()
f.close()
