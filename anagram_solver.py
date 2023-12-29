import itertools
from PyDictionary import PyDictionary

def perm(word):
    dict = PyDictionary()
    letter = [i for i in word]
    bob = set(itertools.permutations(letter))
    for bobs in bob:
        billy = "".join(bobs).lower()
        if dict.meaning(billy):
            print(billy)

ask = input("Enter: ")
perm(ask)


