"""EX03 - Wordle!"""

__author__ = "730669446"

GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
WHITE_BOX: str = "\U00002B1C"

def input_guess (word_length: int) -> str:
    """Asking the user for a guess that is of the correct length"""
    #inital user prompt
    guess: str = input(f"Enter a {word_length} character word: ")

    #looping the question until the correct length word is put in
    while (len(guess) != word_length):
        guess = input(f"That wasn't {word_length} chars! Try again: ")
    return guess

def contains_char (secret_word: str, char_search: str) -> bool:
    """Return true if char_search is found in the secret_word"""
    assert len(char_search) == 1
    i: int = 0

    #indexing through each character 
    while i < len(secret_word):
        if secret_word[i] == char_search:
            return True
        i = i + 1
    return False

def emojified (guess: str, secret: str) -> str:
    """Returns an emoji string comparing "guess" to secret word"""
    assert len(guess) == len(secret)

    result: str = ""
    i: int = 0

    while (i < len(secret)):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i = i + 1 

    return result 

def main (secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    turn: int = 1
    max_turns: int = 6
    won: bool = False

    #the game
    while turn <= max_turns and not won:
        print(f"=== Turn {turn}/{max_turns} ===")

        guess: str = input_guess(len(secret))

        print(emojified(guess, secret))

        if guess == secret:
            won = True
        else:
            turn = turn + 1
        
    #after the game
    if won:
        print(f"You won in {turn}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")
    


if __name__ == "__main__":
    main(secret="codes")