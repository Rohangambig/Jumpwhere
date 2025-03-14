filter_substring = lambda words, sub: list(filter(lambda word: sub in word, words))

words_list = ['red', 'black', 'white', 'green', 'orange']
print(filter_substring(words_list, 'ack'))
print(filter_substring(words_list, 'abc'))
