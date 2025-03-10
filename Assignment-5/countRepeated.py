from collections import Counter

def countRepeatedCharacter(string):
    dict = Counter(string)

    for keys,values in dict.items():
        if values > 1:
            print(keys,' -> ', values)

countRepeatedCharacter("thequickbrownfoxjumpsoverthelazydog")