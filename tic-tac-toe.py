import itertools

def game_board(game_map, player=0, row=0, column=0, just_display=False):
	try:
		if game_map[row][column] != 0:
			print("This space is occupied, try another!")
			return False
		print("   0  1  2")
		#enumerate : return the item and its index value as we iterate
		if not just_display:
			game[row][column] = player
		for count, row in enumerate(game):
			print(count, row)
		return game_map

	except IndexError:
		print("Did you try a number other than 0, 1 or 2? (Index Error)")
		return False

	except Exception as e:
		print(str(e))
		return False


def win(current_game):
	def all_same(l):
		if(l.count(l[0]) == len(l) and l[0] != 0):
			return True
		else:
			return False

	#horizontal
	for row in game:
		print(row)
		if all_same(row):
			print(f"Player {row[0]} is the winner horizontally!")
			return True

	#vertical
	for col in range(len(row[0])):
		check = []
		for row in game:
			check.append(row[col])
		if all_same(check):
			print(f"Player {check[0]} is the winner vertically!")
			return True

	#diagonal /
	diags = []
	for idx, reverse_idx in enumerate(reversed(range(len(game)))):
		diags.append(game[idx][reverse_idx])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner Diagonally (/)")
		return True

	# \ diagonal
	diags = []
	for ix in range(len(game)):
		diags.append(game[ix][ix])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner diagonally (\\) ")
		return True

	return False

play = True
players = [1,2]
while play:
	game = [[0,0,0],
			[0,0,0],
			[0,0,0],]

	game_won = False
	player_cycle = itertools.cycle([1,2])
	game_board(game, just_display = True)
	while not game_won:
		current_player = next(player_cycle)
		played = False
		while not played:
			print(f"Player : {current_player}")
			column_choice = int(input("Which Column? : "))
			row_choice = int(input("Which Row? : "))
			played = game_board(game, player=current_player, row=row_choice, column=column_choice)

	if win(game):
		game_won = True
		again = input("The game is over, would you like to play again? (y/n)")
		if again.lower() == "y":
			print("restarting!")
		elif again.lower() == "n":
			print("Bye!")
			play = False
		else:
			print("I'll take that as a No :), Bye !")
			play = False


# game = "I want to play a game"
# print(id(game))


# def game_board():

#     global game
#     print(id(game))
#     game = "A game"
#     print(id(game))
#     return game


# game_board()
# print(game)
