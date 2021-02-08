import numpy
n=int(input())
matA=numpy.zeros((n, n))
matA1=numpy.zeros((n, n))
matU=numpy.zeros((n, n))
matU1=numpy.zeros((n, n))
matL=numpy.zeros((n, n))
matL1=numpy.zeros((n, n))

for i in range(n):

   matA[i]=input().split(" ")
   matA1[i] = matA[i]





def UAndL(matrix, rowNum1, rowNum2, n):
    s = min(rowNum1, rowNum2)

    for j in range(n - rowNum1 - 1):

        temp = (matrix[rowNum1 + j + 1][rowNum1] / matrix[rowNum1][rowNum1]) * (-1)

        for i in range(n ):
            matrix[rowNum1 + j + 1][i] += matrix[rowNum1][i] * temp
    #print(matrix)
    return matrix










def forward(Augmented,n):
    for i in range(n):
        for j in range(i+1,n):
            temp=Augmented[j][i]*(-1)/Augmented[i][i]
            Augmented[j][i]+=Augmented[i][i]*temp

            Augmented[j][n]+=Augmented[i][n]*temp
    arr = numpy.array(Augmented[:, n])
    arr = arr.reshape((n, 1))

    return arr


def backward(Augmented,n):
   for i in range(n-1,0,-1):

       for j in range(i-1,-1,-1):

           temp=(-1)*Augmented[j][i]/Augmented[i][i]
           Augmented[j][i]+=temp*Augmented[i][i]
           Augmented[j][n]+=temp*Augmented[i][n]

   for i in range(n):
       Augmented[i][n]/=Augmented[i][i]
       Augmented[i][i]/=Augmented[i][i]

   arr = numpy.array(Augmented[:, n])
   arr = arr.reshape((n, 1))

   return arr

for i in range(n):
    if i+1<n:

      for j in range(i,n):
          matL[j][i]=matA[j][i]/matA[i][i]

      temp= UAndL(matA, i, i + 1, n)
   # print(temp)

matL[n-1][n-1]=1
matU=matA
matU1=matU
print("U is: ")
print(matU)



matL1=matL
print("L is:")
print(matL)


Ainverse=numpy.zeros((n,n))
identity=numpy.zeros((n,n))
for i in range(n):
    identity[i][i]=1



for i in range(n):
    arr = numpy.array(identity[i, :])
    arr = arr.reshape((n, 1))
    Augmented=numpy.hstack((matL,arr))
    Augmented2=numpy.hstack((matU1, forward(Augmented,n)))

    temp=backward(Augmented2, n)

    for j in range(n):
        Ainverse[j][i]=temp[j][0]
    print("A inverse is:")
    print(Ainverse)




