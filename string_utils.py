# -*- coding: utf-8 -*-
"""String validation utility"""

import re
from unicodedata import normalize


def text_number_to_int(input_string: str) -> int:
    """Convert text number to integer.
    Example:
        text_number_to_int("zero") returns 0

    Args:
        input_string: Text number as a string.

    Returns:
        Integer if valid, None if invalid

    """
    NUMBERS_DICT = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
    }
    # Check if text is empty
    if len(input_string) < 3:
        return None

    # Check if text
    if input_string in NUMBERS_DICT:
        return NUMBERS_DICT[input_string]
    else:
        return None


def string_starts_with_a_capital_letter(text: str) -> bool:
    """Does a given string start with a capital letter.
    Example:
        string_starts_with_a_capital_letter("My string") returns True
        string_starts_with_a_capital_letter("my string") returns False
        string_starts_with_a_capital_letter('Δέλτα') returns True
        string_starts_with_a_capital_letter('δέλτα') returns False

    Args:
        text: Text string.

    Returns:
        True if string starts with a capital letter, False otherwise

    """
    # Normalize the string - À becomes two separate characters A ̀
    first_letter = normalize('NFKD', text)[0]
    return first_letter == first_letter.upper()


def string_has_an_even_number_of_english_quotation_marks(text: str) -> bool:
    """Does a given string start have an even number of quotation marks.
    Example:
        string_has_an_even_number_of_english_quotation_marks("'abc'")
        returns True
        string_has_an_even_number_of_english_quotation_marks("It's")
        returns False

    Args:
        text: Text string.

    Returns:
        True if the number of quotation marks is even, False if not even

    """
    # Return immediately if string length less than 2
    if len(text) < 2:
        return False
    # Count all quotation marks
    QUOTATION_MARKS = ("'", '"', '‘', '’', '‚', '‛', '“', '”', '„', '‟')
    count = 0

    for character in text:
        for quote_mark in QUOTATION_MARKS:
            if character == quote_mark:
                count += 1
    return count % 2 == 0


def string_ends_with_a_period(text: str) -> bool:
    """Does a given string end with a period.
    Example:
        string_ends_with_a_period("Ends with a period.") returns True
        string_ends_with_a_period("Doesn't end with a period") returns False

    Args:
        text: Text string.

    Returns:
        True if the string ends with a period, False otherwise

    """
    # Return immediately if string length less than 1
    if len(text) < 1:
        return False
    return text[-1] == '.'


def string_has_no_extra_period_characters(text: str) -> bool:
    """Does a given string have more than one period at the end of sentence.
    Example:
        string_has_no_extra_period_characters("No extra periods.") returns True
        string_has_no_extra_period_characters("Extra.period.characters.")
        returns False

    Args:
        text: Text string.

    Returns:
        True if the string contains a single period character at the end
        False otherwise

    """
    if string_ends_with_a_period(text) is False:
        return False

    for character in text[:-1]:
        if character == '.':
            return False
    return True


def numbers_less_than_thirteen_are_spelled_out(text: str) -> bool:
    """Are numbers less than 13 spelled out.
    Example:
        numbers_less_than_thirteen_are_spelled_out("one is less than 13")
        returns True

        numbers_less_than_thirteen_are_spelled_out("1 is less than 13")
        returns False

    Args:
        text: Text string.

    Returns:
        True if all numbers are greater than 13
        False otherwise

    """
    # Find any numbers in the string
    numbers = re.findall('\d+', text)
    for number in numbers:
        # Convert each number to int
        # Check if each number is less than 13
        if int(number) < 13:
            return False
    return True


def sentence_is_valid(text: str) -> bool:
    """Checks if a sentence is valid based on the following rules.

    String starts with a capital letter
    String has an even number of quotation marks
    String ends with a period character “."
    String has no period characters other than the last character
    Numbers below 13 are spelled out (”one”, “two”, "three”, etc…)

    Example:
        sentence_is_valid("One lazy dog is too few, 13 is too many.")
        returns True

        sentence_is_valid("One lazy dog is too few, 12 is too many.")
        returns False

    Args:
        text: Text string.

    Returns:
        True if sentence is valid
        False otherwise

    """

    # String starts with a capital letter
    if string_starts_with_a_capital_letter(text) is False:
        return False

    # String has an even number of quotation marks
    if string_has_an_even_number_of_english_quotation_marks(text) is False:
        return False

    # String ends with a period character “."
    if string_ends_with_a_period(text) is False:
        return False

    # String has no period characters other than the last character
    if string_ends_with_a_period(text) is False:
        return False
    if string_has_no_extra_period_characters(text) is False:
        return False

    # Numbers below 13 are spelled out (”one”, “two”, "three”, etc…)
    if numbers_less_than_thirteen_are_spelled_out(text) is False:
        return False

    return True
