import copy
def print_arr(x):
    for i in range(len(x)):
        print(x[i])
    print()
# 0 - online
# 1 - infected
# 2 - offline
x1 = [   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 2, 0, 0]]

x = [  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def sex(x):
    numberOfNodesInfected = 0
    x_prev = copy.deepcopy(x)
    x_new = copy.deepcopy(x)
    for i in range(len(x_prev)):
        for j in range(len(x_prev[i])):
            if x_prev[i][j] == 1:
                if (i - 1) >= 0 and x_prev[i-1][j] != 2 and x_new[i-1][j]==0:
                    x_new[i - 1][j] = 1
                    numberOfNodesInfected += 1
                if (i + 1) < len(x_prev) and x_prev[i+1][j] != 2 and x_new[i+1][j]==0:
                    x_new[i + 1][j] = 1
                    numberOfNodesInfected += 1
                if (j - 1) >= 0 and x_prev[i][j-1] != 2 and x_new[i][j-1]==0:
                    x_new[i][j - 1] = 1
                    numberOfNodesInfected += 1
                if (j + 1) < len(x_prev[i]) and x_prev[i][j+1] != 2  and x_new[i][j+1]==0:
                    x_new[i][j + 1] = 1
                    numberOfNodesInfected += 1
    return x_new, numberOfNodesInfected

def infectedSum(x):
    sum = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == 1:
                sum = sum + 1
    return sum

def onlineSum(x):
    sum = 0
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == 0:
                sum = sum + 1
    return sum

infected  = infectedSum(x)
online = onlineSum(x)
numberOfNodesInfected = 1
days = 0
while numberOfNodesInfected != 0:
    x, numberOfNodesInfected = sex(x)
    days += 1
    print(days)
    print_arr(x)
    print()

if onlineSum(x) == 0:
    print('Everything is infected on step', days-1)
else:
    print('Some nodes are imposible to reach')