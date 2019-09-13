import time

from .count import count1, count2, count3, count4, count5
from .wordgenerator import word_generator


def test_simple_count():
    # list1 = ['joao', 'maria', 'joao', 'maria', 'francisco']
    list1 = ['joao', 'maria', 'joao', 'maria', 'francisco', 'joao']
    max_word, max_count = count1(list1)
    assert max_word == 'joao'
    assert max_count == list1.count('joao')

    max_word, max_count = count2(list1)
    assert max_word == 'joao'
    assert max_count == list1.count('joao')

    max_word, max_count = count3(list1)
    assert max_word == 'joao'
    assert max_count == list1.count('joao')

    max_word, max_count = count4(list1)
    assert max_word == 'joao'
    assert max_count == list1.count('joao')

    max_word, max_count = count5(list1)
    assert max_word == 'joao'
    assert max_count == list1.count('joao')


def test_random_words():
    words = word_generator(100_000, min_silabas=1, max_silabas=2)
    # name_function_map = {
    #     'count1': count1, 'count2': count2, 'count3': count3, 'count4': count4,
    #     'count5': count5}

    name_function_map = {'count2': count2, 'count3': count3}

    # name_function_map = {'count4': count4, 'count5': count5}


    for name, func in name_function_map.items():
        start_time = time.perf_counter()
        word, count = func(words)
        print(f'{name} time: {time.perf_counter() - start_time}')
