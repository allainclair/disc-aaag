import random

CONS = 'bcdfghjklmnpqrstvxyz'
VOGS = 'aeiou'


def single_word_generator(min_=1, max_=3):
    # Definindo numero de silabas.
    inteval = range(min_, max_+1)
    num_silabas = random.choice(inteval)
    # print(num_silabas)

    # Criar silaba
    word = ''
    for _ in range(num_silabas):
        consoante = random.choice(CONS)
        vogal = random.choice(VOGS)
        word += consoante + vogal
    return word


def word_generator(num_words=100, min_silabas=1, max_silabas=3):
    list_ = []
    for _ in range(num_words):
        list_.append(single_word_generator(min_silabas, max_silabas))
    return list_


def main():
    words = word_generator(50, min_silabas=1, max_silabas=3)
    print(words)
    print('Len:', len(words))


if __name__ == '__main__':
    main()
