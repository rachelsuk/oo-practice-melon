class Player:
    def __init__(self, game_piece, name):
        self.game_piece = game_piece
        self.name = name


class Move:
    def __init__(self, author, position):
        self.author = author
        self.position = position

class Board:
    
    def __init__(self):
        self.moves = {
            'a':["a0","a1","a2"],
            'b':["b0","b1","b2"],
            'c': ["c0","c1","c2"]
            }

    def display(self):
        print(self.moves['a'])
        print(self.moves['b'])
        print(self.moves['c'])
        

    def add_move(self, player, move):
        while True:
            board_row = move[0].lower()
            board_col = int(move[1])
            if self.moves[board_row][board_col] == 'x'or self.moves[board_row][board_col] == 'o':
                print('That spot is already taken!')
                move = input(f'{player.name}, where would you like to play your move? ')
            else:
                self.moves[board_row][board_col] = player.game_piece
                break

class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.game_pieces = {player1.game_piece: self.player1, player2.game_piece: self.player2}
    
def win_game(game):
    win_game = False
    for key in game.board.moves:
        if game.board.moves[key][0] == game.board.moves[key][1] == game.board.moves[key][2]:
            win_game = True
            game_piece = game.board.moves[key][0]
            
    for i in range(3):
        if game.board.moves['a'][i] == game.board.moves['b'][i] == game.board.moves['c'][i]:
            win_game = True
            game_piece = game.board.moves['a'][i]
    
    if game.board.moves['a'][0] == game.board.moves['b'][1] == game.board.moves['c'][2]:
            win_game = True
            game_piece = game.board.moves['a'][0]

    if game.board.moves['a'][2] == game.board.moves['b'][1] == game.board.moves['c'][0]:
            win_game = True
            game_piece = game.board.moves['a'][2]

    if win_game == True:
        print(f'{game.game_pieces[game_piece].name} won the game!')

    return win_game


p1_name = input('What is player one\'s name? ')
p1_game_piece = input(f'Is {p1_name} playing as "x" or "o": ')
p2_name = input('What is player two\'s name? ')
if p1_game_piece.lower() == "x":
    p2_game_piece = "o"
elif p1_game_piece.lower() == "o":
    p2_game_piece = "x"
board = Board()
p1 = Player(p1_game_piece,p1_name)
p2 = Player(p2_game_piece,p2_name)
game = Game(board, p1, p2)
board.display()

end_game = False
while not end_game:
    p1_move = input(f'{p1_name}, where would you like to play your move? ')
    board.add_move(p1, p1_move)
    board.display()
    if win_game(game) == True:
        end_game = True
        break
    p2_move = input(f'{p2_name}, where would you like to play your move? ')
    board.add_move(p2, p2_move)
    board.display()
    if win_game(game) == True:
        end_game = True
    


    

    