#---------------------------------------------------------------[Modules imported for enriched experience]---------------------------------------------------------------
import \
   random, \
   time, \
   os
try: #if module is found and no errors occur when importing
    from colorama import Fore
    import fade
except: #if module is not found install it using the os module
    print('installing modules...')
    os.system('pip install colorama')
    os.system('pip install fade')
    from colorama import Fore
    import fade
    os.system('cls')
#------------------------------------------------------------------------#---------------------------------------------------------------

os.system('Title Dungeon rpg game') #set terminal title to dungeon rpg game

#------colour variables for coloured string prints------
red = Fore.RED
reset = Fore.RESET
white = Fore.WHITE
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW
cyan = Fore.CYAN
lc = Fore.LIGHTCYAN_EX
grey = Fore.LIGHTBLACK_EX
purple = Fore.MAGENTA
aqua = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX

#---------------------------------------------------------------#---------------------------------------------------------------
class Fighter:
   def __init__(self,
                name,
                starting_health,
                weapon,
                shield,
                ):
       """Class use: Stores fighter abilities for player and enemies.
       Also stores the classes functions for player and enemies."""
       #health bar and fighter attributes
       self.name = name
       self.__health = starting_health
       self._max_health = starting_health
       self.weapon = weapon
       self.shield = shield
       self.is_defending = False

       #classes with special abilities:
       self.has_used_wish = False #healer

       self.rage_active = False #warrior
       self.rage_used = False #warrior

       self.beam_used = False #mage

   # ---------------------------------------------------------------#---------------------------------------------------------------
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
       print(f'{red}Class selected: Warrior')
       self.weapon *= 1.1
       self.__health =  self.__health*1.5
       self._max_health = self.__health # set max health to fix hp bar not showing remaining bars
       self.shield *= 1.2
       self.class_name = f"{red}Warrior{reset}"
       print(f"""{red}Class perks:
+10% weapon
+50% health
+20% shield
special ability: enraged 90% more damage on next attack{reset}""")
       input("Press enter to continue")


   def Mage(self):
       '''mage perks'''
       print(f'{blue}Class selected: Mage')
       self.weapon *= 1.25
       self.__health = self.__health*0.8
       self._max_health = self.__health
       self.class_name = f"{blue}Mage{reset}"
       self.shield *= 0.7
       print(f"""{blue}Class perks:
+25% weapon
-20% health
-30% shield
special ability: Beam 50% of enemy health{reset}""")
       input("Press enter to continue")


   def Archer(self):
       '''archer perks'''
       print(f'{purple}Class selected: Archer')
       self.weapon *= 1.3
       self.__health = self.__health*0.85
       self._max_health = self.__health
       self.class_name = f"{purple}Archer{reset}"
       print(f"""{purple}Class perks:
+30% weapon
-15% health{reset}
special ability: you have no special abilities -_- (to much effort to add){reset}
""")
       input("Press enter to continue")


   def Tank(self):
       '''tank perks'''
       print(f'{green}Class selected: Tank')
       self.weapon *= 0.5
       self.__health = self.__health*2.3
       self._max_health = self.__health
       self.shield *= 1.4
       self.class_name = f"{green}Tank{reset}"
       print(f"""{green}Class perks:
-50% weapon
+150% health
+40% shield
{reset}""")
       input("Press enter to continue")


   def Healer(self):
       '''healer stats'''
       print(f'{yellow}Class selected: Healer')
       self.weapon *= 0.9
       self.__health = self.__health*0.7
       self._max_health = self.__health
       self.shield *= 0.8
       self.class_name = f"{yellow}Healer{reset}"
       print(f"""{yellow}Class perks:
-10% weapon
+80% health
-20% shield
special ability: Instead of dying revive yourself and heal for 100% of your health{reset}""")
       input("Press enter to continue")

   # ----------------------[Choice class]-----------------------------------------
   def Character_Class(self):
       '''get input to select character class and assign perks'''
       self.class_name = 'Not selected'
       while True: #until input is in options [1-4]
           print(Game.refined_banner)
           class_select = input(f'''
           {yellow}Select your class: {reset}\n
           {lc}[1] {red}Warrior (best balance for health and attack) {reset}\n
           {lc}[2] {blue}Mage (ranged damage using magical power less health){reset}\n
           {lc}[3] {purple}Archer (ranged damage using arrows power best single hit){reset}\n
           {lc}[4] {green}Tank (most health but least damage){reset}\n
           {lc}[5] {yellow}Healer (ability to revive yourself once){reset}\n
           {grey}============================================================================================{reset}

           Your choice:[--> ''')
           '''Condition of class selection based on input'''
           if class_select == '1':
               self.Warrior()
               break
           elif class_select == '2':
               self.Mage()
               break
           elif class_select == '3':
               self.Archer()
               break
           elif class_select == '4':
               self.Tank()
               break
           elif class_select == '5':
               self.Healer()
               break
           else:
               print(f'{red}Invalid choice!{reset}')
               time.sleep(1)
               os.system('cls')
       os.system('cls')
       # ---------------------------------------------------------------

       # ------------------------Enemy random class logic---------------------------------------
   def enemy_Class(self):
       '''Randomize enemy class choice 1/5 per class'''
       choices = ['Warrior',
                  'Mage',
                  'Archer',
                  'Tank',
                  'Healer']
       self.random = random.choice(choices)
       print(f'Enemy has:')
       #call function based on attribute
       getattr(self, self.random)()
       time.sleep(1.2)
       os.system('cls')


   # --------------------[Functions to check character stats (health)]-------------------------------------------
   def report(self): #return stats
       print(f'{self.name} — Health: {int(self.__health)}')


   def is_dead(self):
       '''death logic'''
       if self.__health <= 0:
           # if character enemy/player is healer
           if self.class_name == f"{yellow}Healer{reset}" and not self.has_used_wish:
               print(f'\n{self.name} used WISH and was revived!')
               self.__health = self._max_health
               self.has_used_wish = True
               time.sleep(2)
               return False
           return True
       return False

   # ---------------------------------------------------------------

   # ------------------------[Player abilities]---------------------------------------

   def random_attack(self):
       '''normal attack logic'''
       self.attack_power = random.randint(int(self.weapon * 0.8), int(self.weapon * 1.2))
       print(f'{self.name} uses a basic attack! Power: {self.attack_power}')
       if self.rage_active:
           print(f'{lc}Rage used!')
           self.attack_power = int(self.attack_power * 1.9)
           self.rage_active = False  # reset after use
           self.rage_used = True
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
       if self.rage_active and not self.rage_used:
           print(f'{lc}Rage used!')
           attack_power = int(attack_power * 1.9)
           self.rage_active = False  # reset after use
           self.rage_used = True
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

   '''exclusive attacks for classes'''
   def Warrior_Rage(self):
       '''Increases the next attack damage by 90% (instant 1 hit when paired with skilled attack)'''
       #dialogue
       print(f'{Fore.LIGHTRED_EX}You become enraged and your next attack will deal 90% more damage!{reset}')
       input(f'Press enter to continue...')
       #logic
       self.rage_active = True


   def Mage_beam(self):
       '''Shoots a beam at the target which syphons 20% of their health (can only be used once)'''
       pass

   def Tank_reflect(self):
       '''Reflect the enemeies attack and deal 90% of the damage dealt on you to them'''
       pass
   def Archer_snipe(self):
       '''Archer shoots A arrow that deals damage 50% of the enemies health and also skipping their turn'''

