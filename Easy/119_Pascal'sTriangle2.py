def getRow( rowIndex=33):
    numRows = rowIndex + 1
    PascalTriangle = []
    for i in range(1, numRows + 1):
        temp = [0] * i
        temp[0] = 1
        temp[-1] = 1
        PascalTriangle.append(temp)
    for idx, list in enumerate(PascalTriangle):
        length = len(list)
        if length > 2:
            for k, v in enumerate(list):
                if (k > 0 and k < length - 1):
                    PascalTriangle[idx][k] = PascalTriangle[idx - 1][k] + PascalTriangle[idx - 1][k - 1]
    return PascalTriangle[-1]
print(getRow())