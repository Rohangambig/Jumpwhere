def lenghtMaximum(arr):
    ans = 0

    for words in arr:
        if ans < len(words):
            ans = len(words)
    
    return ans 

print(lenghtMaximum(["apple", "banana", "strawberry", "kiwi", "pineapple"]))
print(lenghtMaximum(["elephant", "tiger", "crocodile", "dog", "chimpanzee"]))