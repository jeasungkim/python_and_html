def printList(pList):
    for data in pList:
        print(data, end='\t')
    print()
    
with open("D:\\python\\b41915014\\3B_0516\\singer1.csv", 'r') as f:
#    header = f.readline()
#    header = header.strip()
#    headerList = header.split(',')
#    printList(headerList)
    for s in f:
        s = s.strip() #����, \n ���ִ� ����
        rowList = s.split(',') #���ڿ��� ����Ʈ�� ����
        printList(rowList)