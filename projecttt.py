
board = [' ' for _ in range(9)]
current_player = 'X'
game_over = False


def print_board():
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def check_game_over():
    global game_over
    for i in range(0, 9, 3):
       
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            game_over = True
            return True
        
        if board[i // 3] == board[i // 3 + 3] == board[i // 3 + 6] != ' ':
            game_over = True
            return True

    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        game_over = True
        return True
    
    if ' ' not in board:
        game_over = True
        return True
    return False


def make_move():
    global current_player
    while True:
        try:
            move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = current_player
                break
            else:
                print("That position is already taken. Try again.")
        except ValueError:
            print("Invalid input. Try again.")
        except IndexError:
            print("Invalid position. Try again.")
    
    print_board()
    current_player = 'X' if current_player == 'O' else 'O'


while not game_over:
    make_move()


if ' ' not in board:
    print("It's a draw!")
else:
    print(f"Player {current_player} wins!")
