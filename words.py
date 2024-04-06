    
def print_upper_words(words, must_start_with="0"):
    """For a list of words, print out each word on a separate line, but in all uppercase.
    
    Optional: add condition to only print words that start with specific letters using must_start_with
    For example:
        ["How", "now", "brown", "cow"], ["h", "c"] or {"h", "c"}

    Should Print out:
        HOW
        COW
    """

    if(must_start_with == "0"):
        for word in words:
            print(word.upper())
    else:
        for word in words:
            for letter in must_start_with:
                if(word.upper().startswith(letter.upper())):
                    print(word.upper())

print_upper_words(["How", "Now", "Brown", "Cow"])
print_upper_words(["How", "Now", "Brown", "Cow"], must_start_with={"c", "h"})