import random


class Tambola:

    __range_start: int

    __range_end: int

    __numbers_left: int

    __generatedNumbers: set

    def __init__(self):
        self.__generatedNumbers = set()

    def set_range(self, start: int, end: int) -> None:
        self.__range_start = start
        self.__range_end = end
        self.__numbers_left = end - start + 1

    def numbers_left_to_generate(self) -> bool:
        if self.__numbers_left == 0:
            return False

        return True

    def generate_next_unique_number(self) -> int:
        while True:
            unique_number = random.randint(self.__range_start, self.__range_end)
            if unique_number not in self.__generatedNumbers:
                self.__generatedNumbers.add(unique_number)
                self.__numbers_left -= 1
                return unique_number


