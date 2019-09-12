def count0(wordlist):
    """Using Python str.count()."""
    word_counting = []  # Save the word counting as tuple (pair).
    for word in wordlist:
        word_count = wordlist.count(word)
        word_counting.append((word, word_count))

    max_count = 0
    for word, count in word_counting:  # Get the max_count and the max_word.
        if count > max_count:
            max_count = count
            max_word = word

    return max_word, max_count


def main():
    pass


if __name__ == '__main__':
    main()
