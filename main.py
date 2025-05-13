import sys

from stats import get_num_words
from stats import get_char_count
from stats import get_sorted_list


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        char_counts = get_char_count(book_text)
        num_words = get_num_words(book_text)
        sorted_list = get_sorted_list(char_counts)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for i in range(0, len(sorted_list)):
            if sorted_list[i]["char"].isalpha():
                print(f"{sorted_list[i]['char']}: {sorted_list[i]['num']}")
        print("============= END ===============")


main()
