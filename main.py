def word_count(str):
    return len(str.split())

def letter_count(str):
    letters = {}

    for l in str.lower():
        if l in letters:
            letters[l] += 1
        elif l.isalpha():
            letters[l] = 1

    return letters


with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(file_contents)} words found in the document\n")
    letters = list(letter_count(file_contents).items())
    letters.sort(key=lambda x: x[1], reverse=True)
    for letter in letters:
        print(f"The '{letter[0]}' character was found {letter[1]} times")
    print("--- End report ---")