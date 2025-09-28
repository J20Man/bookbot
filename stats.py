def count_words(bk_text):
    text = bk_text.split()
    count = 0

    for words in text:
        count +=1
    return count

def char_count(bk_text):
    chars = {}
    for c in bk_text:
        lower_c = c.lower()
        if lower_c in chars:
            chars[lower_c] += 1
        else:
            chars[lower_c] = 1
    return chars