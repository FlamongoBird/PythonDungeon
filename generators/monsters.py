from classes import weapon, armor
import random
from code import util, terminal, map
from battle import battle



# gen monster

class Monster():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.dead = False

	def move(self, loc, dungeon, player_loc, player):
		"""If the player is in range move"""

		if self.id == 'S' and player.character == 'skeleton':
			return

		# check if player is in monsters range
		if self.y-self.range <= loc[0] <= self.y+self.range and self.x-self.range <= loc[1] <= self.x+self.range:
			x = 0
			y = 0

			# if the y axis is same as the players
			if self.y == loc[0]:
				# move x
				if self.x < loc[1]:
					x = 1
				elif self.x > loc[1]:
					x = -1
			# else move y up or down
			elif self.y < loc[0]:
				y = 1
			elif self.y > loc[0]:
				y = -1

			# if the monsters is blocked
			if dungeon[self.y+y][self.x+x] in ['#', '@', '.', '|', '-', '+', 'S', 't', '*', 'W', "G", "T", "O", "g"]:
				if y == 0:
					x = 0
					# if the x axis is blocked, move the y axis
					if self.y > loc[1]:
						y = 1
					elif self.y < loc[1]:
						 y = -1
				# if the y axis is blocked, move the x axis
				elif x == 0:
					y = 0
					if self.x < loc[0]:
						x = 1
					elif self.x > loc[0]:
						x = -1

			if dungeon[self.y+y][self.x+x] not in ['#', '@', '.', '|', '-', '+', 'S', 't', '*', 'W', "G", "T", "O", "g"]:
				dungeon[self.y][self.x] = " "
				self.y += y
				self.x += x
				dungeon[self.y][self.x] = self.id

			if self.y == player_loc[0] and self.x == player_loc[1]:
				battle.fight(player, [self])



class Skeleton(Monster):
	def __init__(self):
		super().__init__()
		self.weapon = weapon.Weapon(
			random.choice(['sword', 'rusted sword']),
			random.randint(1, 3), 
			random.randint(1, 3), 
			random.randint(1, 3),
		)
		self.armor = armor.Armor(
			random.choice(['chain mail', 'rusted chain mail']),
			random.randint(1, 3),
		)

		self.id = 'S'
		self.name = 'Skeleton'

		self.life = random.randint(50, 100)
		self.range = 10
		self.min_depth = 0
		self.xp = 1


class Goblin(Monster):
	def __init__(self):
		super().__init__()
		self.weapon = weapon.Weapon(
			random.choice(['sword', 'rusted sword', 'mace']),
			random.randint(2, 5), 
			random.randint(2, 5), 
			random.randint(1, 8),
		)
		self.armor = armor.Armor(
			random.choice(['chain mail', 'rusted chain mail']),
			random.randint(1, 3),
		)

		self.id = 'g'
		self.name = 'Goblin'

		self.life = random.randint(75, 150)
		self.range = 15
		self.min_depth = 5
		self.xp = 3


class Orc(Monster):
	def __init__(self):
		super().__init__()
		self.weapon = weapon.Weapon(
			random.choice(['mace', 'war hammer', 'morning star', 'broadsword']),
			random.randint(4, 8), 
			random.randint(4, 5), 
			random.randint(5, 8),
		)
		self.armor = armor.Armor(
			'orc armor',
			random.randint(6, 6),
		)

		self.id = 'O'
		self.name = 'Orc'

		self.life = random.randint(180, 300)
		self.range = 6
		self.min_depth = 10
		self.xp = 5


class CaveTroll(Monster):
	def __init__(self):
		super().__init__()
		self.weapon = weapon.Weapon(
			random.choice(['war hammer', 'mace', 'stone club', 'wooden club']),
			random.randint(4, 8), 
			random.randint(4, 5), 
			random.randint(10, 10),
		)
		self.armor = armor.Armor(
			'Troll Skin',
			random.randint(1, 1),
		)

		self.id = 'T'
		self.name = 'Cave Troll'

		self.life = random.randint(800, 1200)
		self.range = 3
		self.min_depth = 20
		self.xp = 12


class Wyber(Monster):
	def __init__(self):
		super().__init__()
		self.weapon = weapon.Weapon(
			'Wyber Staff',
			random.randint(10, 10), 
			random.randint(3, 6), 
			random.randint(2, 8),
		)
		self.armor = armor.Armor(
			'Chainmail',
			random.randint(3, 8),
		)

		self.id = 'W'
		self.name = 'Wyber'

		self.life = random.randint(100, 130)
		self.range = 20
		self.min_depth = 22
		self.xp = 20


class Ghoul(Monster):
	def __init__(self):
		super().__init__()
		self.weapon = weapon.Weapon(
			"Ghoul's Voulge",
			random.randint(9, 10), 
			random.randint(9, 10), 
			random.randint(9, 10),
		)
		self.armor = armor.Armor(
			"Ghoul's Skin",
			random.randint(1, 1),
		)

		self.id = 'G'
		self.name = "Ghoul"

		self.life = random.randint(150, 300)
		self.range = 14
		self.min_depth = 30
		self.xp = 30


