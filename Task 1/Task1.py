class RedBlueNimGame:
    def __init__(self, num_red, num_blue, version, first_player, depth):
        self.num_red = num_red
        self.num_blue = num_blue
        self.version = version
        self.current_player = first_player
        self.depth = depth
        self.human_score = 0
        self.computer_score = 0

    def display_state(self):
        print(f"Red marbles: {self.num_red}, Blue marbles: {self.num_blue}")
        print(f"Current player: {self.current_player}")

    def is_game_over(self):
        return self.num_red == 0 and self.num_blue == 0

    def calculate_score(self):
        if self.version == 'standard':
            return 1 if self.is_game_over() else -1
        else:  # misère
            return -1 if self.is_game_over() else 1

    def make_move(self, red_taken, blue_taken):
        self.num_red -= red_taken
        self.num_blue -= blue_taken

    def human_move(self):
        self.display_state()

        # Ensure that only 1 or 2 marbles are taken
        while True:
            red_taken = int(input("Number of red marbles to take (1 or 2): "))
            blue_taken = int(input("Number of blue marbles to take (1 or 2): "))

            if (red_taken > 2 or red_taken < 0) or (blue_taken > 2 or blue_taken < 0):
                print("Invalid input! You can only take 1 or 2 marbles. Please try again.")
            elif red_taken == 0 and blue_taken == 0:
                print("You must take at least one marble! Please try again.")
            else:
                break  # Valid input

        self.make_move(red_taken, blue_taken)

    def computer_move(self):
        self.display_state()
        best_score = -float('inf')
        best_move = None

        for red in range(0, 3):  # Computer can only take 1 or 2 marbles
            for blue in range(0, 3):
                if red == 0 and blue == 0:
                    continue
                if self.num_red >= red and self.num_blue >= blue:
                    self.make_move(red, blue)
                    score = self.minimax(self.depth, False, -float('inf'), float('inf'))
                    self.make_move(-red, -blue)
                    if score > best_score:
                        best_score = score
                        best_move = (red, blue)

        red_taken, blue_taken = best_move
        print(f"Computer takes {red_taken} red marbles and {blue_taken} blue marbles.")
        self.make_move(red_taken, blue_taken)

    def minimax(self, depth, is_maximizing, alpha, beta):
        if self.is_game_over() or depth == 0:
            return self.calculate_score()

        if is_maximizing:
            max_eval = -float('inf')
            for red in range(0, 3):  # Computer can only take 1 or 2 marbles
                for blue in range(0, 3):
                    if red == 0 and blue == 0:
                        continue
                    if self.num_red >= red and self.num_blue >= blue:
                        self.make_move(red, blue)
                        eval = self.minimax(depth - 1, False, alpha, beta)
                        self.make_move(-red, -blue)
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = float('inf')
            for red in range(0, 3):  # Human can only take 1 or 2 marbles
                for blue in range(0, 3):
                    if red == 0 and blue == 0:
                        continue
                    if self.num_red >= red and self.num_blue >= blue:
                        self.make_move(red, blue)
                        eval = self.minimax(depth - 1, True, alpha, beta)
                        self.make_move(-red, -blue)
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

def play_game(num_red, num_blue, version, first_player, depth):
    game = RedBlueNimGame(num_red, num_blue, version, first_player, depth)
    game.display_state()

    while not game.is_game_over():
        if game.current_player == 'human':
            game.human_move()
            game.current_player = 'computer'
            game.human_score += 1  # Increment human score
        else:
            game.computer_move()
            game.current_player = 'human'
            game.computer_score += 1  # Increment computer score

        game.display_state()

    print("Game over!")
    print(f"Final Score - Human: {game.human_score}, Computer: {game.computer_score}")
    score = game.calculate_score()
    if score == 1:
        print("Human wins!" if game.version == 'standard' else "Computer wins!")
    else:
        print("Computer wins!" if game.version == 'standard' else "Human wins!")

if __name__ == "__main__":
    num_red = int(input("Enter the number of red marbles: "))
    num_blue = int(input("Enter the number of blue marbles: "))
    version = input("Enter the game version (standard/misere): ").strip().lower()
    first_player = input("Who plays first (human/computer): ").strip().lower()
    depth = 5  # Set depth for AI decision-making

    play_game(num_red, num_blue, version, first_player, depth)