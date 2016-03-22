import unittest

EXERCISES = True

if EXERCISES:
    from exercises.strings import string_formatting, extract_words, \
        only_alphanumeric, drumpf, extract_usa_phone_numbers
else:
    from answers.strings import string_formatting, extract_words, \
        only_alphanumeric, drumpf, extract_usa_phone_numbers


class StringExercises(unittest.TestCase):
    def test_string_formatting(self):
        value = 100.01887
        amount = 0.00293911
        item = "uranium"
        self.assertEqual(
            string_formatting(amount, value, item),
            '0.00294 grams of uranium cost $100.02')

    def test_extract_words(self):
        sent = "I want to go to the store."
        self.assertEqual(extract_words(sent), [
            'i', 'want', 'to', 'go', 'to', 'the', 'store'])

        sent = "  \tThis\n is a great. Story of mine it's quite   wonderful\n\n\n\t"
        self.assertEqual(extract_words(sent), [
            'this', 'is', 'a', 'great', 'story',
            'of', 'mine', 'it\'s', 'quite', 'wonderful'])

    def test_only_alphanumeric(self):
        s = "j2r98232f)302498*@@#(*$&(@#*$7048$(*$&!)*^*!&@^$*!@$L<{:>E@{!3b@OE<)@!(@EN"
        self.assertEqual(only_alphanumeric(s), 'j2r98232f3024987048LE3bOEEN')
        s = ""
        self.assertEqual(only_alphanumeric(s), "")

    def test_drumpf(self):
        s = "Donald Trump has golden hair."
        self.assertEqual(drumpf(s), "Donald Drumpf has golden hair.")

    def test_extract_usa_phone_numbers(self):
        text = '4023105900 afjeiwfh2f, 483-1239283 (420)-328-2131'
        self.assertEqual(extract_usa_phone_numbers(text), [
            '4023105900', '483-1239283', '(420)-328-2131'])
