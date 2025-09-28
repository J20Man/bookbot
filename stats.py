def count_words(bk_text):
    #this counts the amount of letters there are total
    text = bk_text.split()
    count = 0

    for words in text:
        count +=1
    return count

def char_count(bk_text):
    #this counts how many of each char there is and adds it into a dictionary
    chars = {}
    for c in bk_text:
        lower_c = c.lower()
        if lower_c in chars:
            chars[lower_c] += 1
        else:
            chars[lower_c] = 1
    return chars

def makes_list(book_txt):
    to_sort = []
    for ch, count in book_txt.items():
        if ch.isalpha():
            to_sort.append({"char": ch, "num": count})
    return to_sort
    
def sort_on(item):
    return item["num"]
    
def dict_sort(to_sort):
    to_sort.sort(reverse=True, key=sort_on)
    return to_sort