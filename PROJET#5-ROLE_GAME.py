#import of module
import random


ENNEMY_HEALTH = 50
USER_HEALTH = 50
NUMBER_OF_POTIONS = 3
MENU_CHOICES = ["1", "2"]
SKIP_TURN = False

# loop of the game
while True:
# while user_life > 0 and ennemi_life > 0:

    # Game playing
    if SKIP_TURN:
        print("Vous passez votre tour")
        SKIP_TURN = False
    
    else:
        user_choice = ""
        while user_choice not in MENU_CHOICES:
            user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        
        if user_choice == "1": #Attack
            user_attack = random.randint(5, 10)
            ENNEMY_HEALTH -= user_attack
            print(f"Vous avez infligé {user_attack} points de dégats à l'ennemi ⚔️")
        
        elif user_choice == "2" and NUMBER_OF_POTIONS > 0:  # potion
            potion_health = random.randint(15, 20)
            USER_HEALTH += potion_health
            NUMBER_OF_POTIONS -= 1
            SKIP_TURN = True
            print(f"Vous récupérez {potion_health} points de vie ❤️ ({NUMBER_OF_POTIONS} ? restantes)")
        else:
            print("Vous n'avez plus de potions...")
            continue
    

    if ENNEMY_HEALTH <= 0:
        print("Tu as gagné !")
        break

    # ennemi attack
    enemy_attack = random.randint(5, 15)
    USER_HEALTH -= enemy_attack
    print(f"L'ennemi vous a infligé {enemy_attack} points de dégats ⚔️")

    if USER_HEALTH <= 0:
        print("Tu as perdu !")
        break

    # Stats
    print(f"Il vous reste {USER_HEALTH} points de vie.")
    print(f"Il reste {ENNEMY_HEALTH} points de vie à l'ennemi.")
    print("-" * 50)

print("Fin du jeu.")