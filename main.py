def main():
    from stats import count_words
    from stats import char_count
    file = "books/frankenstein.txt"
    
    print(char_count(get_book_text(file)))


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()





main()