import random
import time

# Define some sample Pokémon and their attributes
class Pokemon:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

# Define a function for a battle between two Pokémon
def battle(pokemon1, pokemon2):
    while pokemon1.hp > 0 and pokemon2.hp > 0:
        # Pokémon 1 attacks Pokémon 2
        damage = pokemon1.attack - pokemon2.defense
        damage = max(damage, 1)  # Ensure a minimum of 1 damage
        pokemon2.hp -= damage
        print(f"{pokemon1.name} attacks {pokemon2.name} for {damage} damage.\n")
        time.sleep(2)  # Pause for 2 seconds

        # Check if Pokémon 2 fainted
        if pokemon2.hp <= 0:
            print(f"{pokemon2.name} fainted!")
            break

        # Pokémon 2 attacks Pokémon 1
        damage = pokemon2.attack - pokemon1.defense
        damage = max(damage, 1)
        pokemon1.hp -= damage
        print(f"{pokemon2.name} attacks {pokemon1.name} for {damage} damage.\n")
        time.sleep(2)  # Pause for 2 seconds

        # Check if Pokémon 1 fainted
        if pokemon1.hp <= 0:
            print(f"{pokemon1.name} fainted!")

# Create two sample Pokémon
pikachu = Pokemon("Pikachu", 100, 30, 10)
charizard = Pokemon("Charizard", 120, 21, 12)
blastoise = Pokemon("Blastoise", 122, 20, 19)

player1 = input("Choose your pokemon\n ||\tPikachu\t|| \n ||\tBlastoise\t|| \n ||\tCharizard\t|| \n--> ")

print("Player 1 has chosen:", player1)

player2 = input("Choose your pokemon\n ||\tPikachu\t|| \n ||\tBlastoise\t|| \n ||\tCharizard\t|| \n--> ")

print("Player 2 has chosen:", player1)

if player1.lower() == "charizard":
    player1 = charizard
elif player1.lower() == "blastoise":
    player1 = blastoise
elif player1.lower() == "pikachu":
    player1 = pikachu

if player2.lower() == "charizard":
    player2 = charizard
elif player2.lower() == "blastoise":
    player2 = blastoise
elif player2.lower() == "pikachu":
    player2 = pikachu

# Start a battle between pokemon
print("A wild battle begins!")

battle(player1, player2)

# Determine the winner
winner = player1 if player1.hp > 0 else player2
loser = player2 if player1.hp > 0 else player1

# Save the battle result to a file
with open("pokemon_battle_results.txt", "a") as file:
    file.write(f"{winner.name} defeated {loser.name}\n")
