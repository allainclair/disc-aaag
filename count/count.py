import collections


def count1(words):
    max_count = 0
    for word1 in words:
        word_count = 0
        for word2 in words:
            if word1 == word2:
                word_count += 1
            if word_count > max_count:
                max_count = word_count
                max_word = word2
    return max_word, max_count


def count2(words):
    """Using words from second for from i + 1."""
    max_count = 0
    for i, word1 in enumerate(words):
        word_count = 1
        for word2 in words[i+1:]:
            if word1 == word2:
                word_count += 1
            if word_count > max_count:
                max_count = word_count
                max_word = word2
    return max_word, max_count


def count3(words):
    """Using Python list.count(string)."""
    word_counting = []  # Save the word counting as tuple (pair).
    max_count = 0
    for word in words:
        word_count = words.count(word)
        if word_count > max_count:
            max_count = word_count
            max_word = word
    return max_word, max_count


def count4(words):
    """Sorting and getting the max subsequence."""
    max_sequence = 0
    sequence_size = 1
    sorted_words = sorted(words)
    max_word = sorted_words[0]  # Caso soh tenha palavras diferentes.
    for i in range(len(sorted_words) - 1):
        if sorted_words[i] == sorted_words[i+1]:
            sequence_size += 1
            if sequence_size > max_sequence:
                max_sequence = sequence_size
                max_word = sorted_words[i]
        else:
            sequence_size = 1
    return max_word, max_sequence


def count5(words):
    """Dictionaries (hash)."""
    word_count_map = collections.defaultdict(int)
    for word in words:
        word_count_map[word] += 1

    max_count = 0
    for word, count in word_count_map.items():
        if count > max_count:
            max_count = count
            max_word = word

    return max_word, max_count


def main():
    pass


if __name__ == '__main__':
    main()