#--------------------------------------------------------------[Enemy logic + Healthbar display]---------------------------------------------------------------


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
                color="",

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
       class_name = self.entity.class_name if self.entity.class_name else "None"
       print(f"{self.barrier}"
             f"{self.color if self.is_colored else ''}"
             f"{remaining_bars * self.symbol_remaining}"
             f"{lost_bars * self.symbol_lost}"
             f"{self.colors['default'] if self.is_colored else ''}"
             f"{self.barrier} ({class_name})")



   @staticmethod #not in instance (self/cls)
   def clear_screen():
       '''Clear terminal screen each loop'''
       os.system('cls' if os.name == 'nt' else 'clear')


   @staticmethod
   def game_lore():
       '''Lore of the game ig'''
       lore_dialogue = [
           "Leader: You have been training for many years young fighter"
           "Leader: It is time you face a challenge"
           "You: Yes sir!"
           "A goblin leaps forward and challenges you to fight to the death...\n",

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
           time.sleep(0.1)
           class_name = player.class_name
           Enemy1.clear_screen()
           print(Game.refined_banner)
           print('== BATTLE STATUS ==')
           player.report()
           player.health_bar.update()
           player.health_bar.draw()
           enemy.report()
           enemy.health_bar.update()
           enemy.health_bar.draw()
           if enemy.is_dead():
               print(f'\n{green}You defeated the {enemy.name}! 🎉{reset}')
               enemy.health = 0
               enemy.health_bar.update()
               break
           if player.is_dead():
               print(f'\n{red}You were defeated by the {enemy.name}!{reset} 💀')
               player.health = 0
               player.health_bar.update()
               break
           if class_name == f"{red}Warrior{reset}" and not player.rage_used:
               print('====================')
               print('\nYour turn! Choose an action:')
               print('1. Regular Attack')
               print('2. Skill Attack')
               print('3. Defend')
               print('4. Enrage (90% more damage next hit)')
               choice = input('> ')
           elif class_name == f"{blue}mage{reset}" and not player.rage_used:
               print('====================')
               print('\nYour turn! Choose an action:')
               print('1. Regular Attack')
               print('2. Skill Attack')
               print('3. Defend')
               print('4. Shoot beam (50% of enemy health)')
               choice = input('> ')
           else:
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
           elif choice == '4' and class_name == f"{red}Warrior{reset}" and not player.rage_used:
               player.Warrior_Rage()
           else:
               print('Invalid choice! You lose your turn.')
           print(f'\n{enemy.name}\'s turn...')
           enemy_action = random.choice(['attack', 'magic'])
           if enemy_action == 'attack':
               attack = enemy.random_attack()
           else:
               attack = enemy.random_attack() + enemy.magic
           player.defend(attack)
           input('\nPress Enter to continue to the next round...')

class Game:
    '''Puts everything together to create the game'''
    #-----static variables-----------#
    first_run = False

    banner = \
        """
                                ██████╗ ██████╗  ██████╗      ██████╗  █████╗ ███╗   ███╗███████╗
                                ██╔══██╗██╔══██╗██╔════╝     ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
                                ██████╔╝██████╔╝██║  ███╗    ██║  ███╗███████║██╔████╔██║█████╗  
                                ██╔══██╗██╔═══╝ ██║   ██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
                                ██║  ██║██║     ╚██████╔╝    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
                                ╚═╝  ╚═╝╚═╝      ╚═════╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                                                             
        """
    refined_banner = fade.purpleblue(banner)
    #------------------------------------------------------------#---------------------------------------------------------------
    @staticmethod
    def game_setup():
        '''Player objects along side their stats and healthbar'''
        # ---------------------------------------------------------------[Game setup]---------------------------------------------------------------
        # Creates objects and calls functions to create game
        player = Fighter("Hero", 100, 60, 20)
        player.Character_Class()
        player.health_bar = Enemy1("HP Bar", 0, 0, 0, 0, None, entity=player, color="green")

        enemy_base = Fighter("Monkey", 80, 30, 10)
        enemy_base.enemy_Class()

        enemy = Enemy1(f"Monkey", 15, 146, 39, 10, None, entity=enemy_base)
        enemy.class_name = enemy_base.class_name
        enemy.has_used_wish = enemy_base.has_used_wish
        enemy.weapon = enemy_base.weapon
        enemy.shield = enemy_base.shield
        enemy.health = enemy_base.health
        enemy._max_health = enemy_base.health_max

        enemy.health_bar = Enemy1("HP Bar", 0, 0, 0, 0, None, entity=enemy, color="red")
        #check if loop was played
        if not Game.first_run:
            print(Game.refined_banner)
            print('\n')
            Enemy1.game_lore()
            Game.first_run = True
        #fight

        Enemy1.start_battle(player, enemy)
        # ---------------------------------------------------------------#---------------------------------------------------------------

    @staticmethod
    def play_again():
        '''Ask if player wants to play again'''
        while True:
            choice = input('Play again? (y/n): ').strip().lower()
            if choice == 'y':
                try:
                    os.system('cls')
                except:
                    os.system('clear')
                Game.game_setup()
            elif choice == 'n':
                print("Thanks for playing!")
                break
            else:
                print('Invalid choice! Please type y or n.\n')
                time.sleep(1)

#---------------------------------------------------------------
#call Game functions
Game().game_setup()
Game.play_again()
#------------------------End of script---------------------------------------
