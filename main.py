import pygame, sys
from calc import getDistanceAndAngle, addPos
from code import getCode

pygame.init()

#Show map
image = pygame.image.load("map.jpg")
witdhImage, heightImage = image.get_size()
scale = heightImage / witdhImage

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

