#!/usr/bin/python 
from pygame import *
import random
import os, sys
import pygame
from pygame.locals import *
import math

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', wav
        raise SystemExit, message
    return sound

class Sprite:
	def __init__(self, xpos, ypos, filename):
		self.x = xpos
		self.y = ypos
		self.x_vel = 0
		self.y_vel = 0
		self.bitmap = image.load(filename)
		self.bitmap.set_colorkey((0,0,0))
 	def speed(self, x_vel, y_vel):
		self.x_vel = x_vel
		self.y_vel = y_vel
	def set_position(self, xpos, ypos):
		self.x = xpos
		self.y = ypos
	def render(self):
		self.x += self.x_vel
		self.y += self.y_vel
		screen.blit(self.bitmap, (self.x, self.y))
   


def Intersect(s1_x, s1_y, s2_x, s2_y):
	if (s1_x > s2_x - 32) and (s1_x < s2_x + 32) and (s1_y > s2_y - 32) and (s1_y < s2_y + 32):
		return 1
	else:
		return 0

def PlaySound(file):
	if soundmute == 0:
		file.play()
	return



init()
screen = display.set_mode((1024,768))
key.set_repeat(1, 5)
display.set_caption('PyInvaders')
backdrop = image.load('data/backdrop.bmp')


enemies = []
ourmissiles = []

x = 0
kill = 0
missileno = 1
score = 0
lives = 3
soundmute = 0
LEFT_MAX = 800
DOWN_MAX = 600

for count in range(5):
	ourmissiles.append(Sprite(0,480, 'data/heromissile.bmp'))

for count in range(5):
	enemies.append(Sprite(50 * x + 50, 50, 'data/baddie.bmp'))
	x += 1

hero = Sprite(800, 600, 'data/hero.bmp')
ourmissile = Sprite(0, 480, 'data/heromissile.bmp')
enemymissile = Sprite(0, 480, 'data/baddiemissile.bmp')
alien = Sprite(640,480,'data/alien.bmp')
soundon = Sprite(600,5, 'data/soundon.bmp')
soundoff = Sprite(600,5, 'data/soundoff.bmp')

scorefont = font.Font(None, 30)
livesfont = font.Font(None, 30)
speedfont = font.Font(None, 15)

zapsound = load_sound('ZAP3.WAV')
explodesound = load_sound('BOOM1.WAV')
warpsound = load_sound('WARP.WAV')

quit = 0
enemyspeed = 3
hero.speed(-1,-1)

