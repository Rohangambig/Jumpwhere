def CollectDictionary(string):
    dictionary = {}

    for char in string:
        if char in dictionary: dictionary[char] += 1
        else: dictionary[char] = 1
    return dictionary

def Anagram(string1,string2):
    if len(string1) !=  len(string2): return False
 
    dict1 = {}
    dict2 = {}

    dict1 = CollectDictionary(string1)
    dict2 = CollectDictionary(string2)

    return dict1 == dict2


def AnagramSort(string1,string2):

    string1 = list(string1)
    string2 = list(string2)

    string1.sort()
    string2.sort()

    return string1 == string2

if __name__ == "__main__":
    print("Is anagram : ",Anagram("garden",'danger'))
    print("Is anagram : ",Anagram("Hello","World"))

    print("Is anagram : ",AnagramSort("garden",'danger'))
    print("Is anagram : ",AnagramSort("Hello","World"))