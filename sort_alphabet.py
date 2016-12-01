import unittest


def sort_alphabet(list):
    list_size = len(list) - 1
    change = True

    while change:
        change = False

        for index in range(list_size):

            if list[index] > list[index + 1]:
                aux = list[index]
                list[index] = list[index + 1]
                list[index + 1] = aux

                change = True

    return list

class TestSortAlphabet(unittest.TestCase):

    def test_sort_alphabet(self):
        alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        unordered_alphabet = ['J','O','P','K','B','F','Q','U','S','Z','D','X','W','N','E','C','G','Y','I','T','H','V','M','L','R','A']
        self.assertEqual(sort_alphabet(unordered_alphabet), alphabet)

if __name__ == '__main__':
    unittest.main()