with open("D:\\python\\b41915014\\3B_0516\\singer1.csv", "r") as f:
    with open("D:\\python\\b41915014\\3B_0516\\singer2.csv", "w") as fs:
        h = f.readline()
        h = h.strip()
        hList = h.split(',')

        idx1 = hList.index('���̵�')
        idx2 = hList.index('�̸�')
        idx3 = hList.index('��� Ű')
        
        hList = [hList[idx1],hList[idx2],hList[idx3]] #������ ����Ʈ�� hList�� ����
        hStr = ','.join(map(str,hList))
        fs.write(hStr + '\n')
        for s in f:
            s = s.strip()
            rList = s.split(',')
            if int(rList[idx3]) >= 165:
                rList = [rList[idx1], rList[idx2], rList[idx3]]
                rStr = ','.join(map(str,rList))
                fs.write(rStr + '\n')

print('Save OK!')