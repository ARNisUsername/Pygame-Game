import pygame
import random
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("First game")

x = 50
y = 50
width = 20
height = 60
vel = 10
straight = True

x1 = 100
y1 = 100
width1 = 20
height1 = 60
straight1 = True

def not_max():

    global x
    global y
    global vel
    global width
    global height
    
    if x >= (500 - height/2) - width - vel:
        return False
    if x <= vel:
        return False
    if y <= vel:
        return False
    if y >= (500 - width/2) - height - vel:
        return False
    return True

def is_equal(x, y, x1, y1, straight, straight1):

    global width1
    global height1

    if x == x1 and y == y1 and straight == straight1:
        return True
    return False

def set_text(string, coord1, coord2, fontSi):

    font = pygame.font.Font('freesansbold.ttf', fontSi) 
    text = font.render(string, True, (255, 0, 0), (0, 0, 255))
    textRect = text.get_rect()
    textRect.center = (coord1, coord2)
    return (text, textRect)

def make_divisible(ran1, ran2):

    theRandom = random.randint(ran1, ran2)
    randomStr = str(theRandom)
    if theRandom % 10 != 0:
        randomStr = str(theRandom)[0]
        for i in range(len(str(theRandom)) - 1):
            randomStr += "0"
    return int(randomStr)

score = "Your score: 0"
scoreNum = 0
currentTime = "25 Seconds Left"
timeNum = 25
originalTime = 25
run = True
color = (255, 0, 0)
timedDel = 0
hasDone = False
shouldSpace = True

while run:

    if timedDel == 0:
        shouldSpace = True
        
    pygame.time.delay(75)
    timedDel += 75

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 500 - height - vel:
        y += vel
    if keys[pygame.K_SPACE] and not_max() and shouldSpace == True:
        shouldSpace = False
        widthStored = width
        heightStored = height
        width = heightStored
        height = widthStored
        if straight == True:
            straight = False
        elif straight == False:
            straight = True
    
    
    win.fill((0, 0, 0))

    pygame.draw.rect(win, color, (x, y, width, height))
    pygame.draw.rect(win, (0, 0, 255), (x1, y1, width1, height1))

    setText = set_text(score, 250, 20, 32)
    win.blit(setText[0], setText[1])
    pygame.display.update()

    if is_equal(x, y, x1, y1, straight, straight1):
        
        hasDone = True
        if originalTime > 3:
            originalTime = int(originalTime / 1.2)
        timeNum = originalTime + 1
        scoreNum += 1
        score = "Your score: {}".format(scoreNum)
        x1 = make_divisible(10, 350)
        y1 = make_divisible(35, 400)
        
        if random.randint(1, 2) == 2:
            widthStored = width1
            heightStored = height1
            width1 = heightStored
            height1 = widthStored
            if straight1 == True:
                straight1 = False
            elif straight1 == False:
                straight1 = True
        
    pygame.display.update()

    timeText = set_text(currentTime, 360, 460, 32)
    win.blit(timeText[0], timeText[1])
    pygame.display.update()
    
    if timeNum != 0 and timedDel >= 1000:
        timeNum -= 1
        currentTime = "{} Seconds Left".format(timeNum)
        timedDel = 0
        timeText = set_text(currentTime, 360, 460, 32)
        win.blit(timeText[0], timeText[1])
        pygame.display.update()
        
    elif timeNum == 0 and hasDone == False:
        
        pygame.time.delay(500)
        win.fill((0, 0, 0))
        youLost = set_text("You Lost Lmao", 250, 250, 60)
        win.blit(youLost[0], youLost[1])
        pygame.display.update()
        
        yourScoreStr = "Score: {}".format(scoreNum)
        endScore = set_text(yourScoreStr, 350, 350, 25)
        win.blit(endScore[0], endScore[1])
        pygame.display.update(
            )
        runAgain = True
        while runAgain:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runAgain = False
                    run = False
        

    hasDone = False

pygame.quit()
