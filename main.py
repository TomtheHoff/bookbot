def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_char = char_count(text)
    output(book_path, num_words, num_char)
    


def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    count = 0
    for i in words:
        count +=1
    return count

def char_count(text): 
    lowered_text = text.lower()
    char = {}
    for characters in lowered_text:
        if characters.isalpha():
            if characters not in char: 
                char[characters] = 1
            else:
                char[characters] += 1
    return char


def output(book_path, word_count, char_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    for character, count in sorted_chars:
        print(f"The '{character}' character was found {count} times")
    print("--- End report ---")



main()