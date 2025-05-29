import \
   random, \
   time, \
   os

os.system('Title Dungeon rpg game') #set terminal title to dungeon rpg game

class Fighter:
   def __init__(self,
                name,
                starting_health,
                weapon,
                shield,
                ):
       #health bar and fighter attributes
       self.name = name
       self.__health = starting_health
       self._max_health = starting_health
       self.weapon = weapon
       self.shield = shield
       self.is_defending = False
       self.has_used_wish = False
       self.class_name = None


   @property #healthbar property returning health value (read only attribute)
   def health(self):
       return self.__health


   @health.setter #healthbar set health (change health using decrorator)
   def health(self, value):
       self.__health = max(0, value)


   @property #(read only attribute)
   def health_max(self):
       return self._max_health


   def Warrior(self):
       '''warrior perks'''
       print('Class selected: Warrior')
       self.weapon *= 1.1
       self.__health =  self.__health*1.5
       self._max_health = self.__health # set max health to fix hp bar not showing remaining bars
       self.shield *= 1.2


   def Mage(self):
       '''mage perks'''
       print('Class selected: Mage')
       self.weapon *= 1.25
       self.__health = self.__health*0.8
       self._max_health = self.__health
       self.shield *= 0.7
       print("""Class perks:
+25% weapon
-20% health
-30% shield""")
       input("Press enter to continue")


   def Archer(self):
       '''archer perks'''
       print('Class selected: Archer')
       self.weapon *= 1.3
       self.__health = self.__health*0.85
       self._max_health = self.__health
       print("""Class perks:
+20% weapon
-10% health""")
       input("Press enter to continue")


   def Tank(self):
       '''tank perks'''
       print('Class selected: Tank')
       self.weapon *= 0.5
       self.__health = self.__health*2.3
       self._max_health = self.__health
       self.shield *= 1.4
       print("""Class perks:
-50% weapon
+150% health
+40% shield
""")
       input("Press enter to continue")


   def Healer(self):
       '''healer stats'''
       print('Class selected: Healer')
       self.weapon *= 0.9
       self.__health = self.__health*0.7
       self._max_health = self.__health
       self.shield *= 0.8
       self.class_name = "Healer"
       print("""Class perks:
-10% weapon
+80% health
-20% shield
           """)
       input("Press enter to continue")


   def Character_Class(self):
       '''get input to select character class and assign perks'''
       class_select = input('''
Select your class:
[1] Warrior (best balance for health and attack)
[2] Mage (ranged damage using magical power less health)
[3] Archer (ranged damage using arrows power best single hit)
[4] Tank (most health but least damage)
[5] Healer (ability to revive yourself once)


Your choice: ''')
       '''Condition of class selection based on input'''
       if class_select == '1':
           self.Class = self.Warrior()
       elif class_select == '2':
           self.Class = self.Mage()
       elif class_select == '3':
           self.Class = self.Archer()
       elif class_select == '4':
           self.Class = self.Tank()
       elif class_select == '5':
           self.Class = self.Healer()
       else:
           raise ValueError('Invalid choice')
       time.sleep(1.5)
       os.system('cls')


   def enemy_Class(self):
       '''Randomize enemy class choice 1/5 per class'''
       choices = ['Warrior',
                  'Mage',
                  'Archer',
                  'Tank',
                  'Healer']
       self.random = random.choice(choices)
       print(f'Enemy has:')
       getattr(self, self.random)()
       time.sleep(1.5)
       os.system('cls')


   def report(self): #return stats
       print(f'{self.name} — Health: {int(self.__health)}')


   def is_dead(self):
       '''death logic'''
       if self.__health <= 0:
           if self.class_name == "Healer" and not self.has_used_wish: #if character enemy/player is healer
               print(f'\n{self.name} used WISH and was revived!')
               self.__health = self._max_health
               self.has_used_wish = True
               time.sleep(2)
               return False
           return True
       return False


   def random_attack(self):
       '''normal attack logic'''
       self.attack_power = random.randint(int(self.weapon * 0.8), int(self.weapon * 1.2))
       print(f'{self.name} uses a basic attack! Power: {self.attack_power}')
       return self.attack_power


   def skill_attack(self):
       '''skill attack logic (needs balancing)'''
       attack_power = random.randint(int(self.weapon * 0.8), int(self.weapon * 1.2))
       target = random.randint(2, 4)
       print(f'== Skill Attack! Try to hit enter in exactly {target} seconds ==')
       tic = time.time()
       input('Press enter when ready...')
       toc = time.time()
       time_taken = toc - tic
       diff = abs(target - time_taken)
       #damage multiplier
       if diff < 0.2:
           multiplier = 1.5
       elif diff < 0.5:
           multiplier = 1.3
       elif diff < 1.0:
           multiplier = 1.1
       else:
           multiplier = 0.4


       print(f'Base Attack: {attack_power}')
       print(f'Timing Multiplier: {multiplier:.2f}')
       return int(attack_power * multiplier)


   def defend(self, attack_power):
       '''defend action logic'''
       damage = attack_power - self.shield
       if self.is_defending: #if player is defending = True
           damage = damage // 2
           print(f'{self.name} blocks! Damage halved.')
           self.is_defending = False


       if damage > 0:
           self.__health -= damage
           print(f'{self.name} takes {int(damage)} damage!')
       else:
           print(f'{self.name} takes no damage.')




