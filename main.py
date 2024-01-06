import pygame, sys
from math import sqrt, degrees, pi, atan2

pygame.init()

#Show map
image = pygame.image.load("map.jpg")
witdhImage, heightImage = image.get_size()
scale = heightImage / witdhImage

#Robot
picture = pygame.image.load("robot.jpg")

#Game window
width = 1400
height = width * scale
image = pygame.transform.scale(image, (width, height))
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("WRO bumsdings")

#Variables
drawing = False
cm = 2362 / 10
posList = []
distanceList = []
angleList = []
lastPos = None

#Calc functions
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

#Code functions
def getCode(distanceList, angleList):
    print(f"{distanceList}\n{angleList}")
    for distance, angle in zip(distanceList, angleList):
        if -5 < angle < 5:
            print(f"Strecke({distance})")
        elif 85 < angle < 95:
            print(f"Drehung(1, 0, 0, 90)\nStrecke(0, 0, {distance})")
        elif -95 < angle < -85:
            print(f"Drehung(1, 0, 0, -90)\nStrecke(0, 0, {distance})")
        elif 175 < angle < -175:
            print(f"Strecke(0, 0, -10)")
            if distance < 10:
                return
            print(f"Drehung(1, 0, 0, 180)\nStrecke(0, 0, {distance - 10})")
        else:
            print(f"Drehung(1, 0, 0, {angle})\nStrecke(0, 0, {distance})")

#Program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            getCode(distanceList, angleList)
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                addPos(event.pos, posList)
                lastPos = event.pos

    window.fill((255, 255, 255))
    window.blit(image, (0, 0))

    if len(posList) > 1:
        pygame.draw.lines(window, (255, 0, 0), False, posList, 2)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if not drawing:
            getDistanceAndAngle(posList, distanceList, angleList)
            posList = []
            drawing = True
    else:
        drawing = False

    pygame.display.flip()

