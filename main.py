def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_char = char_count(text)
    print(num_char)
    


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
        if characters not in char: 
            char[characters] = 1
        else:
            char[characters] += 1
    return char




main()