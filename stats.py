def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(items):
    return items["num"]


def sort_dict(char_dict):
    result = []
    for key in char_dict:
        value = char_dict[key]
        item = {"char": key, "num": value}
        result.append(item)

    result.sort(reverse=True, key=sort_on)
    return result