class Enemy1(Fighter):
   '''Health bar symbols/colours'''
   #static variables
   symbol_remaining = "█"
   symbol_lost = "_"
   barrier = "|"
   colors = {
       "red": "\033[91m", "green": "\033[92m",
       "default": "\033[0m"
   }


   def __init__(self,
                name,
                magic,
                starting_health,
                weapon,
                shield,
                Class,
                entity,
                length=20,
                is_colored=True,
                color=""
                ):
       super().__init__(name, starting_health, weapon, shield) #get from Fighter class
       self.magic = magic
       self.entity = entity
       self.length = length
       self.current_value = entity.health
       self.max_value = entity.health_max
       self.is_colored = is_colored
       self.color = self.colors.get(color, self.colors["default"])


   def update(self):
       self.current_value = self.entity.health


   def draw(self):
       '''healthbar logic (how healthbar will display)'''
       remaining_bars = round(self.current_value / self.max_value * self.length)
       lost_bars = self.length - remaining_bars
       print(f"{self.barrier}"
             f"{self.color if self.is_colored else ''}"
             f"{remaining_bars * self.symbol_remaining}"
             f"{lost_bars * self.symbol_lost}"
             f"{self.colors['default'] if self.is_colored else ''}"
             f"{self.barrier}")


   def random_attack(self):
       '''Random attack logic'''
       attack_power = random.randint(int(self.weapon * 0.8), int(self.weapon * 1.2))
       print(f'{self.name} casts a magic attack! Power: {attack_power + self.magic}')
       return attack_power + self.magic


   @staticmethod #not in instance (self/cls)
   def clear_screen():
       '''Clear terminal screen each loop'''
       os.system('cls' if os.name == 'nt' else 'clear')

   @staticmethod
   def game_lore():
       '''Lore of the game ig'''
       lore_dialogue = [
           "In a land where ancient magic and steel rule, the world stands divided between the last human kingdoms and the shadow beasts of the Forgotten Realm.",

           "Each battle is not just a fight — it is part of a long prophecy where chosen heroes rise to restore balance or fall into the abyss.\n",

           "The player, a descendant of the ancient guardians, carries the fate of the realms."
           " Every enemy defeated weakens the grip of the Dark Lord, but every loss strengthens it.\n",

           "Step into the arena where every clash of sword and spell echoes across the ages."
           " Destiny awaits.\n"
       ]
       #print lore of game using for loops to reduce lines instead of repeating print, input and os.system each line.
       for line in lore_dialogue:
           print(line)
           input('Press enter to continue...')
           try: #windows clear command
            os.system('cls')
           except: #non windows clear command (linux I think)
               os.system('clear')


   @staticmethod #static method to act as a stand alone function while still being in the class
   def start_battle(player, enemy):
       '''battle logic between player and enemy'''
       while True:
           Enemy1.clear_screen()
           print('== BATTLE STATUS ==')
           player.report()
           player.health_bar.update()
           player.health_bar.draw()
           enemy.report()
           enemy.health_bar.update()
           enemy.health_bar.draw()
           print('====================')


           print('\nYour turn! Choose an action:')
           print('1. Regular Attack')
           print('2. Skill Attack')
           print('3. Defend')
           choice = input('> ')
           if choice == '1':
               attack = player.random_attack()
               enemy.defend(attack)
           elif choice == '2':
               attack = player.skill_attack()
               enemy.defend(attack)
           elif choice == '3':
               player.is_defending = True
               print(f'{player.name} prepares to block the next attack.')
           else:
               print('Invalid choice! You lose your turn.')


           if enemy.is_dead():
               print(f'\nYou defeated the {enemy.name}! 🎉')
               break


           time.sleep(1)


           print(f'\n{enemy.name}\'s turn...')
           enemy_action = random.choice(['attack', 'magic'])
           if enemy_action == 'attack':
               attack = enemy.random_attack()
           else:
               attack = enemy.random_attack() + enemy.magic
           player.defend(attack)


           if player.is_dead():
               print(f'\nYou were defeated by the {enemy.name}! 💀')
               break


           input('\nPress Enter to continue to the next round...')

first_run = False
def game_setup():
    #turn this code into a function so it can be called again using the loop instead of copy and pasting the whole block
        global first_run #declare as global and set as true when lore is played
        # Game Setup
        player = Fighter("Hero", 100, 60, 20)
        player.Character_Class()
        player.health_bar = Enemy1("HP Bar", 0, 0, 0, 0, None, entity=player, color="green")

        enemy_base = Fighter("Monkey", 80, 30, 10)
        enemy_base.enemy_Class()

        enemy = Enemy1(f"Monkey", 15, 120, 40, 10, None, entity=enemy_base)
        enemy.class_name = enemy_base.class_name
        enemy.has_used_wish = enemy_base.has_used_wish
        enemy.weapon = enemy_base.weapon
        enemy.shield = enemy_base.shield
        enemy.health = enemy_base.health
        enemy._max_health = enemy_base.health_max

        enemy.health_bar = Enemy1("HP Bar", 0, 0, 0, 0, None, entity=enemy, color="red")

        if not first_run:
            Enemy1.game_lore()
            first_run = True
        Enemy1.start_battle(player, enemy)



game_setup()


'''Ask if player wants to play again'''
while True:
    choice = input('Play again? (y/n): ')
    if choice == 'y':
        try:
         os.system('cls')
         game_setup()
        except:
            os.system('clear')
            game_setup()

    if choice == 'n':
        break
    else:
        print('invalid choice! \n')
        time.sleep(1)
