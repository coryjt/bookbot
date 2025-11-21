from stats import get_num_words, get_chars_dict, sort_dict
import sys


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print(sys.argv)
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_dict = sort_dict(chars_dict)
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
""")
    for item in sorted_dict:
        char = item["char"]
        num = item["num"]
        if not char.isalpha():
            continue
        print(f"{char}: {num}")

    print("============= END ===============")

if __name__ == "__main__":
    main()