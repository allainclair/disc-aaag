[https://malbarbo.pro.br/arquivos/2012/1747/01-introdução.pdf](https://malbarbo.pro.br/arquivos/2012/1747/01-introdução.pdf)

## Análise matemática da eficiência dos algoritmos

### Algoritmo 1

```
func count1(words)
    max_count = 0
    for i = 0 to words.length - 1
        word = words[i]
        word_count = 0
        for j = 0 to words.length - 1
            if words[j] == word
                word_count += 1
            if word_count > max_count
                max_count = word_count
                max_word = word
    return max_word, max_count
```

### Algoritmo 2

```
func count2(words)
    max_count = 0
    for i = 0 to words.length - 1
        word = words[i]
        word_count = 1
        for j = i + 1 to words.length - 1
            if words[j] == word
                word_count += 1
            if word_count > max_count
                max_count = word_count
                max_word = word
    return max_word, max_count
```


[https://malbarbo.pro.br/arquivos/2012/1747/02-conceitos-básicos.pdf](https://malbarbo.pro.br/arquivos/2012/1747/02-conceitos-básicos.pdf)
