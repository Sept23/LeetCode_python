def matrixReshape( nums=[[1,2],[3,4]], r=2, c=4) :
    matrixSize = r * c
    matrix = []
    for row in nums:
        # matrix.extend(row)
        matrix += row
    if len(matrix) != matrixSize:
        return nums
    else:
        res = []
        for i in range(r):
            res.append(matrix[i*c :(i+1)* c])
        return res
print(matrixReshape())