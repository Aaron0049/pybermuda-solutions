"""
WORDLE SOLVER

https://www.nytimes.com/games/wordle/index.html

Your task is to create a `solve_wordle` function that takes in a wordle puzzle
and an initial guess, solves the puzzle, and returns the word.

A `Wordle` class has been provided for you, which has a `guess` method that
takes in a word and returns a clue. The clue is a string of 5 characters,
where each character is one of:
- 🟩: The letter is in the correct position
- 🟨: The letter is in the word, but not in the correct position
- ⬜: The letter is not in the word

With 'proper' Wordle, you would have 6 guesses to solve the puzzle. However,
this restriction has not been implemented here. You can make as many guesses as
you like (though in all likelihood, your `solve_wordle` function won't need
more than 6).

Obviously, your `solve_wordle` function should not access the `Wordle` object's
`.secret` attribute directly. That would be cheating. You should only use the 
`.guess` method to get clues.

BONUS:
At the moment, initialising a `Wordle` object with a word results in one being
chosen at random from `WORDS`. You could change this behaviour to use the 
NY Times API to pull today's word, add it to `WORDS` if it isn't already there,
and *then* solve the puzzle.

The API URL is:
https://www.nytimes.com/svc/wordle/v2/YYYY-MM-DD.json
(replacing YYYY-MM-DD with today's date)
"""
from urllib.request import urlopen
from random import choice
from timeit import default_timer as timer
import requests
from datetime import date

WORD_LIST_URL = "https://gist.githubusercontent.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b/raw/45c977427419a1e0edee8fd395af1e0a4966273b/wordle-answers-alphabetical.txt"


with urlopen(WORD_LIST_URL) as f:
    WORDS = f.read().decode("utf-8").upper().splitlines()

def word_from_today() -> str:
    dt_string = date.today().strftime("%Y-%m-%d")
    url = f"https://www.nytimes.com/svc/wordle/v2/{dt_string}.json"

    response = requests.get(url).json()

    word = response["solution"].upper()

    if word not in WORDS:
        WORDS.append(word)

    return word

class Wordle:
    def __init__(self, word: str | None = None) -> None:
        self._secret = word or word_from_today()
        self.clues: list[str] = []

    def guess(self, word: str) -> str:
        word = word.upper()
        assert len(word) == 5, "Word must be 5 letters long"

        clue: str = ["⬜"] * 5

        for i, letter in enumerate(word):
            if letter in self._secret:
                if letter == self._secret[i]:
                    clue[i] = "🟩"
                else:
                    clue[i] = "🟨"

        self.clues.append("".join(clue))

        return self.clues[-1]
    
def solve_wordle(wordle: Wordle, initial_guess: str) -> str:
    tlist = tuple(WORDS)
    hint = wordle.guess(initial_guess)
    print("guessing   " + initial_guess)
    print(hint + "   hint returned")
    while hint != "🟩🟩🟩🟩🟩":
        for x in tlist:
            for i in range(5):
                if hint[i] == "⬜" and initial_guess[i] in x:
                    WORDS.remove(x)
                    break
                elif hint[i] == "🟩" and initial_guess[i] != x[i]:
                    WORDS.remove(x)
                    break
                elif hint[i] == "🟨" and initial_guess[i] not in x:
                    WORDS.remove(x)
                    break
                elif hint[i] == "🟨" and initial_guess[i] == x[i]:
                    WORDS.remove(x)
                    break
        tlist = tuple(WORDS)
        initial_guess = choice(WORDS)
        hint = wordle.guess(initial_guess)
        print("guessing   " + initial_guess)
        print(hint + "   hint returned")
    return initial_guess
   
if __name__ == "__main__":
    start = timer()
    game = Wordle()
    solution = solve_wordle(game, "SLATE")
    end = timer()
    print(f"The solution is {solution}")
    print(end - start)
