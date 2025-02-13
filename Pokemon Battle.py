import random, time

class Pokemon:
    def __init__(self, name, attack, defense, health, skill_points):
        self.name=name
        self.attack=attack
        self.defense=defense
        self.health=health
        self.skill_points=skill_points

    def getInformation(self):
        print(f"{self.name}\t attack: {self.attack}\t defense: {self.defense}\t health: {self.health}")

    #def takeTurn(self):

    def basicAttack(self,target):  #Basic attack
        damage=self.attack-target.defense
        if damage>0:
            target.health-=damage
            print(f"{self.name} attacked {target.name} for {damage} damage.")
        else:
            print(f"{self.name}'s attack had no effect on {target.name}.")

    def getHealth(self):
        self.health+=3
        print(f"{self.name} restored 3 health.")

    def faint(self):
        print(f"{self.name} fainted!")
        #Game over

class Pikachu(Pokemon):

    def __init__(self):
        super().__init__(name="Pikachu", attack=7, defense=3, health=10, skill_points=2)

    def lowerDefense(self, target): #Lower opponent defense
        if target.defense>2:
            target.defense-=2
            print(f"{self.name} lowered {target.name}'s defense by 2.")
        else:
            target.defense=0
            print(f"{target.name}'s defense can't be lowered anymore.")

    def stun(self, target): #30% of opponent skip turn
        chance=random.randint(0,9)
        if chance<3:
            target.isStunned=True #Target is stunned
            print(f"{self.name} stunned {target.name}.")
        else:
            print(f"Missed!")

    def lightning(self, target): #Skill attack
        if self.skill_points>0:
            self.skill_points-=1
            damage=int(self.attack*1.5-target.defense)
            if damage>0:
                target.health-=damage
                print(f"{self.name} attacked {target.name} for {damage} damage.")
            else:
                print(f"{self.name}'s attack had no effect on {target.name}.")
        else:
            print("Skill points insufficient, default to basic attack")
            self.basicAttack(target)

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__(name="Bulbasaur", attack=3, defense=4, health=14, skill_points=3)
        self.isStunned=False

    def raiseAttack(self): #Raise self attack
        self.attack+=2
        print(f"{self.name} raised its attack by 2.")

    def stomp(self, target): #Skill attack
        if self.skill_points>0:
            self.skill_points-=1
            damage=int(self.attack*1.5-target.defense)
            if damage>0:
                target.health-=damage
                print(f"{self.name} attacked {target.name} for {damage} damage.")
            else:
                print(f"{self.name}'s attack had no effect on {target.name}.")
        else:
            print("Skill points insufficient, default to basic attack")
            self.basicAttack(target)

class PlayGame:
    def __init__(self):
        self.player1=None
        self.player2=None

    def choosePokemon(self, pikachu, bulbasaur):
        print("p-Pikachu")
        print("b-Bulbasaur")
        choice_1=input("Player 1 chooses a Pokemon: ").lower()
        choice_2=input("Player 2 chooses a Pokemon: ").lower()
        if choice_1=="p" and choice_2=="b":
            player1=pikachu
            player2=bulbasaur
        elif choice_1=="b" and choice_2=="p":
            player1=bulbasaur
            player2=pikachu
        else:
            print("Invalid choice, defaulting to player 1-Pikachu, player 2-Bulbasaur")
            player1=pikachu
            player2=bulbasaur
        self.player1=player1
        self.player2=player2
        time.sleep(2)

    def pikachuActionSet(self, player_num):
        if player_num==1:
            player=self.player1
            target=self.player2
        else: #player_num==2
            player=self.player2
            target=self.player1
        print("1 - basic attack")
        print("2 - lower defense")
        print("3 - stun")
        print("4 - lightning")
        print("5- get health")
        action=input(f"What will {player.name} do? ")
        if action=="1":
            player.basicAttack(target)
        elif action=="2":
            player.lowerDefense(target)
        elif action=="3":
            player.stun(target)
        elif action=="4":
            player.lightning(target)
        elif action=="5":
            player.getHealth()
        else:
            print("Invalid choice, default to basic attack")
            player.basicAttack(target)

    def bulbasaurActionSet(self, player_num):
        if player_num==1:
            player=self.player1
            target=self.player2
        else: #player_num==2
            player=self.player2
            target=self.player1
        if player.isStunned==True:
            print(f"{player.name} is stunned, turn skipped.")
            player.isStunned=False
            return
        print("1 - basic attack")
        print("2 - raise attack")
        print("3 - stomp")
        print("4 - get health")
        action=input(f"What will {player.name} do? ")
        if action=="1":
            player.basicAttack(target)
        elif action=="2":
            player.raiseAttack()
        elif action=="3":
            player.stomp(target)
        elif action=="4":
            player.getHealth()
        else:
            print("Invalid choice, default to basic attack")
            player.basicAttack(self.player2)

    def startGame(self):
        while True:
            print("")
            self.player1.getInformation()
            self.player2.getInformation()
            time.sleep(2)

            print("")
            print("Player 1's turn")
            if self.player1.name=="Pikachu":
                self.pikachuActionSet(1)
            else:
                self.bulbasaurActionSet(1)

            if self.player2.health<=0:
                self.player2.faint()
                print("Player 1 wins! Game over.")
                break

            time.sleep(2)

            print("")
            print("Player 2's turn")
            if self.player2.name=="Pikachu":
                self.pikachuActionSet(2)
            else:
                self.bulbasaurActionSet(2)

            if self.player1.health<=0:
                self.player1.faint()
                print("Player 2 wins! Game over.")
                break

            time.sleep(2)

pikachu = Pikachu()
bulbasaur = Bulbasaur()

game=PlayGame()
game.choosePokemon(pikachu, bulbasaur)
game.startGame()