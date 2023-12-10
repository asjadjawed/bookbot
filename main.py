"""
BookBot for Boot.dev Project
"""


def main():
    """
    main function
    """
    book_path = "books/frankenstein.txt"
    text = get_file_text(book_path)
    num_words = count_words(text)
    letter_counts = count_chars(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    display_letter_report(letter_counts)
    print("--- End report ---")


def display_letter_report(letter_counts):
    """
    Prints only letters sorted by count

    Args:
        letter_counts (dict): a dictionary of character with count
    """
    for char, count in sorted(letter_counts.items(), key=lambda item: item[1], reverse=True):
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")


def count_chars(text):
    """
    count characters in text

    Args:
        text (str): input text

    Returns:
        dict: count of number of characters in text
    """
    letter_counts = {}

    for c in text.lower():
        if c in letter_counts:
            letter_counts[c] += 1
        else:
            letter_counts[c] = 1

    return letter_counts


def count_words(text):
    """
    count words in text

    Args:
        text (str): text to count words

    Returns:
        int: number of words
    """
    return len(text.split())


def get_file_text(path):
    """
    get text from file

    Args:
        path (str): filepath

    Returns:
        str: file text content
    """
    with open(path, 'r', encoding='UTF-8') as f:
        return f.read()


if __name__ == '__main__':
    main()
