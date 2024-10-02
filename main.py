def main():
    book_path = "books/frankenstein.txt"
    whole_text = get_book_text(book_path)
    count_of_words = word_count(whole_text)
    print(count_of_words)
    


def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    count = 0
    for i in words:
        count +=1
    return count


main()