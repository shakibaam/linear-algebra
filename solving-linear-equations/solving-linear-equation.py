import numpy
n=int(input())
matA=numpy.zeros((n, n))


for i in range(n):

   matA[i]=input().split(" ")


entries = list(map(int, input().split()))
matrixB = numpy.array(entries).reshape(n, 1)

Augmented=numpy.hstack((matA,matrixB))




def func(i,matrix,n):
    count=0
    for j in range(n):
        if matrix[i][j]==0:
            count+=1

    if count==n:
        return True
    else:return False







def rowReduced(matrix, rowNum1, rowNum2, n):
   s=min(rowNum1,rowNum2)




   for j in range(n - rowNum1 - 1):


    temp = (matrix[rowNum1+j+1][rowNum1] / matrix[rowNum1][rowNum1]) * (-1)

    for i in range(n+1):

     matrix[rowNum1+j+1][i] += matrix[rowNum1][i] * temp
   print(matrix)


#Anasor balaye pivotha ra sefr mikonim

def reducedEchelon(matrix,n,rowNum):
    for i in range(0,rowNum):
        temp=(matrix[i][rowNum]/matrix[rowNum][rowNum])*(-1)
        for j in range(n+1):


          matrix[i][j]+=temp*matrix[rowNum][j]










for i in range(n):
    if i+1<n:
        if Augmented[i][i]!=0:
            rowReduced(Augmented,i,i+1,n)
        else:
            Augmented[[i,i+1]]=Augmented[[i+1,i]]
            rowReduced(Augmented, i, i + 1, n)



count=0
for j in range(n):
  if Augmented[n-1][j]==0:
    count+=1

    if count==n:
        if Augmented[n-1][n]==0:
            print("infinite solution")
            exit()
        else:
            print("No solution")
            exit()




for i in range(n):
    reducedEchelon(Augmented,n,i)
print("reduced Echelon Form:")
print(Augmented)
counter=0
for i in range(n):
  for j in range(n):
      if i==j:
          if Augmented[i][i]!=0:
              counter+=1
#dar nahayat baraye javab adad pivot ra be adad b moghabel an taghsim karde va javab ra namayesh midahim

if counter==n:
    for i in range(n):
        Augmented[i][n] = Augmented[i][n] / Augmented[i][i]

    print("solution is : ")
    print(Augmented[:, n])































