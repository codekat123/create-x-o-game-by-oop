import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
class player:
    def __init__(self):
        self.name = ""
        self.symbol = ""
        self.score = 0
    def set_name(self):
        while True:
            name = input("enter your name (only letter): ")
            if name.isalpha():
                self.name = name
                break
            print("enter only letter")

    def set_symbol(self):
        while True:
            symbol = input(f"{self.name}, enter your symbol (only letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("enter only letter and only one letter")
class Menu:
    def display_menu(self):
        while True:
            print("welcome to tic tac toe game")
            choose = """
                1 => start game 
                2 => exit
                """
            choice = input(choose)
            if choice == "1" or choice == "2":
                return choice
            print("invalid number. please you choose 1 or 2")       
    def end_game(self):
        while True:
            choose = """
            1 => play again
            2 => exit"""            
            choice = input(choose)
            if choice == "2" or choice == "1":
                return choice 
            print("invalid number. please you choose 1 or 2")        
class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i: i + 3]))
            if i < 6:
                print("-" * 5)

    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def reset_board(self):
        self.board = [str(i)for i in range(1,10)]
class game :
    def __init__(self):
        self.player = [player(), player()]
        self.menu = Menu()
        self.board = Board()
        self.current_player = 0
    def startgame(self):
        choice = self.menu.display_menu()
        if choice == "1":
            self.setup()
            self.game_play()
        elif choice == "2":
            self.quit()
    def game_play(self):
        while True :
            self.play_turn()
            if self.win() or self.draw():
                choose = self.menu.end_game()
                if choose == "1":
                    self.restart_game()
                elif choose == "2":
                    self.quit()
                    break    
            clear_screen()
    def setup(self):
        for number,player in enumerate(self.player, start = 1):
            print(f"{number}player's turn, enter your details")
            player.set_name()
            player.set_symbol()
    def quit(self):
        print ("thank you for playing")
    def draw(self):
      return all( not cell.isdigit() for cell in self.board.board)
    def win(self):
        check = [
    [0, 1, 2],   
    [3, 4, 5],
    [6, 7, 8],  
    [0, 3, 6],  
    [1, 4, 7],  
    [2, 5, 8],  
    [0, 4, 8],  
    [2, 4, 6]   ]
        for i in check:
            if self.board.board[i[0]] == self.board.board[i[1]] == self.board.board[i[2]] and not self.board.board[i[0]].isdigit():
              self.player[self.current_player] += 1
              return True
        return False      
    def play_turn(self):
        players = self.player[self.current_player]
        self.board.display_board()
        clear_screen()
        while True :
            try:
                print(f"{players.name}'s your turn")
                cell = int(input("choose a cell"))
                if 1 <= cell <= 9 and self.board.update_board(cell,players.symbol):
                    break
                else :
                    print("invalid move")
            except:
                print("invalid value")
        self.switch()        
    def switch(self):
        self.current_player = 1 - self.current_player                    
    def restart_game(self):
        self.board.reset_board()
        self.current_player = 0
        self.game_play()
        clear_screen() 
print(game().game_play())