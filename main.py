BOOK_PATH = "books/frankenstein.txt"


def main():
    with open(BOOK_PATH) as f:
        file_contents = f.read()
    counts = count_chars(file_contents)
    print(f"--- Begin report of {BOOK_PATH} ---")
    print(f"{get_words(file_contents)} words found in the document")
    for c in sorted(counts, key=lambda x: -counts[x]):
        print(f"The {c} character was found {counts[c]} time",
              end="s\n" if counts[c] > 1 else "\n")
    print("--- End report ---")


def get_words(text):
    return len(text.split())


def count_chars(text):
    res = {}
    for c in text.lower():
        if c.isalpha():
            if c in res:
                res[c] += 1
            else:
                res[c] = 1
    return res


main()
