## Algoritmo 1

```
func count1(words)
    max_count = 0
    for i = 0 to words.length - 1
        word = words[i]
        word_count = 0
        for j = 0 to words.length
            if words[j] == word
                word_count += 1
            if word_count > max_count
                max_count = word_count
                max_word = word
    return max_word, max_count
```

## Algoritmo 2

```
func count2(words)
    max_count = 0
    for i = 0 to words.length - 1
        word = words[i]
        word_count = 1
        for j = i + 1 to words.length
            if words[j] == word
                word_count += 1
            if word_count > max_count
                max_count = word_count
                max_word = word
    return max_word, max_count
```

## Algoritmo 3

```
func count3(words)
    max_count = 0
    for i = 0 to words.length - 1
        word = words[i]
        word_count = words.count(word)
        if word_count > max_count
            max_count = word_count
            max_word = word
    return max_word, max_count
```

## Algoritmo 4

```
func count4(words)
    max_sequence = 0
    sequence_size = 1
    words.sort()
    for i = 0 to words.length - 2
        word = words[i]
        if word == words[i+1]
            sequence_size += 1
            if sequence_size > max_sequence
                max_sequence = sequence_size
                max_word = word
        else
            sequence_size = 1
    return max_word, max_sequence
```

## Algoritmo 5

```
func count5(words)
    word_count_map = {}
    for i = 0 to words.length - 1
        word = words[i]
        if word in dict
            dict[word] += 1
        else
            dict[word] = 1

    max_count = 0
    for word, count in word_count_map
        if count > max_count
            max_count = count
            max_word = word

    return max_word, max_count
```
