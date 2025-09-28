def main():
    from stats import count_words
    from stats import char_count
    from stats import makes_list
    from stats import dict_sort
    #from stats import sorted_text
    file = "books/frankenstein.txt"
    text = get_book_text(file)

    total_chars = count_words(text)
    char_count_dict = char_count(text)
    new_list = makes_list(char_count_dict)
    sorted_dict = dict_sort(new_list)

    #print(sorted_dict)
    print(f"============ BOOKBOT ============")
    print("Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {total_chars} total words")
    print("--------- Character Count -------")
    print(sorted_dict)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()



main()