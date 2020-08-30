from itertools import takewhile
from operator import itemgetter

def longestCommonPrefix(strs: list) -> str:
    a = takewhile(lambda x: len(set(x)) == 1, zip(*strs))
    f = map(itemgetter(0), a)
    return ''.join(f)
    

"""
TEST CASES
["aaa","aa","aaa"]
["dog","racecar","car"]
["flower","flow","flight"]
["a", "aa"]
"""
