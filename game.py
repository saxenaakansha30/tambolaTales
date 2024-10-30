from tambola import Tambola

class Game:

    _player_count: int

    _tambola_game: Tambola

    def __init__(self):
        self._tambola_game = Tambola()

    def play(self) -> None:
        self._tambola_game.set_range(1, 10)

        key = input("Enter n to generate next unique number:\n ")
        while True:
            if not self.entered_next_key(key):
                print("You have ended the game.")
                break

            next_number = self._tambola_game.generate_next_unique_number()
            print(f"Number is {next_number}")

            if not self._tambola_game.numbers_left_to_generate():
                print("All numbers are generated.")
                break

            key = input("Enter n to generate next unique number:\n")

    def entered_next_key(self, key: str) -> bool:
        if key == 'n':
            return True

        return False

    def choose_theme(self) -> None:
        pass

    def add_players(self) -> None:
        pass

    def set_player_count(self, count: int) -> None:
        self._player_count = count
