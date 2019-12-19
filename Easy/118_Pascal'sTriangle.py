def generate(numRows=5):
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
    return PascalTriangle
def generate1( numRows=5):
    result = []
    for i in range(numRows):
        r = [1]*(i+1)
        if i+1 <= 2:
            result.append(r)
            continue
        for j in range(i-1):
            r[j+1]=result[-1][j]+result[-1][j+1]
        result.append(r)
    return result
print(generate1())