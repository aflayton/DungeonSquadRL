from random import randint

availableTargets = []
inCombat = False
currentRoom = None
numberOfRooms = 3
floorNumber = 1

class Character(object):
	def __init__(self):
		self.hp = 15 #hit points
		self.maxHp = 15
		self.gold = 0
		self.stuff = {}
		self.chooseSkills()
		self.chooseStuff()
	
	def chooseSkills(self):
		i = raw_input("Warrior or Wizard? ").lower()
		if i == "warrior":
			self.warrior = 12
			self.wizard = 8
		elif i == "wizard":
			self.warrior = 8
			self.wizard = 12
		else:
			self.chooseSkills()

	def chooseStuff(self):
		availableStuff = ["Sword","Armor","Heal","Fireball"]
		
		firstStuff = raw_input("What level 10 stuff would you like? " + str(availableStuff) + ": ").capitalize()
		if not (firstStuff in availableStuff):
			print "Invalid input. Try again."
			self.chooseStuff()
		else:
			self.stuff[firstStuff] = 10
			availableStuff.remove(firstStuff)
		
		secondStuff = raw_input("What level 6 stuff would you like? " + str(availableStuff) + ": ").capitalize()
		if not (secondStuff in availableStuff):
			print "Invalid input. Try again."
			self.chooseStuff()
		else:
			self.stuff[secondStuff] = 6

	def attack(self, target):
		if self.stuff.has_key("Sword"):
			dmgDie = self.stuff["Sword"]
		else: #unarmed
			dmgDie = 4

		print "You attack!"
		warriorRoll = randint(1, self.warrior)
		print "Warrior roll = " + str(warriorRoll)
		if warriorRoll >= target.beingHitThreshold:
			dmg = randint(1, dmgDie)
			if target.armor > 0:
				dmg -= randint(1,target.armor)
			target.hp -= dmg
			print "You hit the " + str(target) + " for " + str(dmg) + " damage!"
			print "Target hp: " + str(target.hp)
		else:
			print "You miss."
	
	def heal(self, combatStatus):
		wizardRoll = randint(1,self.wizard)
		print "Wizard roll = " + str(wizardRoll)
		healRoll = randint(1,self.stuff["Heal"])
		if combatStatus:
			if wizardRoll > 4:
				print "You heal yourself for " + str(healRoll) + " hp!"
				self.hp += healRoll
				if self.hp > self.maxHp:
					self.hp = self.maxHp
				print "You now have " + str(self.hp) + " hp!"
			else:
				print "You failed to cast."
		else:
			if wizardRoll > 2:
				print "You heal yourself for " + str(healRoll) + " hp!"
				self.hp += healRoll
				if self.hp > self.maxHp:
					self.hp = self.maxHp
				print "You now have " + str(self.hp) + " hp!"
			else:
				print "You failed to cast."
	
	def fireball(self, target):
		wizardRoll = randint(1,self.wizard)
		print "Wizard roll = " + str(wizardRoll)
		if wizardRoll > 4:
			dmg = randint(1, self.stuff["Fireball"])
			print "You deal " + str(dmg) + " damage to the target!"
			target.hp -= dmg
			print "The " + str(target) + "'s hp is now " + str(target.hp) + "!"
		else:
			print "You failed to cast."
			
	def shop(self):
		bandage = {"Cost": 2,"Description": "Heals D4"}
		salve = {"Cost": 4,"Description": "Heals D6"}
		potion = {"Cost": 8,"Description": "Heals D12"}
		hpUpgrade = {"Cost": 16,"Description": "+1 Max Hp"}
		warriorUpgrade = {"Cost": 32,"Description": "+2 Warrior level"}
		wizardUpgrade = {"Cost": 32,"Description": "+2 Wizard level"}
		stuffUpgrade = {"Cost": 32,"Description": "+2 Stuff level"}
		shopInventory = {"Bandage": bandage, "Salve": salve, "Potion": potion, "Hp Upgrade": hpUpgrade, "Warrior Upgrade": warriorUpgrade, "Wizard Upgrade": wizardUpgrade, "Stuff Upgrade": stuffUpgrade}
		print "You can buy the following items:"
		for k in shopInventory.keys():
			print k + " - " + str(shopInventory[k])
		item = raw_input("What would you like to buy? ").lower()
		if item == "bandage":
			if self.gold >= 2: #2 is the cost
				print "You spend 2 gold."
				self.gold -= 2
				print "You now have " + str(self.gold) + " gold left."
				heal = randint(1,4)
				print "You heal yourself for " + str(heal) + " hp."
				self.hp += heal
				if self.hp > self.maxHp:
					self.hp = self.maxHp
				print "You now have " + str(self.hp) + " hp."
			else:
				print "You can't afford that item."
				self.getInput()
		elif item == "salve":
			if self.gold >= 4:
				print "You spend 4 gold."
				self.gold -= 4
				print "You now have " + str(self.gold) + " gold left."
				heal = randint(1,6)
				print "You heal yourself for " + str(heal) + " hp."
				self.hp += heal
				if self.hp > self.maxHp:
					self.hp = self.maxHp
				print "You now have " + str(self.hp) + " hp."
			else:
				print "You can't afford that item."
				self.getInput()
		elif item == "potion":
			if self.gold >= 8:
				print "You spend 8 gold."
				self.gold -= 8
				print "You now have " + str(self.gold) + " gold left."
				heal = randint(1,12)
				print "You heal yourself for " + str(heal) + " hp."
				self.hp += heal
				if self.hp > self.maxHp:
					self.hp = self.maxHp
				print "You now have " + str(self.hp) + " hp."
			else:
				print "You can't afford that item."
				self.getInput()
		elif item == "hp upgrade":
			if self.gold >= 16:
				print "You spend 16 gold."
				self.gold -= 16
				print "You now have " + str(self.gold) + " gold left."
				self.maxHp += 1
				print "You now have " + str(self.maxHp) + " max hp."
			else:
				print "You can't afford that item."
				self.getInput()
		elif item == "warrior upgrade":
			if self.gold >= 32:
				print "You spend 32 gold."
				self.gold -= 32
				print "You now have " + str(self.gold) + " gold left."
				self.warrior += 2
				print "You now have a " + str(self.warrior) + " warrior skill level."
			else:
				print "You can't afford that item."
				self.getInput()
		elif item == "wizard upgrade":
			if self.gold >= 32:
				print "You spend 32 gold."
				self.gold -= 32
				print "You now have " + str(self.gold) + " gold left."
				self.wizard += 2
				print "You now have a " + str(self.wizard) + " wizard skill level."
			else:
				print "You can't afford that item."
				self.getInput()
		elif item == "stuff upgrade":
			s = raw_input("What stuff would you like to upgrade? ").capitalize()
			if s in self.stuff.keys():
				if self.gold >= 32:
					print "You spend 32 gold."
					self.gold -= 32
					print "You now have " + str(self.gold) + " gold left."
					self.stuff[s] += 2
					print "You now have a " + str(self.stuff[s]) + " level " + s + "."
				else:
					print "You can't afford that item."
			else:
				print "You don't have that stuff."
				self.getInput()
		else:
			print "Invalid input. Try again."
			self.getInput()

	def getInput(self):
		global forever
		global floor
		global availableTargets
		global inCombat
		global currentRoom
		global floorCleared
		
		i = raw_input("What will you do next? ").lower()
		if i == "quit":
			inCombat = False
			floorCleared = True
			forever = False
		elif i[:5] == "enter":
			if not inCombat:
				room = i[6:].capitalize()
				if floor.rooms.has_key(room):
					print "You enter " + room + "!"
					currentRoom = floor.rooms[room]
					availableTargets += currentRoom.monsters.keys()
					inCombat = True
				else:
					print "Invalid input. Try again."
					self.getInput()
			else:
				print "You can't do that while in combat."
				self.getInput()
		elif i[:6] == "attack":
			if inCombat:
				target = i[7:].capitalize()
				if target in availableTargets:
					self.attack(currentRoom.monsters[target])
				else:
					print "Invalid Input. Try again."
					self.getInput()
			else:
				print "You aren't in combat."
				self.getInput()
		elif i == "heal":
			if self.stuff.has_key("Heal"):
				self.heal(inCombat)
			else:
				print "You don't have that spell."
				self.getInput()
		elif i[:8] == "fireball":
			if inCombat:
				if self.stuff.has_key("Fireball"):
					target = i[9:].capitalize()
					if target in availableTargets:
						self.fireball(currentRoom.monsters[target])
					else:
						print "Invalid input. Try again."
						self.getInput()
				else:
					print "You don't have that spell."
					self.getInput()
			else:
				print "You aren't in combat."
				self.getInput()
		elif i == "shop":
			if not inCombat:
				self.shop()
			else:
				print "You can't do that while in combat."
				self.getInput()
		else:
			print "Invalid Input. Try again."
			self.getInput()
			
	def delete(self):
		global floorCleared
		global forever
		print "You died."
		inCombat = False
		floorCleared = True
		forever = False
	