class Enslaver(Monster):
	def __init__(self):
		super().__init__()
		self.weapon = weapon.Weapon(
			"Mancatcher",
			12, 
			15, 
			10,
		)
		self.armor = armor.Armor(
			"Enchanted Chainmail",
			8,
		)

		self.id = 'E'
		self.name = "The Enslaver"

		self.life = 1000
		self.range = 100 # he will attack from the oder side of de map
		self.min_depth = 500 # basically he doesn't spawn automatically
		self.xp = 800


class Thorgan(Monster):
	def __init__(self):
		super().__init__()
		self.weapon = weapon.Weapon(
			random.choice(["Thorgan Spear", "Thorgan Hammer", "Thorgan Sword", "Thorgan War Axe"]),
			random.randint(9, 10), 
			random.randint(10, 11), 
			random.randint(15, 20),
		)
		self.armor = armor.Armor(
			"Thorgan War Armor",
			10,
		)

		self.id = 't'
		self.name = "Thorgan"

		self.life = random.randint(500, 1000)
		self.range = 8
		self.min_depth = 90
		self.xp = 150

class ZombieGoblin(Monster):
	def __init__(self):
		super().__init__()
		self.weapon = weapon.Weapon(
			random.choice(['sword', 'rusted sword', 'mace']),
			random.randint(3, 6), 
			random.randint(2, 5), 
			random.randint(1, 8),
		)
		self.armor = armor.Armor(
			random.choice(['chain mail', 'rusted chain mail']),
			random.randint(1, 3),
		)

		self.id = 'Z'
		self.name = 'Zombie Goblin'

		self.life = random.randint(200, 350)
		self.range = 12
		self.min_depth = 20
		self.xp = 6


class CrazedKnight(Monster):
	def __init__(self):
		super().__init__()
		self.weapon = weapon.Weapon(
			random.choice(["Kakavian Shortsword", "Kakavian Longsword", "Kakavian Battleaxe"]),
			random.randint(5, 8), 
			random.randint(3, 6), 
			random.randint(5, 8),
		)
		self.armor = armor.Armor(
			"Kakavian Iron Armor",
			7,
		)

		self.id = 'C'
		self.name = "Crazed Knight"

		self.life = 140
		self.range = 20
		self.min_depth = 35
		self.xp = 25


class Fishman(Monster):
	def __init__(self):
		super().__init__()
		self.weapon = weapon.Weapon(
			"Jagged Dagger",
			random.randint(7, 8), 
			random.randint(9, 10), 
			5,
		)
		self.armor = armor.Armor(
			"Scale Armor",
			10,
		)

		self.id = 'F'
		self.name = "Fishman"

		self.life = random.randint(200, 250)
		self.range = 10
		self.min_depth = 65
		self.xp = 50


class Villager(Monster):
	def __init__(self):
		super().__init__()
		self.weapon = weapon.Weapon(
			"Pitchfork",
			2, 
			2, 
			2,
		)
		self.armor = armor.Armor(
			"Villager Robes",
			1,
		)

		self.id = 'V'
		self.name = "Crazed Villager"

		self.life = 100
		self.range = 0 # Will not attack you
		self.min_depth = 0
		self.xp = 0


class Villager(Monster):
	def __init__(self):
		super().__init__()
		self.weapon = weapon.Weapon(
			"Pitchfork",
			2, 
			2, 
			2,
		)
		self.armor = armor.Armor(
			"Villager Robes",
			1,
		)

		self.id = 'V'
		self.name = "Crazed Villager"

		self.life = 100
		self.range = 0 # Will not attack you
		self.min_depth = 0
		self.xp = 0

	

monsters = [Skeleton(), Goblin(), Orc(), CaveTroll(), Wyber(), Ghoul(), Thorgan(), ZombieGoblin(), CrazedKnight(), Fishman(), Villager()]
		

def gen_random(dungeon_level):
	monster_ids = []

	for monster in monsters:
		if dungeon_level >= monster.min_depth:
			monster_ids.append(monster.id)

	m = random.choice(monster_ids)
	return get_monster(m)


def get_enemies_from_list(enemies):
	monsters = []

	for e in enemies:
		monster = get_monster(e['id'])
		monster.y = e["y"]
		monster.x = e["x"]
		monsters.append(monster)

	return monsters

def enemies_to_strings(enemies):
	return [{"id":enemy.id, "x":enemy.x, "y":enemy.y} for enemy in enemies]
	


def get_monster(symbol):
	if symbol == 'S':
		return Skeleton()
	elif symbol == 'g':
		return Goblin()
	elif symbol == 'O':
		return Orc()
	elif symbol == 'T':
		return CaveTroll()
	elif symbol == 'W':
		return Wyber()
	elif symbol == 'G':
		return Ghoul()
	elif symbol == 't':
		return Thorgan()
	elif symbol == "Z":
		return ZombieGoblin()
	elif symbol == "C":
		return CrazedKnight()
	elif symbol == "F":
		return Fishman()
	elif symbol == "V":
		return Villager()

	