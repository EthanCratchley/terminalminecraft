import time
import random

# Run the Game
def main():
    print("Welcome to Terminal Minecraft!")
    time.sleep(2)
    print("You can do one of three things.")
    time.sleep(2)
    print("You can attack the skeleton. (Watch out it can attack you too!)")
    time.sleep(2)
    print("You can kill the pig for food! (Food can heal you!)")
    time.sleep(3)
    print("Or you can run away!")
    time.sleep(1)
    
    # Continue the Game until the Player Runs Away to Quit    
    while True:
        user_msg = input("Enter (Attack Skeleton) or (Attack Pig) or (Run Away):")

        if user_msg.title() == "Attack Skeleton":
            skeleton_0.take_damage(steve_0.hand())
            if skeleton_0.health >=1:
                damage_dealt = skeleton_0.attack()
                steve_0.take_damage(damage_dealt)
        elif user_msg.title() == "Attack Pig":
            pig_0.take_damage(steve_0.hand())
        elif user_msg.title() == "Run Away":
            print("You ran away!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

#Mobs, Friendly Animals, and Humans(User)
class Creature():

    def __init__(self, health):
        self.health = health

# Checks if Creature is Alive
    def check_life(self):
        if self.health <= 0:
            print(f"The {self.__class__.__name__} is dead.")
        else:
            print(f"The {self.__class__.__name__} is at {self.health} health!")

    # Lose Health when Taking Damage
    def take_damage(self, damage):
        self.health -= damage
        self.check_life()

#Friendly Animals 
class Friendly(Creature):
    
    def __init__(self, health):
        super().__init__(health)


#Friendly Animal 1
class Pig(Friendly):

    def __init__(self, health):
        super().__init__(health)
        self.food_dropped = False  # Initialize the flag to False

    # Check Life of Pig 
    def check_life(self):
        if self.health <= 0:
            print(f"The {self.__class__.__name__} is dead.")
            self.pork()
        else:
            print(f"The {self.__class__.__name__} is at {self.health} health!")

    def pork(self):
        if self.health <= 0 and not self.food_dropped:  # Check if the pig is dead and food is not dropped yet
            steve_0.heal()   # Heal the player
            print("You got food from the pig and healed by 2 health points!")
            self.food_dropped = True  # Set the flag to True to indicate food is dropped
        elif self.food_dropped:
            print("The pig is already dead, and there's no food left.")
        else:
            print("The pig is still alive, can't get food yet.")

#Enemies 
class Mob(Creature):
    
    def __init__(self, health, damage, attack_chance):
        super().__init__(health)
        self.damage = damage
        self.attack_chance = attack_chance

# Mob 1 
class Skeleton(Mob):

    def __init__(self, health, damage, attack_chance):
        super().__init__(health, damage, attack_chance)

    # Skeleton Attack
    def attack(self):
        if random.random() <= self.attack_chance:
            return self.damage
        else:
            print("The skeleton missed its attack!")
            return 0
        
# Weapon for Skeleton to do damage 
    def bow_arrow(self):
        return self.damage

# Player 
class Steve(Creature):

    def __init__(self, health, damage):
        super().__init__(health)
        self.damage = damage

    # Deal Damage
    def hand(self):
        return self.damage
    
    # Regenerate Health
    def heal(self):
        self.health += 2
    
# Creating Creatures and Giving Them Health and Damage
pig_0 = Pig(8) # 8 Health
skeleton_0 = Skeleton(10, 3, 0.75) # 10 Health, Deal 3 Damage, 75% Chance to Attack
steve_0 = Steve(10, 4) # 10 Health, Deal 4 Damage

# Run Game
main()