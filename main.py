import json
import sys
import random

class Tank:
	def __init__(self, pos_x, pos_y, can_shoot, direction):
		self.pos_x = pos_x;
		self.pos_y = pos_y;
		self.can_shoot = can_shoot;
		self.direction = direction;
		
class Wall:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		
class Bullet:
	def __init__(self, x, y, dx, dy):
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy

while True:
	state = json.loads(input())
	
	# Parsing
	width = state.map.width
	height = state.map.height
	
	player = Tank(state.player.x, state.player.y, state.player.canShoot, None) 
	ennemies = []
	walls = []
	my_bullets = []
	opps_bullets = []
	
	for ennemy in state.opponents:
		ennemies.append(Tank(ennemy.x, ennemy.y, None, ennemy.direction))
		
	for wall in state.walls:
		walls.append(Tank(wall.x, wall.y, wall.width, wall.height))
		
	for bullet in state.bullets.fromPlayer:
		my_bullets.append(Tank(bullet.x, bullet.y, bullet.dx, bullet.dy))
		
	for bullet in state.bullets.fromOpponents:
		opps_bullets.append(Tank(bullet.x, bullet.y, bullet.dx, bullet.dy))
	
	
	
	# To Output
	#{
	#	"direction": "RIGHT",
	#	"newBullet": {
	#		"dx": 0.5,
	#		"dy": 3
	#}
		
	print(json.dumps({
		"direction": direction,
		"newBullet": newBullet
	}))
	sys.stdout.flush()