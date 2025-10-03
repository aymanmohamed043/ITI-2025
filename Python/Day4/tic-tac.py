# tic_tac_toe.py
import random

class Player:
    """Base Player class"""
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        raise NotImplementedError("Subclasses must implement this method")


class HumanPlayer(Player):
    """Human player gets input from user"""
    def make_move(self, board):
        while True:
            try:
                pos = int(input(f"{self.name} ({self.symbol}), enter your move (1-9): "))
                if pos < 1 or pos > 9:
                    print("Invalid position! Choose 1-9.")
                    continue
                if board.update(pos, self.symbol):
                    break
                else:
                    print("That spot is already taken, try again.")
            except ValueError:
                print("Please enter a valid number between 1-9.")


class ComputerPlayer(Player):
    """Computer chooses random available move"""
    def make_move(self, board):
        available_moves = [i for i in range(1, 10) if board.is_empty(i)]
        pos = random.choice(available_moves)
        print(f"Computer ({self.symbol}) chooses position {pos}")
        board.update(pos, self.symbol)


class Board:
    """Game board class"""
    def __init__(self):
        self._grid = [" "] * 9  # private grid with 9 cells

    def display(self):
        print(self)

    def update(self, position, symbol):
        """Update board if cell is empty"""
        if self._grid[position - 1] == " ":
            self._grid[position - 1] = symbol
            return True
        return False

    def is_empty(self, position):
        return self._grid[position - 1] == " "

    def check_winner(self, symbol):
        """Check if a player has won"""
        win_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        return any(all(self._grid[i] == symbol for i in combo) for combo in win_positions)

    def is_full(self):
        return " " not in self._grid

    def __str__(self):
        """String representation of the board"""
        return (f"\n"
                f" {self._grid[0]} | {self._grid[1]} | {self._grid[2]} \n"
                f"---+---+---\n"
                f" {self._grid[3]} | {self._grid[4]} | {self._grid[5]} \n"
                f"---+---+---\n"
                f" {self._grid[6]} | {self._grid[7]} | {self._grid[8]} \n")


class Game:
    """Main game controller"""
    def __init__(self):
        self.board = Board()
        self.players = []
        self.current_turn = 0

    def setup(self):
        print("Welcome to Tic-Tac-Toe!")
        choice = input("Do you want to play with a friend (1) or vs computer (2)? ")

        if choice == "1":
            name1 = input("Enter Player 1 name: ")
            name2 = input("Enter Player 2 name: ")
            self.players = [HumanPlayer(name1, "X"), HumanPlayer(name2, "O")]
        else:
            name1 = input("Enter your name: ")
            self.players = [HumanPlayer(name1, "X"), ComputerPlayer("Computer", "O")]

    def switch_turns(self):
        self.current_turn = 1 - self.current_turn

    def play(self):
        self.setup()
        self.board.display()

        while True:
            player = self.players[self.current_turn]
            player.make_move(self.board)
            self.board.display()

            if self.board.check_winner(player.symbol):
                print(f"🎉 {player.name} wins!")
                break
            elif self.board.is_full():
                print("It's a draw!")
                break

            self.switch_turns()


if __name__ == "__main__":
    game = Game()
    game.play()
    print("Thanks for playing!")# End of tic_tac_toe.py