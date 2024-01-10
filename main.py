# Mohammed's Tic-Tac-Toe Game

# --------- Global Variables -----------

# Holds the game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Indicates if the game is still ongoing
is_game_active = True

# Specifies the winner of the game
winner = None

# Identifies the current player (X goes first)
current_player = "X"


# ------------- Functions ---------------

# Initiates and manages a game of tic tac toe
def play_game():

  # Display the initial game board
  display_board()

  # Loop until the game stops (due to a winner or tie)
  while is_game_active:

    # Handle a player's turn
    handle_turn(current_player)

    # Check if the game is over
    check_if_game_over()

    # Switch to the other player
    flip_player()
  
  # Since the game is over, print the winner or a tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


# Display the current game board
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


# Handle a turn for a given player
def handle_turn(player):

  # Get the desired position from the player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # Validate the user input and ensure the selected spot is available
  is_valid = False
  while not is_valid:

    # Validate the input
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # Get the correct index on the board
    position = int(position) - 1

    # Ensure the spot is available on the board
    if board[position] == "-":
      is_valid = True
    else:
      print("You can't go there. Please choose another position.")

  # Place the player's game piece on the board
  board[position] = player

  # Show the updated game board
  display_board()


# Check if the game is over
def check_if_game_over():
  check_for_winner()
  check_for_tie()


# Check for a winning player
def check_for_winner():
  # Access global variables
  global winner
  # Check for a winner in rows, columns, and diagonals
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Determine the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# Check rows for a win
def check_rows():
  # Access global variables
  global is_game_active
  # Check rows for a match and a non-empty sequence
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row matches, flag the game as over
  if row_1 or row_2 or row_3:
    is_game_active = False
  # Return the winner if found
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # Return None if there's no winner
  else:
    return None


# Check columns for a win
def check_columns():
  # Access global variables
  global is_game_active
  # Check columns for a match and a non-empty sequence
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any column matches, flag the game as over
  if column_1 or column_2 or column_3:
    is_game_active = False
  # Return the winner if found
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  # Return None if there's no winner
  else:
    return None


# Check diagonals for a win
def check_diagonals():
  # Access global variables
  global is_game_active
  # Check diagonals for a match and a non-empty sequence
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any diagonal matches, flag the game as over
  if diagonal_1 or diagonal_2:
    is_game_active = False
  # Return the winner if found
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  # Return None if there's no winner
  else:
    return None


# Check for a tie in the game
def check_for_tie():
  # Access global variables
  global is_game_active
  # If the board is full
  if "-" not in board:
    is_game_active = False
    return True
  else:
    return False


# Switch the current player from X to O, or O to X
def flip_player():
  # Access the global variable
  global current_player
  # Change the current player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"


# Start the game execution
play_game()
