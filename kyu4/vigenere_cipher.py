# https://www.codewars.com/kata/vigenere-cipher-helper/train/python

import test


class VigenereCipher(object):

    def __init__(self, key: str, alphabet: str):
        pass

    def encode(self, text: str) -> str:
        pass

    def decode(self, text: str) -> str:
        pass


s = "abcdefghijklmnopqrstuvwxyz"
k = "password"
c = VigenereCipher(k, s)

test.assert_equals(c.encode('codewars'), 'rovwsoiv')
test.assert_equals(c.decode('rovwsoiv'), 'codewars')

test.assert_equals(c.encode('waffles'), 'laxxhsj')
test.assert_equals(c.decode('laxxhsj'), 'waffles')

test.assert_equals(c.encode('CODEWARS'), 'CODEWARS')
test.assert_equals(c.decode('CODEWARS'), 'CODEWARS')
