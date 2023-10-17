m1 = [[1,2,3,4],[4,5,6,7]]  # 2*4
m2 = [[9,8,7],[4,5,6],[1,2,3],[5,4,3]]  #4*3

m3 =[]

for i in range(len(m1)):
    for j in range(len(m2[0])):
        sum = 0

        for k in range(len(m1[0])):
            mul = m1[i][k] * m2[k][j]
            sum += mul
        m3.append(sum)


print(m3)






