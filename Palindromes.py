from collections import deque
import re

class Palindrome:
    def __init__(self):  
        self.stack = []
        self.queue = []

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        self.queue.append(ch)


    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.pop(0)


def is_palindrome(text : str) -> bool:
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()## the lower case is to avoid character mismatch like when we have "A" and "a"

    obj = Palindrome()
    for char in cleaned:
        obj.pushCharacter(char)
        obj.enqueueCharacter(char)

    for i in range(len(cleaned) // 2):
        if obj.popCharacter() != obj.dequeueCharacter():
            return False
    return True