while quit == 0:
	screen.blit(backdrop, (0, 0))
	scoretext = scorefont.render('Score: ' +str(score), True, (0,255,0),(0,0,0))
	screen.blit(scoretext,(900,5))
	livestext = livesfont.render('Lives: ' +str(lives), True, (0,255,0),(0,0,0))
	screen.blit(livestext,(900,25))
	ac_speed = math.sqrt((hero.x_vel**2)+(hero.y_vel**2))
	ac_heading =  math.degrees(math.atan2(hero.x_vel,-hero.y_vel))
	ac_heading = -((ac_heading + 360) % 360)
	velocity = "%s | %s" % (ac_speed,-ac_heading)
	speed = "(%i,%i)" % (-hero.x_vel,-hero.y_vel)
	speedtext = speedfont.render(velocity, True, (0,255,0),(0,0,0))
	screen.blit(speedtext,(900,45))

	if soundmute:
		soundoff.render()
	else:
		soundon.render() 


	#for count in range(len(enemies)):
		#enemies[count].x += + enemyspeed
		#enemies[count].render()

	#if enemies[len(enemies)-1].x > 490:

		#enemyspeed = -3
		#for count in range(len(enemies)):
			#enemies[count].y += 5

	#if enemies[0].x < 10:
		#enemyspeed = 3
		#for count in range(len(enemies)):
			#enemies[count].y += 5

	if alien.y < LEFT_MAX and alien.y > 0:
		alien.render()

	if alien.x >= 1024 and len(enemies) > 0:
		aliendecision = random.randint(0,9999)
		print "Alien Decision: ", aliendecision
		if aliendecision < 100:
			print "Alien Released"
			alien.x = 0
			alien.y = 20
			alien.speed(2,1)
		else:
			print "Alien Not Released"


	for count in range(0, len(ourmissiles)):
		if ourmissiles[count].y < 479 and ourmissiles[count].y > 0:
			ourmissiles[count].render()
			ourmissiles[count].y -= 5		
		if Intersect(ourmissiles[count].x,ourmissiles[count].y,enemymissile.x, enemymissile.y):
			ourmissiles[count].x = 0
			ourmissiles[count].y = 480
			enemymissile.x = enemies[random.randint(0, len(enemies) - 1)].x
			enemymissile.y = enemies[0].y
			score += 5
			#explodesound.play()			
			PlaySound(explodesound)
		if Intersect(alien.x,alien.y,hero.x,hero.y):
			print "Alien Destroyed"
			score += 20
			hero.x = 600
			hero.y = 600
			alien.x = 2000
			alien.y = 2000
			PlaySound(explodesound)
		for count2 in range(0, len(enemies)):
			if Intersect(ourmissiles[count].x, ourmissiles[count].y, enemies[count2].x, enemies[count2].y):
				#explodesound.play()			
				PlaySound(explodesound)
				del enemies[count2]
				score += 10
				ourmissiles[count].x = 0
				ourmissiles[count].y = 480
				break

	if len(enemies) == 0:
		quit = 1

	if missileno == 0:
		nextmissile = 0
	else:
		nextmissile = missileno % len(ourmissiles)

	

	for ourevent in event.get():
		if ourevent.type == QUIT:
			quit = 2
		if ourevent.type == KEYDOWN:
			if ourevent.key == K_SPACE:
				ourmissiles[nextmissile].x = hero.x
				ourmissiles[nextmissile].y = hero.y
				missileno += 1
				#zapsound.play()
				PlaySound(zapsound)
			if ourevent.key == K_LEFT:
				hero.speed(hero.x_vel-1,hero.y_vel)
			if ourevent.key == K_RIGHT:
				hero.speed(hero.x_vel+1,hero.y_vel)
			if ourevent.key == K_UP:
				hero.speed(hero.x_vel,hero.y_vel-1)
			if ourevent.key == K_DOWN:
				hero.speed(hero.x_vel,hero.y_vel+1)
			if ourevent.key == K_q:
				quit = 2
			if ourevent.key == K_s:
				if soundmute == 1:
					soundmute = 0
				else:
					soundmute = 1



	enemymissile.render()
	enemymissile.y += 5

	hero.render()

	display.update()
	time.delay(100)

if quit == 1:
	PlaySound(warpsound)
	while hero.y > 0:
		screen.blit(backdrop, (0, 0))
		scoretext = scorefont.render('You Scored: ' +str(score), True, (0,255,0),(0,0,0))
		screen.blit(scoretext,(200,200))
		livestext = livesfont.render('Lives Remaining: ' +str(lives), True, (0,255,0),(0,0,0))
		screen.blit(livestext,(200,240))
		keyfont = font.Font(None, 30)
		keytext = keyfont.render('... Press Any Key to Continue ...', True, (0,255,0),(0,0,0))
		screen.blit(keytext,(200,280))
		#screen.blit(backdrop, (0, 0))	
		hero.y -= 5
		if hero.x < 320:
			hero.x += 10
		if hero.x > 320:
			hero.x -= 10
		hero.render()
		display.update()
		time.delay(5)
	del hero
	display.update()
else:
	screen.blit(backdrop, (0, 0))
	scoretext = scorefont.render('Game Over!!', True, (0,255,0),(0,0,0))
	screen.blit(scoretext,(200,200))
	display.update()



