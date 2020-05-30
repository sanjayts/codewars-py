# https://www.codewars.com/kata/vigenere-cipher-helper/train/python
from typing import Dict, List

import test
import itertools


class VigenereCipher(object):

    def __init__(self, key: str, alphabet: str):
        self.ch_to_row = {}  # type: Dict[str, str]
        self.ch_to_idx = {}  # type: Dict[str, int]
        for (i, c) in enumerate(alphabet):
            self.ch_to_row[c] = alphabet[i:] + alphabet[:i]
            self.ch_to_idx[c] = i

        k_len = len(key)
        self.key = key

    def encode(self, text: str) -> str:
        chars = []
        for c in text:

        pass

    def decode(self, text: str) -> str:
        pass




s = "abcdefghijklmnopqrstuvwxyz"
k = "password"
cipher = VigenereCipher(k, s)

#
# test.assert_equals(cipher.encode('codewars'), 'rovwsoiv')
# test.assert_equals(cipher.decode('rovwsoiv'), 'codewars')
#
# test.assert_equals(cipher.encode('waffles'), 'laxxhsj')
# test.assert_equals(cipher.decode('laxxhsj'), 'waffles')
#
# test.assert_equals(cipher.encode('CODEWARS'), 'CODEWARS')
# test.assert_equals(cipher.decode('CODEWARS'), 'CODEWARS')
