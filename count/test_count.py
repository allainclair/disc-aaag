from .count import count0


def test_count():
    list1 = ['joao', 'maria', 'joao', 'maria', 'francisco']
    max_word, max_count = count0(list1)
    assert max_word == 'joao'
    assert max_count == 2


def test_random_words():
    pass
