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
    start = time.perf_counter()
    words = word_generator(8_000_000, min_silabas=1, max_silabas=2)
    print(f'Time to generate words: {time.perf_counter() - start}')
    # name_function_map = {
    #     'count1': count1, 'count2': count2, 'count3': count3, 'count4': count4,
    #     'count5': count5}

    # name_function_map = {'count1': count1, 'count2': count2, 'count3': count3}

    name_function_map = {'count4': count4, 'count5': count5}

    print()
    for name, func in name_function_map.items():
        start_time = time.perf_counter()
        word, count = func(words)
        print(f'{name} time: {time.perf_counter() - start_time}')


# def test_random_words_set():
#     word_base_size = 1_000_000
#     for i in range(11, 51):
#         print('word_base_size:', word_base_size*i)
#         words = word_generator(word_base_size*i, min_silabas=1, max_silabas=3)
#         for j in range(3):
#             print('Instance:', j)
#             # name_function_map = {
#             #     'count1': count1, 'count2': count2, 'count3': count3, 'count4': count4,
#             #     'count5': count5}
#
#             name_function_map = {'count4': count4, 'count5': count5}
#
#             # name_function_map = {'count4': count4, 'count5': count5}
#
#
#             for name, func in name_function_map.items():
#                 start_time = time.perf_counter()
#                 word, count = func(words)
#                 print(f'{name} time: {time.perf_counter() - start_time}')
