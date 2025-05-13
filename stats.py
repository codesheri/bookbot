def get_num_words(text):
    return len(text.split())


def get_char_count(text):
    words = text.lower()
    char_count = {}

    for char in words:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def sort_on(dict):
    return dict["num"]


def get_sorted_list(char_counts):
    # take the dictionary of characters and their counts and returns a sorted list of dictionaries.
    # Each dictionary should have two key-value pairs: one for the character itself
    # and one for that character's count (e.g. {"char": "b", "num": 4868}).

    list = []

    for char_count in char_counts:
        list.append({"char": char_count, "num": char_counts[char_count]})

    return sorted(list, key=sort_on, reverse=True)
