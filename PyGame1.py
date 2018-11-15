import pygame
from pygame.locals import *
import time
import random
displayWidth=800
displayHeight=600
FPS=100
increase=3
pygame.init()
gameDisplay=pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("mario")
randAppleX=round(random.randrange(0,(displayWidth-10)/10))*10
randAppleY=round(random.randrange(0,(displayHeight-10)/10))*10
font=pygame.font.SysFont(None,50)
def snake(snakeList):
	for XnY in snakeList:
		pygame.draw.rect(gameDisplay,(0,0,0),[XnY[0],XnY[1],10,10])
def massegeToScreen(msg,color):
	screenText=font.render(msg,True,color)
	gameDisplay.blit(screenText,[0,250])
clk=pygame.time.Clock()
#--------------------------------------------------------
def gameLoop():
	gameExit=False
	gameOver=False
	x=displayWidth/2
	y=displayHeight/2
	snakeList=[]
	snakeLength=1
	xch=0
	ych=0
	enUp=True
	enDown=True
	enRight=True
	enLeft=True
	Apple=10
	while not gameExit:
		while gameOver==True:
			gameDisplay.fill((255,255,255))
			massegeToScreen("Game Over , press C to play again and Q to quit",(0,0,0))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					gameExit=True
					gameOver=False
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_q:	
						gameExit=True
						gameOver=False
					if event.key==pygame.K_c:
						print("iam again")
						gameLoop()
		for event in pygame.event.get():
			global event
			if event.type == pygame.QUIT:
				print("Exit")
				gameExit=True
	        if event.type == pygame.KEYDOWN:
	        	if event.key== K_LEFT:
	        		xch=-increase
	        		ych=0
	    		elif event.key== K_RIGHT: 
	        		xch=increase
	        		ych=0
	        	elif event.key== K_UP:
	        		ych=-increase
	        		xch=0
	        	elif event.key== K_DOWN: 
	        		ych=increase
	        		xch=0  
	        if x>displayWidth-10 or x<0 or y>displayHeight-10 or y<0:
	        	gameOver=True
	        
	        x+=xch
	        y+=ych	
		
		snakeHead=[]
		snakeHead.append(x)
		snakeHead.append(y)
		snakeList.append(snakeHead)
		if len(snakeList)>snakeLength:
			del snakeList[0]
		for eachSegment in snakeList[:-1]:
			if eachSegment==snakeHead:
	    		#time.sleep(2)
				gameOver=True			
		gameDisplay.fill((255,155,55))
		pygame.draw.rect(gameDisplay,(255,0,0),[randAppleX,randAppleY,Apple,Apple])
		snake(snakeList)
		pygame.display.update()
		if x>=randAppleX and x<=randAppleX+Apple or x+10>=randAppleX and x+10<=randAppleX+Apple:
			if y>=randAppleY and y<=randAppleY+Apple or y+10>=randAppleY and y+10<=randAppleY+Apple:
				global randAppleX
				global randAppleY
				randAppleX=round(random.randrange(0,(displayWidth-10)/10))*10
				randAppleY=round(random.randrange(0,(displayHeight-10)/10))*10
				snakeLength+=1
		clk.tick(FPS)
	pygame.quit()
	quit()
#--------------------------------------------------------	
gameLoop()
