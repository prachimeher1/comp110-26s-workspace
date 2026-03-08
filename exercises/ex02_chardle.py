"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730669446"


def input_word() -> str:
    """Function will ask user for a 5 character word."""
    #ask user for word input
    word: str = input("Enter a 5-character word: ")
    #check word length
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")    
        exit ()
    return word

def input_letter() -> str:
    """Function will ask user for a single character."""
    
    #ask user for letter input
    letter: str = input("Enter a single character: ")
    #check letter length
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter

def contains_char(word: str, letter: str) -> None:
    """Function will check if the single character is found in the 5 character word."""
    #tell user what the program is searching for
    print(f"Searching for {letter} in {word}")
    
    #checking every index of the word for the letter and counting how many times it is found
    count: int = 0
    if word[0] == letter:
        count += 1
        print(f"{letter} found at index 0")
    if word[1] == letter:
        count += 1
        print(f"{letter} found at index 1")
    if word[2] == letter:
        count += 1
        print(f"{letter} found at index 2")
    if word[3] == letter:
        count += 1
        print(f"{letter} found at index 3")
    if word[4] == letter:
        count += 1
        print(f"{letter} found at index 4")
    #printing summary 
    if count == 0:
        print(f"No instances of {letter} found in {word}")
    if count == 1:
        print(f"1 instance of {letter} found in {word}")
    else:
        print(f"{count} instances of {letter} found in {word}")
def main () -> None:
    """Main function that calls all other functions."""
    contains_char(word=input_word(), letter=input_letter())

if __name__ == "__main__":
    main()