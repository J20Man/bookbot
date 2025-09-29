import sys

def main():
    
    
    from stats import count_words
    from stats import char_count
    from stats import makes_list
    from stats import dict_sort
    
    text = get_book_text()
    
    total_chars = count_words(text)
    char_count_dict = char_count(text)
    new_list = makes_list(char_count_dict)
    sorted_dict = dict_sort(new_list)

    print("============ BOOKBOT ============")
    print("Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {total_chars} total words")
    print("--------- Character Count -------")
    
    for item in sorted_dict:
        ch = item["char"]
        count = item["num"]
        print(f"{ch}: {count}:")


def get_book_text():
    if len(sys.argv) >= 2:
        filepath = sys.argv[1]
        print("calculating file", filepath)
        with open(filepath) as f:
            return f.read()
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    


main()