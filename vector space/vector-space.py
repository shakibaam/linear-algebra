from __future__ import division
import numpy
from click._compat import raw_input


the_string = raw_input()
m, n = the_string.split()

# print(m + " " + n)
matA = numpy.zeros((int(m), int(n)))

for i in range(int(m)):
    matA[i] = input().split(" ")

# print(matA)


matrixB = numpy.zeros((int(m), 1))

Augmented = numpy.hstack((matA, matrixB))

# print(Augmented)


# اگر اولین عنصر در ماتریس صفر بود با جابه جایی ردیفی عنصر غیر صفر را بالا می آوریم

if Augmented[0][0] == 0:
    flag1 = False
    i = 1
    while flag1 != True:
        if Augmented[i][0] != 0:
            for j in range(int(n) + 1):
                temp = Augmented[0][j]
                Augmented[0][j] = Augmented[i][j]

                Augmented[i][j] = temp
        flag1 = True
    else:
        i += 1


def echelon(matrix, rowNum1, m, column, n):
    for j in range(int(m) - rowNum1 - 1):

        temp = (matrix[rowNum1 + j + 1][column] / matrix[rowNum1][column]) * (-1)

        for i in range(int(n)):
            matrix[rowNum1 + j + 1][i] += matrix[rowNum1][i] * temp

    #print(matrix)
    return matrix


def reducedEchelon(matrix, n, rowNum):
    for i in range(rowNum - 1, -1, -1):
        temp = (matrix[i][rowNum] / matrix[rowNum][rowNum]) * (-1)
        print(temp)
        for j in range(n):
            matrix[i][j] += temp * matrix[rowNum][j]

    # print(matrix)


def reducedEchelon2(matrix, n, rowNum, clumn):
    for i in range(rowNum - 1, -1, -1):
        print(matrix[rowNum][clumn])
        temp = (matrix[i][clumn] / matrix[rowNum][clumn]) * (-1)
        # print(temp)
        for j in range(n):
            matrix[i][j] += temp * matrix[rowNum][j]

    # print(matrix)


m1 = int(m)
n1 = int(n)
arr = []
for i in range(m1 - 1):

    temp = i
    if i == 0:

        echelon(Augmented, 0, m1, 0, n1)

    else:
        flag = False
        counter = 0
        while flag != True and temp <= n1 - 1:
            if Augmented[i][temp] != 0:
                flag = True
            else:
                temp += 1

            counter += 1

        if flag == False:

            Augmented[[i, i + 1]] = Augmented[[i + 1, i]]
            continue

        elif flag == True:
            # print(temp)

            echelon(Augmented, i, m, temp, n)
print("echelon form of matrix: ")
print(Augmented)

arr2 = []
for i in range(m1):
    temp1 = i
    if Augmented[i][temp] != 0:
        arr.append(temp1)
        arr2.append(i)

    else:

        while temp1 < n1 and Augmented[i][temp1] == 0:
            temp1 += 1

    if Augmented[i][temp1] != 0:
        arr.append(temp1)
        arr2.append(i)


# print(arr2)
# counter=0
# for i in arr2:
#     tempp=arr[counter]
#     for j in range(tempp,n1):
#         print(Augmented[i][j])
#         Augmented[i][j]=Augmented[i][j]/Augmented[i][tempp]
#         print(Augmented[i][j])
#     counter+=1

#print(Augmented)


print("base for column space:")
for i in arr:
    m2=matA[:,i]
    m2 = m2.reshape((m1,1))
    print(m2)


flag2=False
counter1=0

print("base for row space:")

for i in range(m1):
    counter1 = 0
    for j in range(n1):
        if Augmented[i][j]==0:
            counter1+=1

   # print(counter1)

    if counter1!=n1:
         m1 = Augmented[i,0:n1]
         m1=m1.reshape((int(m), 1))
         print(m1)


# print(arr)

matAprime = numpy.zeros((int(m), len(arr)))

for i in range(int(m)):
    for j in range(len(arr)):
        matAprime[i][j] = matA[i][(int(arr[j]))]

# print(matAprime)
# print(arr)

temperoryA = matAprime
for i in range(n1):
    if i not in arr:
        # print(i)
        m2 = matA[:, i]
        m2 = m2.reshape((int(m), 1))
        temperoryA = numpy.hstack((matAprime, m2))
        # print("temperory:")
        # print(temperoryA)

        for i in range(int(m) - 1):

            temp = i
            if i == 0:

                echelon(temperoryA, 0, int(m), 0, int(n))

            else:
                flag = False
                counter = 0
                while flag != True and temp <= n1 - 1:
                    if temperoryA[i][temp] != 0:
                        flag = True
                    else:
                        temp += 1

                    counter += 1

                if flag == False:
                    # print("hello")
                    temperoryA[[i, i + 1]] = temperoryA[[i + 1, i]]
                    continue

                elif flag == True:
                    # print(temp)

                    echelon(temperoryA, i, m, temp, n)

        # print(temperoryA)

        for i in range(int(m)):
            if temperoryA[i][i] != 0:
                reducedEchelon(temperoryA, int(n), i)

        print("this non pivot column(see just in bottom of this text) according to pivot column")
        print(m2)
        print("you see the coefficent of the pivot column sequential :")
        for k in range(int(m)):
            if temperoryA[k][k] != 0:
                print(temperoryA[k][int(n) - 1] / temperoryA[k][k])



def Reverse(lst):
    return [ele for ele in reversed(lst)]


arr_reverse = Reverse(arr)
arr2_reverse = Reverse(arr2)
count = 0
for i in arr_reverse:
    reducedEchelon2(Augmented, int(n), arr2_reverse[count], i)
    count += 1

# print(Augmented)

nonPivpt = []
for i in range(int(n)):
    if i not in arr:
        nonPivpt.append(i)

# print(nonPivpt)
for i in nonPivpt:

    base = []
    c = 0

    base.insert(i, 1)

    for j in arr2:
        t = arr[c]
        t1 = arr2[c]
        base.insert(arr[c], Augmented[j][i] / Augmented[t1][t])
        c += 1

    lst = numpy.array(base)

    lst = lst.reshape((int(m), 1))
    print("you see bases for null space : ")
    print(lst)
