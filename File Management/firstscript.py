f=open('inputFile.txt','r')
#print(f.read())
writeF=open('FailRecords.txt','w')
writeP=open('PassRecords.txt','w')
for l in f:
    sl=l.split()
    if (sl[2]=='F'):
        writeF.write(l)
    else:
        writeP.write(l)
f.close()
writeF.close()
writeP.close()