
a=[[2,3,4]
   ,[1,2,4]
   ,[1,2,3]]
b=[[2,3,4],
   [3,2,5]
   ,[6,4,3]]
c=[[0,0,0],[0,0,0],[0,0,0]]

m=0
for i in range(3):
    for j in range(3):
        for k in range(3):
            c[i][j] += a[i][k] * b[k][j]
            

print(c)
a=10
b=10
print('1' if a is b else 0)
