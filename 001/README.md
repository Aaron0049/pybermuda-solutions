Hello, I am somewhat of a Python novice so my solutions may lack in readability and optimization.

My solution works by taking the returned clue, iterating through the word list, and removing words that cannot be correct based on the returned clue. It will then pick a random word from the remaining words to use as a new guess and repeat until the returned clue is "🟩🟩🟩🟩🟩".

The function sometimes takes more than 6 guesses. If you are looking to minimize the number of guesses, I would try a better strategy for picking the next guess than random.choice() from the word list.

I also made a change to the .guess method. It was returning a string of 9 characters because it was adding spaces between the squares, and I removed the added spaces for simplicity.
