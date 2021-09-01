# -*- coding: utf-8 -*-

import unittest
import string_utils


class Test(unittest.TestCase):
    VALID_SENTENCES = (
        'The quick brown fox said “hello Mr lazy dog”.',
        'The quick brown fox said hello Mr lazy dog.',
        'One lazy dog is too few, 13 is too many.',
        'One lazy dog is too few, thirteen is too many.'
    )
    INVALID_SENTENCES = (
        'The quick brown fox said "hello Mr. lazy dog".',
        'the quick brown fox said “hello Mr lazy dog”.',
        '"The quick brown fox said “hello Mr lazy dog."',
        'One lazy dog is too few, 12 is too many.'
    )

    # Test text number to int conversion
    def test_text_number_to_int(self):
        # Test positive numbers from 0 to 20 - English
        TEXT_NUMBERS = (
            'zero', 'one', 'two', 'three', 'four', 'five', 'six',
            'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
            'thirteen', 'fourteen', 'fifteen', 'sixteen',
            'seventeen', 'eighteen', 'nineteen', 'twenty'
        )

        for number in range(0, 21):
            actual = number
            expected = string_utils.text_number_to_int(TEXT_NUMBERS[number])

            self.assertEqual(actual, expected,
                             f"Actual: {actual}, Expected: {expected}")

        # Test invalid inputs
        # Valid number with whitespace
        self.assertEqual(string_utils.text_number_to_int(" one"), None)
        self.assertEqual(string_utils.text_number_to_int(" one "), None)

        # Tab character + valid number
        self.assertEqual(string_utils.text_number_to_int("\tone"), None)

        # Positive numbers outside of specification
        self.assertEqual(string_utils.text_number_to_int("thirty"), None)

        # Non-English numbers
        # Two in French - deux
        self.assertEqual(string_utils.text_number_to_int("deux"), None)

        # Empty string
        self.assertEqual(string_utils.text_number_to_int(""), None)

    # String starts with a capital letter
    def test_string_starts_with_a_capital_letter_returns_true(self):
        sentence = 'The quick brown fox said “hello Mr lazy dog”.'
        self.assertEqual(string_utils.
                         string_starts_with_a_capital_letter("Text"), True)
        self.assertEqual(string_utils.
                         string_starts_with_a_capital_letter(sentence), True)

        # Unicode capital letters
        # Greek - Delta = Δέλτα
        self.assertEqual(
            string_utils.string_starts_with_a_capital_letter('Δέλτα'),
            True,
            'Δέλτα')

    def test_string_starts_with_a_capital_letter_returns_false(self):
        sentence = 'the quick brown fox said “hello Mr lazy dog”.'
        self.assertEqual(string_utils.
                         string_starts_with_a_capital_letter("text"), False)
        self.assertEqual(string_utils.
                         string_starts_with_a_capital_letter(sentence), False)
        # Greek - delta = δέλτα
        self.assertEqual(
            string_utils.string_starts_with_a_capital_letter('δέλτα'),
            False,
            'δέλτα')

    # String has an even number of quotation marks
    # Unicode reference - https://www.unicode.org/charts/PDF/U2000.pdf
    # General Punctuation - pg 3 & 4 - Quotation marks and apostrophe
    def test_string_has_an_even_number_of_quotation_marks_returns_true(self):
        SENTENCES_WITH_EVEN_QUOTATION_MARKS = (
            'Testing "123"',  # 2 double quotes
            '""',  # 2 double quotes
            "''",  # 2 single quotes
            '""" """',  # 6 double quotes
            "'" ''"'",  # 4 single quotes, 2 double quotes
            '‘ ’',  # 2 unicode single quotes, LEFT and RIGHT SINGLE
            '‚ ‚',  # 2 unicode single quotes, SINGLE LOW-9 QUOTATION MARK
            '‛ ‛',  # 2 unicode single quotes, SINGLE HIGH-REVERSED-9
            # 2 unicode double quotes, LEFT DOUBLE QUOTATION MARK (U+201C) and
            # RIGHT DOUBLE QUOTATION MARK (U+201D)
            'The quick brown fox said “hello Mr lazy dog”',
            # 2 unicode double quotes, DOUBLE LOW-9 QUOTATION MARK (U+201E) and
            # DOUBLE HIGH-REVERSED-9 QUOTATION MARK (U+201F)
            'The quick brown fox said „hello Mr lazy dog‟',
        )
        for sentence in SENTENCES_WITH_EVEN_QUOTATION_MARKS:
            self.assertEquals(
                string_utils.
                string_has_an_even_number_of_english_quotation_marks(
                    sentence),
                True,
                f"{sentence}")

    def test_string_has_an_even_number_of_quotation_marks_returns_false(self):
        SENTENCES_WITH_EVEN_QUOTATION_MARKS = (
            'Testing 123"',  # 1 double quote
            '"',  # 1 double quote, no text
            "'",  # 1 single quote
            '""" ""',  # 5 double quotes
            "''" ''"'",  # 5 single quotes, 2 double quotes
            '‘',  # 1 unicode single quote, LEFT SINGLE QUOTATION MARK (U+2018)
            # 1 unicode single quote, RIGHT SINGLE QUOTATION MARK (U+2019)
            '’',
            # 1 unicode single quote, SINGLE LOW-9 QUOTATION MARK (U+201A)
            '‚',
            # 1 unicode single quote, SINGLE HIGH-REVERSED-9 QUOTATION MARK
            # (U+201B)
            '‛',
            # 1 unicode double quote, LEFT DOUBLE QUOTATION MARK (U+201C)
            'The quick brown fox said “hello Mr lazy dog',
            # 1 unicode double quote, RIGHT DOUBLE QUOTATION MARK (U+201D)
            'The quick brown fox said hello Mr lazy dog”',
            # 1 unicode double quote, DOUBLE LOW-9 QUOTATION MARK (U+201E)
            'The quick brown fox said „hello Mr lazy dog',
            # 1 unicode double quote, DOUBLE HIGH-REVERSED-9 QUOTATION MARK
            # (U+201F)
            'The quick brown fox said hello Mr lazy dog‟',
        )
        for sentence in SENTENCES_WITH_EVEN_QUOTATION_MARKS:
            self.assertEquals(
                string_utils.
                string_has_an_even_number_of_english_quotation_marks(sentence),
                False, f"{sentence}")

        # Empty string
        self.assertEquals(
            string_utils.
            string_has_an_even_number_of_english_quotation_marks(""),
            False)

    # String ends with a period character “."
    def test_string_ends_with_a_period_returns_true(self):
        for sentence in self.VALID_SENTENCES:
            self.assertEquals(string_utils.
                              string_ends_with_a_period(sentence), True)
        # Multiple period characters in string
        self.assertEquals(string_utils.
                          string_ends_with_a_period(".multiple.period.chars."),
                          True)

    def test_string_ends_with_a_period_returns_false(self):
        sentences = (
            '',  # Empty string
            'Period. mid sentence',
            '.Sentence starts with a period',
        )
        for sentence in sentences:
            self.assertEquals(string_utils.
                              string_ends_with_a_period(sentence), False)

    # String has no period characters other than the last character
    def test_string_has_no_extra_period_characters_returns_true(self):
        for sentence in self.VALID_SENTENCES:
            self.assertEquals(string_utils.
                              string_has_no_extra_period_characters(sentence),
                              True, f"{sentence}")

    def test_string_has_no_extra_period_characters_returns_false(self):
        # String with all period characters
        self.assertEquals(
            string_utils.string_has_no_extra_period_characters("..."), False)

        # String with period characters at the end
        self.assertEquals(
            string_utils.string_has_no_extra_period_characters("Etc..."),
            False)

    # Numbers below 13 are spelled out (”one”, “two”, "three”, etc…)
    def test_numbers_below_13_are_spelled_out_returns_true(self):
        #
        self.assertEquals(
            string_utils.numbers_less_than_thirteen_are_spelled_out(""), True)
        for sentence in self.VALID_SENTENCES:
            self.assertEqual(string_utils.
                             numbers_less_than_thirteen_are_spelled_out(
                                 sentence), True, f"{sentence}")

    def test_numbers_below_13_are_spelled_out_returns_false(self):
        for number in range(0, 13):
            number_string = str(number)
            self.assertEqual(string_utils.
                             numbers_less_than_thirteen_are_spelled_out(
                                 number_string), False, f"{number_string}")
    # Sentence is valid

    def test_sentence_is_valid_returns_true(self):
        for sentence in self.VALID_SENTENCES:
            self.assertEqual(string_utils.sentence_is_valid(
                sentence), True, f"{sentence}")

    def test_sentence_is_valid_returns_false(self):
        for sentence in self.INVALID_SENTENCES:
            self.assertEqual(string_utils.sentence_is_valid(
                sentence), False, f"{sentence}")


if __name__ == "__main__":
    unittest.main()
