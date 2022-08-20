import random


class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        new_data = random.randint(1, 6)
        self._value = new_data
        return new_data


class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.roll()


class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("=" * 30)
        print("Welcome to Roll The Dice!")
        print("=" * 30)
        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break

    def play_round(self):
        self.print_round_welcome()

        # Rolling the dice
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        # Show the values
        self.show_dice(player_value, computer_value)

        # Checking the wiiner and loser
        if player_value > computer_value:
            print("You won the round")
            self.update_counter(winner=self._player, loser=self._computer)
        elif computer_value > player_value:
            print("The PC won this round!")
            self.update_counter(winner=self._computer, loser=self._player)
        else:
            print("It's a tie")

        self.show_counters()

    def print_round_welcome(self):
        print("-------- New Round --------")
        input("Press any key to roll the dice")

    def show_dice(self, player_value, computer_value):
        print(f"Your die: {player_value}")
        print(f"Computer die: {computer_value}")

    def update_counter(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def show_counters(self):
        print(f"Your counter: {self._player.counter}")
        print(f"PC counter: {self._computer.counter}")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False

    def show_game_over(self, winner):
        if winner.is_computer:
            print("Game Over! PC won")
        else:
            print("Game Over! You won")


my_die = Die()
computer_die = Die()

my_player = Player(my_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_player)

game.play()