class Floor(object):
	rooms = {}
	def __init__(self):
		global floorNumber
		global numberOfRooms
		self.name = "Floor" + str(floorNumber)
		print "You enter " + self.name + " of the Dungeon."
		for i in range(1, numberOfRooms):
			roomName = "Room"+str(i)
			self.rooms[roomName] = Room()
			self.rooms[roomName].name = roomName
	
	def delete(self):
		global numberOfRooms
		global floorNumber
		print "You have cleared " + self.name + " of the Dungeon."
		numberOfRooms += 2
		floorNumber += 1
			
class Room(object):
	def __init__(self):
		global floorNumber
		self.monsters = {}
		monsterCodes = [[1,2],[3,4,5],[6,7,8],[9,10,11],[12]]
		maxRow = 4
		for i in range(1, randint(2,5)):
			if floorNumber <= maxRow:
				randomRow = randint(0,floorNumber-1)
			else:
				randomRow = randint(0,maxRow)
			
			if randomRow == 0:
				maxColumn = 1
			elif 1 <= randomRow <= 3:
				maxColumn = 2
			else:
				maxColumn = 0
			randomColumn = randint(0,maxColumn)
		
			monsterName = "Monster"+str(i)
			
			rmc = monsterCodes[randomRow][randomColumn] #rmc = random monster code
			if rmc == 1:
				randomMonster = Rat()
			elif rmc == 2:
				randomMonster = Bat()
			elif rmc == 3:
				randomMonster = GiantRat()
			elif rmc == 4:
				randomMonster = Wolf()
			elif rmc == 5:
				randomMonster = Goblin()
			elif rmc == 6:
				randomMonster = Orc()
			elif rmc == 7:
				randomMonster = Skeleton()
			elif rmc == 8:
				randomMonster = GiantSpider()
			elif rmc == 9:
				randomMonster = Giant()
			elif rmc == 10:
				randomMonster = Troll()
			elif rmc == 11:
				randomMonster = BabyDragon()
			else: #(rmc == 12)
				randomMonster = Dragon()
			
			self.monsters[monsterName] = randomMonster
			self.monsters[monsterName].id = monsterName
			
	def __str__(self):
		return self.name

	def delete(self):
		global inCombat
		global currentRoom
		print "You have cleared " + self.name + "!"
		inCombat = False
		currentRoom = None
		
	def __getitem__(self, key):
		return self.monsters[key]
		
