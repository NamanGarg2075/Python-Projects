mat = [[1,2,3],
       [4,5,6]]

matt = [[0,0],
        [0,0],
        [0,0]]

for i in range(len(mat)):
    for j in range(len(mat[0])):
        matt[j][i] = mat[i][j]

for i in matt:
    print(i)