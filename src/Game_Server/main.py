from Game_Server.GameLoop import *

game_loop = GameLoop(True)
thread = threading.Thread(target=game_loop.game_loop, args=(None,))
player_name = input("What is your name?: [TYPE YOUR NAME]: ")
kingdom_name = input("What is the name of your kingdom? [TYPE THE NAME OF YOUR KINGDOM]: ")

print(f"Your name is {player_name} and your kingdom is named {kingdom_name}")

game_loop.game_loop()