class Monster(object):
	hitThreshold = 4 #the number a monster has to roll to hit a player
	armor = 0
	
	def attack(self, target):
		print self.name + " attacks!"
		hitRoll = randint(1, self.hitDie)
		if hitRoll >= self.hitThreshold:
			dmg = randint(1, self.dmgDie)
			if target.stuff.has_key("Armor"):
				dmg -= randint(1, target.stuff["Armor"])
				if dmg < 0:
					dmg = 0
			print "The " + self.name + " hits you for " + str(dmg) + " damage!"
			target.hp -= dmg
		else:
			print "The " + self.name + " misses."
	
	def dropLoot(self, target):
		print "You gain " + str(self.goldValue) + " gold!"
		target.gold += self.goldValue
		print "You now have " + str(target.gold) + " gold."

	def delete(self):
		global player
		global availableTargets
		availableTargets.remove(self.id)
		print "The " + self.name + " dies!"
		self.dropLoot(player)
		
	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.name
		
class Vermin(Monster):
	beingHitThreshold = 0 #the number a player has to roll in order to hit
	hitDie = 4 #the die a monster rolls in order to attempt hitting a player
	goldValue = 1
	
class Rat(Vermin):
	name = "Rat"
	dmgDie = 1
	hp = 1

class Bat(Vermin):
	name = "Bat"
	dmgDie = 2
	hp = 2

