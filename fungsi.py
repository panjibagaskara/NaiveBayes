# Menghitug P(C)
def PC(data,x):
    j = 0
    for i in range(len(data)):
        if data[i][8] == x:
            j += 1
    return j/len(data),j

def PXC(data, n, nC1, nC2, x):
        yes, no = 0,0
        for i in range(len(data)):
                if data[i][n] == x[n] and data[i][8] == '>50K':
                        yes += 1
                elif data[i][n] == x[n] and data[i][8] == '<=50K':
                        no += 1
        return yes/nC1, no/nC2