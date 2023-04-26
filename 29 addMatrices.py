mat1 = [[1,2,3],
        [4,5,6],
        [7,8,9]]

mat2 = [[9,8,7],
        [6,5,4],
        [3,2,1]]

result =[[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        result[i][j] = mat1[i][j] + mat2[i][j]
    
for i in result:
    print(i)
