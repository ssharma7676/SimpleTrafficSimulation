import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from itertools import count


global numCars
numCars = 20
maxCarSpeed = 90  # 90 mph is the max car speed allowed on this road
minCarSpeed = 20
minDistBetweenCars = 0.5
speedLimit = 60  # 60 mph is the speed limit on this road

carSpeed = []
carLoc = []
yLoc = []
for i in range(numCars):
    carSpeed.append(speedLimit)
    carLoc.append(-i * minDistBetweenCars)
    yLoc.append(50)

fig1, ax = plt.subplots()
fig2, bx = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 100)
bx.set_ylim(0, 90)
ax.set_xlabel('Location')
ax.set_title('Straight Road')
bx.set_xlabel('Time')
bx.set_ylabel('Average Speed')
bx.set_title("Change in Average Speed Over Time")

index = count()
time = [0]
avgSpeed = [0]


def artists():
    ax.plot(carLoc, yLoc, 'bo')
    bx.plot(time, avgSpeed, 'm')
    return


def update(frame):
    ax.clear()

    ax.set_xlim(carLoc[numCars - 1] - 2, carLoc[0] + 2)
    ax.set_ylim(0, 100)
    bx.set_ylim(0, 90)
    ax.set_xlabel('Location')
    ax.set_title('Straight Road')
    bx.set_xlabel('Time')
    bx.set_ylabel('Average Speed')
    bx.set_title("Change in Average Speed Over Time")

    deltaT = 5

    sumSpeed = 0
    for i in range(numCars):
        sumSpeed += carSpeed[i]
    time.append(next(index))
    avgSpeed.append(sumSpeed / numCars)

    for i in range(numCars):

        """
        1. changeInLoc of each car is given by s * t
        2. newPos of each car is given by ccarLoc[i] + changeInLoc
        3. for all cars but the first car, distToCarAhead = carLoc[i-1] - newPos
        4. if the newPos + minDistBetweenCars < carLoc[i-1], increase car speed by random int from 1 to 5, change 
           changeInLoc and newPos
        5. while the newPos + minDistBetweenCars > carLoc[i-1], decrease car speed by 1 and keep changing changeInLov 
           and newPos
        6. return newPos
        """

        changeInLoc = carSpeed[i] * (deltaT / 3600)
        newPos = carLoc[i] + changeInLoc

        if i > 0:
            if newPos + minDistBetweenCars < carLoc[i - 1]:
                carSpeed[i] += random.randint(-20, 20)
                changeInLoc = carSpeed[i] * (deltaT / 3600)
                newPos = carLoc[i] + changeInLoc

            while newPos + minDistBetweenCars > carLoc[i - 1]:
                carSpeed[i] -= 1
                changeInLoc = carSpeed[i] * (deltaT / 3600)
                newPos = carLoc[i] + changeInLoc
        else:
            carSpeed[i] += random.randint(-20, 20)
            changeInLoc = carSpeed[i] * (deltaT / 3600)
            newPos = carLoc[i] + changeInLoc

        if carSpeed[i] > maxCarSpeed:
            carSpeed[i] = maxCarSpeed
            changeInLoc = carSpeed[i] * (deltaT / 3600)
            newPos = carLoc[i] + changeInLoc
        if carSpeed[i] < minCarSpeed:
            carSpeed[i] = minCarSpeed
            changeInLoc = carSpeed[i] * (deltaT / 3600)
            newPos = carLoc[i] + changeInLoc

        carLoc[i] = newPos

    ax.plot(carLoc, yLoc, 'bo')

    for i in range(numCars):
        ax.annotate(i, (carLoc[i] - 0.04, yLoc[i] - 0.45), color='w', size=5)

cars = FuncAnimation(fig1, update, frames=1, interval=10, init_func=artists)
graph = FuncAnimation(fig2, update, frames=1, interval=10, init_func=artists)


plt.show()