import numpy as np


def calc_lev_sim(first_word_, sec_word_):
    lev_matrix = np.zeros(((len(first_word_) + 1), (len(sec_word_) + 1)), dtype=int)

    for i in range(len(first_word_) + 1):
        lev_matrix[i, 0] = i

    for j in range(1, len(sec_word_) + 1):
        lev_matrix[0, j] = j

    for index_first_word in range(1, len(first_word_) + 1):
        for index_sec_word in range(1, len(sec_word_) + 1):
            cost = 0 if first_word_[index_first_word - 1] is sec_word_[index_sec_word - 1] else 1

            lev_matrix[index_first_word, index_sec_word] = min(
                lev_matrix[index_first_word - 1, index_sec_word] + 1,
                lev_matrix[index_first_word, index_sec_word - 1] + 1,
                lev_matrix[index_first_word - 1, index_sec_word - 1] + cost
            )

    return lev_matrix[len(first_word_), len(sec_word_)]


if __name__ == '__main__':
    first_word = input('Enter first word: ')
    sec_word = input('Enter sec word: ')
    print('Dif: ' + str(calc_lev_sim(first_word, sec_word)))
