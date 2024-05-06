def vowels_counter(text):
    vowels = ("A", "E", "I", "O", "U")
    total_vowels = 0
    text = text.upper()
    for vowel in vowels:
        total_vowels += text.count(vowel)
    return total_vowels

if __name__ == "__main__":
    text = input("Enter a text: ")
    print(f"Total vowel in {text} are {vowels_counter(text)}")