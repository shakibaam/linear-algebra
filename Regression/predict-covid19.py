import pandas
import csv
import numpy
import matplotlib.pyplot as plt


def echelon(matrix, rowNum1, m, column, n):
    for j in range(int(m) - rowNum1 - 1):

        temp = (matrix[rowNum1 + j + 1][column] / matrix[rowNum1][column]) * (-1)
        # print(temp)

        for i in range(int(n)):
            matrix[rowNum1 + j + 1][i] += matrix[rowNum1][i] * temp

    # print(matrix)
    return matrix


def reducedEchelon(matrix, n, rowNum):
    # print(matrix[rowNum][rowNum])

    for i in range(rowNum - 1, -1, -1):
        # print(i)
        temp = (matrix[i][rowNum] / matrix[rowNum][rowNum]) * (-1)

        # print(temp)
        for j in range(n):
            matrix[i][j] += temp * matrix[rowNum][j]

    print(matrix)
url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/ecdc/total_cases.csv"
df = pandas.read_csv(url, index_col=0)

df = pandas.read_csv(url)

world = df.World.tolist()

# print(world)

print(world)
print(len(world))
recent_7 = []
x = len((world)) - 6
y = len(world) + 1

for i in range(x, y):
    recent_7.append(i)

# print(t)

notUse = len(world) - 7
active_case_before7 = world[0:notUse]
active_size = len(active_case_before7)
active_case_after7 = world[notUse:len(world)]
# print(active_case_after7)


matA = numpy.zeros((active_size, 3))

for i in range(active_size):
    for j in range(3):
        if j == 0:
            matA[i][j] = 1
        elif j == 1:

            matA[i][j] = (i + 1)
        elif j == 2:
            matA[i][j] = ((i + 1) * (i + 1))

matA = numpy.int64(matA)
# print(matA)

active_case_before7 = numpy.array(active_case_before7)
active_case_before7 = active_case_before7.reshape((active_size, 1))
active_case_before7 = active_case_before7.astype(numpy.int64)

matA_transpose = matA.transpose()
matA_transpose = matA_transpose.astype(numpy.int64)

At_mul_A = numpy.dot(matA_transpose, matA)
At_mul_A = At_mul_A.astype(numpy.int64)

At_mul_active = numpy.dot(matA_transpose, active_case_before7)
At_mul_active = At_mul_active.astype(numpy.int64)

Augmented = numpy.hstack((At_mul_A, At_mul_active))
Augmented = Augmented.astype(numpy.int64)
print(Augmented)

for i in range(2):
    echelon(Augmented, i, 3, i, 4)

print(Augmented)
arr = []
for i in range(3):
    if i != 0:
        arr.insert(0, i)

for i in arr:
    reducedEchelon(Augmented, 4, i)

print(Augmented)

b = []
for i in range(3):
    temp = Augmented[i][3] / Augmented[i][i]
    # print(temp)
    b.append(temp)

b = numpy.array(b)
b = b.reshape((3, 1))
b = b.astype(numpy.int64)
print(b)
print(b)

predicted = []

for i in recent_7:
    temp1 = b[0][0] + b[1][0] * i + b[2][0] * i * i
    # print(temp1)
    predicted.append(temp1)

predicted = numpy.array(predicted)
print(predicted)
#

len1 = len(world)
All_predicted = []

date_until_now = []

for i in range(len1):
    date_until_now.append(i + 1)

for i in date_until_now:
    tempp = b[0][0] + b[1][0] * i + b[2][0] * i * i
    # print(i)
    # print(tempp)
    All_predicted.append(tempp)

All_predicted = numpy.array(All_predicted)
All_predicted = All_predicted.astype(numpy.int64)
# print(All_predicted)

#
world=numpy.array(world)
world=world.astype(float)
plt.plot(date_until_now,world)
plt.plot(date_until_now,All_predicted)

plt.title("covid-19 until now")
plt.xlabel("Days since starts of covid 19 ")
plt.ylabel("Cases")
plt.show()
