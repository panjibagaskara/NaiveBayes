import csv
import fungsi as fg

C1,C2,train,test,hasil = [],[],[],[],[]
with open('TrainsetTugas1ML.csv') as trainn:
    reader = csv.reader(trainn, delimiter=',')
    next(reader)
    for row in reader:
        train.append(row)

with open('TestsetTugas1ML.csv') as testt:
    reader = csv.reader(testt, delimiter=',')
    next(reader)
    for row in reader:
        test.append(row)

PC1, nC1 = fg.PC(train,'>50K')
PC2, nC2 = fg.PC(train,'<=50K')
n = 8
akurasi = 0

for i in range(len(test)):
    PC1X,PC2X = 1,1
    PXC1,PXC2 = 1,1
    
    for j in range(1,n):
        a,b = fg.PXC(train,j,nC1,nC2,test[i])
        PXC1 *= a
        PXC2 *= b

    PC1X = PXC1 * PC1
    PC2X = PXC2 * PC2

    if PC1X > PC2X:
        hasil.append('>50K')
    else:
        hasil.append('<=50K')

with open('TebakanTugas1ML.csv','w',newline='\n') as Tulis:
    file = csv.writer(Tulis,dialect='excel')
    for i in range(0,len(hasil)):
        file.writerow([hasil[i]])
Tulis.close()
        