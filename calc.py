from math import sqrt, degrees, pi, atan2

addPos = lambda pos, posList: posList.append(pos)

def calculateDistance(posA, posB):
    xA, yA = posA
    xB, yB = posB
    return round((sqrt((xB - xA) ** 2 + (yB - yA) ** 2) / 1400) * 236.2, 2)

def getDistance(posList):
    distance = 0
    for index, pos in enumerate(posList):
        if len(posList) == index + 1:
            return distance
        distance += calculateDistance(posList[index], posList[index + 1])

def calculateAngle(posA, posB, posC):
    xA, yA = posA
    xB, yB = posB
    xC, yC = posC

    if xB - xA == 0:
        AB = float("inf")
    else:
        AB = (yB - yA) / (xB - xA)
    if xC - xB == 0:
        return round(degrees(pi / 2))
    
    BC = (yC - yB) / (xC - xB)

    return round(degrees(atan2(AB - BC, 1 + AB * BC)), 2)

def getDistanceAndAngle(posList, distanceList, angleList):
    for index, pos in enumerate(posList):
        if len(posList) == index + 1:
            return
        
        if index == 0:
            distanceList.append(calculateDistance(pos, posList[index + 1]))
            angleList.append(0)
            continue

        distanceList.append(calculateDistance(pos, posList[index + 1]))
        angleList.append(calculateAngle(posList[index - 1],pos, posList[index + 1]))

if __name__ == "__main__":
    print("Loaded calculateDistance")
