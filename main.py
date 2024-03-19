import json
import sys
import random
from math import sqrt

test_data = {
	"map": {
		"width": 400,
		"height": 200,
		"walls": [{ 
			"x": 20,
			"y": 40,
			"width": 100,
			"height": 100
		}, {
			"x": 320,
			"y": 100,
			"width": 20,
			"height": 50
		}]
	},
	"player": {
		"x": 250,
		"y": 150,
		"canShoot": True
	},
	"opponents": [{ 
		"x": 150,
		"y": 72,
		"direction": "UP"
	}, {
		"x": 300,
		"y": 100,
		"direction": "NONE"
	}],
	"bullets": {
		"fromPlayer": [{ 
			"x": 50,
			"y": 20,
			"dx": 2,
			"dy": 1	
		}],
		"fromOpponents": [{
			"x": 50,
			"y": 40,
			"dx": 2,
			"dy": 1
		}]
	}
}



def distance(x, y, xp, yp ):
	return (sqrt((xp - x)**2 + (yp - y)**2 ))

class Tank:
	def __init__(self, pos_x, pos_y, can_shoot, direction):
		self.x = pos_x;
		self.y = pos_y;
		self.can_shoot = can_shoot;
		self.direction = direction;
		
class Wall:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		
class Bullet:
	def __init__(self, x, y, dx, dy, distance_player):
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.distance_player = distance_player

while True:
	# state = test_data
	state = json.loads(input())
	
	# Parsing
	width = state["map"]["width"]
	height = state["map"]["height"]
	
	player = Tank(state["player"]["x"], state["player"]["y"], state["player"]["canShoot"], None) 
	ennemies = []
	walls = []
	my_bullets = []
	opps_bullets = []
	danger_zone = []

	for ennemy in state["opponents"]:
		ennemies.append(Tank(ennemy["x"], ennemy["y"], None, ennemy["direction"]))
		
	for wall in state["map"]["walls"]:
		walls.append(Wall(wall["x"], wall["y"], wall["width"], wall["height"]))
		
	for bullet in state["bullets"]["fromPlayer"]:
		my_bullets.append(Bullet(bullet["x"], bullet["y"], bullet["dx"], bullet["dy"], None))
		
	for bullet in state["bullets"]["fromOpponents"]:
		opps_bullets.append(Bullet(bullet["x"], bullet["y"], bullet["dx"], bullet["dy"], None))
	
	# Algo
	for bullet in opps_bullets:
		danger_zone.append(Bullet(bullet.x, bullet.y,bullet.dx, bullet.dy, distance(bullet.x, bullet.y, player.x, player.y)))
		for i in range (0, 200):
			danger_zone.append(Bullet(bullet.x + bullet.dx * i, bullet.y + bullet.dy * i,bullet.dx, bullet.dy, distance(bullet.x + bullet.dx * i, bullet.y + bullet.dy * i, player.x, player.y)))
	
	sorted_danger_zone = sorted(danger_zone, key=lambda x: x.distance_player, reverse=True)
	
	direction = "NONE"
	if (len(sorted_danger_zone) != 0):
		if (sorted_danger_zone[0].distance_player <= 8):
			direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

	# To Output
	#{
	#	"direction": "RIGHT",
	#	"newBullet": {
	#		"dx": 0.5,
	#		"dy": 3
	#}
		
	print(json.dumps({
		"direction": direction,
		"newBullet": {}
	}))
	sys.stdout.flush()
