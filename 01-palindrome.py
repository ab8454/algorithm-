import collections
import re


class foo:
    def isPalindrome1(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

    def isPalindrome2(self, s: str) -> bool:
        strs: collections.deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

    def isPalindrome3(self, s:str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]

s = 'absba'
f = foo()
print(f.isPalindrome1(s))
print(f.isPalindrome2(s))
print(f.isPalindrome3(s))
