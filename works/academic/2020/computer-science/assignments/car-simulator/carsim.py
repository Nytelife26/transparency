import pygame
from pygame.locals import *
import math

def getRPM(speed, gear, rad):
	rpm = (speed * gear * 63360) / ((math.pi * rad * 12 * 2) * 60)
	return rpm if rpm < 5252 else 5252

def accelerate(speed, gear, rpm, hp, rad, mass):
	torque = (hp * 5252) / rpm
	force = torque / rad
	acceleration = (force / mass) * 32.18
	new_speed = speed + acceleration
	return (new_speed, gear, getRPM(new_speed, gear, rad))

def decelerate(speed, gear, rpm, hp, rad, mass):
	torque = (hp * 5252) / rpm
	force = torque / rad
	acceleration = (force / mass) * 32.18
	new_speed = speed - acceleration
	return (new_speed, gear, getRPM(new_speed, gear, rad))
	
def eventHandler(speed, gear, rpm, hp, rad, mass):
	events = pygame.event.get()
	for event in events:
		if event.type == QUIT:
			return QUIT
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		return accelerate(speed, gear, rpm, hp, rad, mass)
	if keys[pygame.K_s]:
		return decelerate(speed, gear, rpm, hp, rad, mass)
	return (speed, gear, rpm)

def main():
	carTypes = {
		"default": {
			"horsepower": 200,
			"tyreRad": 1,
			"mass": 2172,
			"ratios": {
				"1": 14,
				"2": 8.8,
				"3": 5.4,
				"4": 4,
				"5": 2.8,
				"6": 2
			}
		}
	}
	selected_gear = 1
	speed = 0
	rpm = 5252
	hp = carTypes["default"]["horsepower"]
	rad = carTypes["default"]["tyreRad"]
	mass = carTypes["default"]["mass"]
	gear = carTypes["default"]["ratios"][str(selected_gear)]
	
	pygame.init()
	screen = pygame.display.set_mode((540, 540))
	pygame.display.set_caption("Car Simulator v1.0 by Nytelife26")
	
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	
	font = pygame.font.Font(None, 24)
	while True:
		event = eventHandler(speed, gear, rpm, hp, rad, mass)
		if event == QUIT:
			break
		speed, gear, rpm = event
		background.fill((250, 250, 250))
		text = font.render(str(event), 1, (10, 10, 10))
		textpos = text.get_rect()
		textpos.centerx = background.get_rect().centerx
		background.blit(text, textpos)
		screen.blit(background, (0, 0))
		pygame.display.update()

if __name__ == "__main__":
	main()