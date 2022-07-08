import random
import re
from copy import deepcopy
from wordle.lists import WORDLE_ANSWERS, WORDLE_GUESSES
from wordle.play import Solver
from wordle.core.result import ensure_result, is_winner
from wordle.core.gameplay import filter_word_list, get_result


class WordleSolver(Solver):
    def __init__(self, answer, guess, interactive=False):
        self.answers = WORDLE_ANSWERS
        self.guesses = WORDLE_GUESSES
        self.guess = guess
        self.answer = answer
        self.interactive = interactive

    def gather_response(self, strlen=5):
        if self.interactive:
            resp = input("What's the result? ( _ = black, ? = yellow, ! = green ) ")
            match = re.match(r'^[!?_]{' + str(strlen) + '}$', resp)
            if not match:
                print("Invalid response string, try again")
                return self.gather_response(strlen)
            return ensure_result(resp)
        return get_result(self.guess, self.answer)

    def solve(self):
        notoutofguesses = 6
        remaining_words = deepcopy(self.answers)

        while notoutofguesses:
            if len(remaining_words) == 0:
                print("I give up")
                break
            print(f"{len(remaining_words)} valid words remain")
            print(f"remaining: {remaining_words} ")

            GuessingAlgorithm = self.get_guessing_algorithm(remaining_words)
            print(f"using {GuessingAlgorithm.__name__}")
            self.guess = GuessingAlgorithm.guess(remaining_words)
            notoutofguesses -= 1
            certainty = round(1.0 / len(remaining_words) * 100)
            print(f"Guess: {self.guess.upper()} ({certainty}% certain)")
            result = self.gather_response(len(remaining_words[0]))
            if is_winner(result):
                print(f"Oh yeah, {6 - notoutofguesses} guesses")
                break
            remaining_words = filter_word_list(remaining_words, self.guess, result)
        return notoutofguesses


def main():
    import argparse
    dictionary = WORDLE_ANSWERS
    answer = dictionary[random.randrange(len(dictionary))]
    parser = argparse.ArgumentParser(
        description="Wordle Play"
    )
    parser.add_argument(
        "-p",
        "--playmyself",
        default=False,
        action="store_true",
        help="Default: Play myself. Ill pick a random word and attempt to guess"
    )
    parser.add_argument(
        "-a",
        "--answer",
        default=answer,
        # type=argparse.FileType('w', encoding='UTF-8'),
        help="Enter a 5 letter word to guess"
    )
    parser.add_argument(
        "-i",
        "--interactive",
        default=False,
        action="store_true",
        help="Interactive Results Entry (essentially you play the middle man by entering program guesses and reporting results)",
    )
    args = parser.parse_args()
    answer = args.answer
    interactive = args.interactive
    print(f"The answer is {answer.upper()}")
    solver = WordleSolver(answer, "later", interactive)
    solver.solve()


if __name__ == "__main__":
    main()
