import math

board = [' ' for _ in range(9)]
player = 'X'
computer = 'O'

def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def is_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_board_full(board):
    return ' ' not in board

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, computer):
        return 1
    if is_winner(board, player):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move] = computer
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move] = player
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def computer_move():
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = computer
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = computer

def player_move():
    move = int(input("Enter your move (0-8): "))
    if board[move] == ' ':
        board[move] = player
    else:
        print("Invalid move! Try again.")
        player_move()

def play_game():
    while True:
        print_board(board)
        if is_winner(board, computer):
            print("Computer wins!")
            break
        if is_winner(board, player):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        player_move()
        if not is_board_full(board) and not is_winner(board, player):
            computer_move()

play_game()
