from matplotlib import pyplot
import numpy as np
import win32com.client as w

spk = w.Dispatch("SAPI.SpVoice")


# this is datasets of flowers type (1 for red and 0 for blue ) 
data = [
    [1, 1, 0],
    [2, 1,   0],
    [2, .5, 0],
    [3,   1, 0],
    [3, 1.5, 1],
    [3.5,   .5, 1],
    [4, 1.5, 1],
    [5.5,   1,   1]
]

mystery = [4.5 , 1]

pyplot.figure(1)
pyplot.axis([0,6,0,6])
pyplot.grid()
for j in range(len(data)):
    color = "b"
    if data[j][2] == 1:
        color = "r"
        pass
    pyplot.scatter(data[j][0] , data[j][1] , c=color)
pyplot.scatter(mystery[0] , mystery[1] , c="y")


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

w1 = np.random.randn()
w2 = np.random.randn()
b = np.random.randn()

learning_rate = 0.5

costs = []

for i in range(50000):
    ri = np.random.randint(len(data))
    point = data[ri]
    target = point[2]

    z = w1 * point[0] + w2 * point[1] + b
    pred = sigmoid(z)

    cost = (pred - target) ** 2

    costs.append(cost)

    dcost_dpred = (pred - target) * 2

    dpred_dz = sigmoid(z) * (1-sigmoid(z)) 

    dz_dw1 = point[0]
    dz_dw2 = point[1]
    dz_db = 1


    dcost_dw1 = dcost_dpred * dpred_dz * dz_dw1
    dcost_dw2 = dcost_dpred * dpred_dz * dz_dw2
    dcost_db = dcost_dpred * dpred_dz * dz_db

    w1 = w1 - learning_rate * dcost_dw1
    w2 = w2 - learning_rate * dcost_dw2
    b = b - learning_rate * dcost_db
# plotting error 
pyplot.figure(2)
pyplot.plot(costs)


def predict(x1,x2):
    pred = w1 * data[i][0] + w2 * data[i][1] + b
    prd = sigmoid(pred)
    if prd >= 0.5:
        spk.speak("I Think its red flower")
    else:
        spk.speak("I Think its blue flower")
    print(prd)




for i in range(len(data)):
    pred = w1 * data[i][0] + w2 * data[i][1] + b
    prd = sigmoid(pred)

    print(data[i] , prd)


pr1 = input("Input Feature 1 : ")
pr2 = input("Input Feature 2 : ")


predict(pr1,pr2)

pyplot.show()