class Weak(Monster):
	beingHitThreshold = 2
	hitDie = 6
	goldValue = 2
	
class GiantRat(Weak):
	name = "Giant Rat"
	dmgDie = 4
	hp = 4
	
class Wolf(Weak):
	name = "Wolf"
	dmgDie = 6
	hp = 6
	
class Goblin(Weak):
	name = "Goblin"
	dmgDie = 8
	hp = 8

class Average(Monster):
	beingHitThreshold = 4
	hitDie = 8
	goldValue = 4
	
class Orc(Average):
	name = "Orc"
	dmgDie = 6
	hp = 10
	armor = 6
	
class Skeleton(Average):
	name = "Skeleton"
	dmgDie = 8
	hp = 4
	
class GiantSpider(Average):
	name = "Giant Spider"
	dmgDie = 6
	hp = 12
	
class Tough(Monster):
	beingHitThreshold = 6
	hitDie = 10
	goldValue = 6

class Giant(Tough):
	name = "Giant"
	dmgDie = 10
	hp = 20
	
class Troll(Tough):
	name = "Troll"
	dmgDie = 10
	hp = 12
	armor = 10
	
class BabyDragon(Tough):
	name = "Baby Dragon"
	dmgDie = 9 
	hp = 40
	armor = 6
	
class Boss(Monster):
	beingHitThreshold = 8
	hitDie = 12
	goldValue = 0
	
	def delete(self):
		global forever
		global floorCleared
		print "You win!"
		inCombat = False
		floorCleared = True
		forever = False
	
	
class Dragon(Boss):
	name = "Dragon"
	dmgDie = 11
	hp = 60
	armor = 10

player = Character()
forever = True
while forever:
	floor = Floor()
	floorCleared = False
	while not floorCleared:
		if not inCombat:
			print str(floor.rooms.keys())
			player.getInput()
		
		if inCombat:
			print str(currentRoom.monsters)
			player.getInput()
		
		#delete monster if it has no hp left
		for r in floor.rooms.keys():
			for m in floor.rooms[r].monsters.keys():
				if floor.rooms[r].monsters[m].hp <= 0:
					floor.rooms[r].monsters[m].delete()
					del floor.rooms[r].monsters[m]
					
		#delete room if there are no monsters left
		for r in floor.rooms.keys():
			if len(floor.rooms[r].monsters) == 0:
				floor.rooms[r].delete()
				del floor.rooms[r]
				
		#delete floor if there are no rooms left
		if len(floor.rooms) == 0:
			floor.delete()
			del floor
			floorCleared = True
			break
		
		#monsters' turn
		if inCombat:
			for monster in currentRoom.monsters.keys():
				currentRoom[monster].attack(player)
				if player.hp <= 0:
					player.delete()
					del player

print "Game Over"
