#!/usr/bin/python3
# -*- coding: utf-8 -*-

import string_utils


def main():
    # Delta
    print(string_utils.string_starts_with_a_capital_letter('Δέλτα'))

    # delta
    print(string_utils.string_starts_with_a_capital_letter('δέλτα'))

    print(string_utils.string_has_an_even_number_of_english_quotation_marks(
        'Testing "123"'))
    print(string_utils.string_has_an_even_number_of_english_quotation_marks(
        'Testing 123"'))
    print(string_utils.string_has_an_even_number_of_english_quotation_marks(
        ''))
    print(string_utils.string_has_an_even_number_of_english_quotation_marks(
        '"'))
    print(string_utils.string_has_an_even_number_of_english_quotation_marks(
        "'" ''"'"))

    print(string_utils.sentence_is_valid(
        'The quick brown fox said “hello Mr lazy dog”.'))


if __name__ == '__main__':
    main()
